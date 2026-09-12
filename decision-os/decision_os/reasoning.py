"""Layer 4 — Reasoning & agents (the decision engine).

The engine is deliberately model-*agnostic*: it talks to a ``ModelProvider``
interface, never to a specific vendor. That is the "own the orchestration, rent
the intelligence" principle in code — you can swap the brain (a local model,
Anthropic, OpenAI, a self-hosted open-weight model) without touching anything
else.

v1 ships a fully-working ``LocalProvider`` that runs offline with zero API keys
and zero network calls, so the sovereign guarantee holds out of the box. It is
a deterministic baseline: it grounds every answer in retrieved evidence and
cites its sources. Plug a real LLM into ``ExternalLLMProvider`` when you decide
to trade some sovereignty for more fluent reasoning.
"""
from __future__ import annotations

import abc
import sqlite3
from typing import Any

from . import config, governance, semantic


class ModelProvider(abc.ABC):
    """The one interface the engine reasons through."""

    name: str = ""

    @abc.abstractmethod
    def generate(self, question: str, evidence: list[dict[str, Any]]) -> dict[str, Any]:
        """Return a structured decision brief grounded in ``evidence``."""
        raise NotImplementedError


class LocalProvider(ModelProvider):
    """Offline, deterministic baseline. No keys, no network, nothing leaves the box."""

    name = "local-offline (deterministic baseline)"

    def generate(self, question: str, evidence: list[dict[str, Any]]) -> dict[str, Any]:
        if not evidence:
            return {
                "recommendation": "Not enough connected data to make this call yet.",
                "summary": "No relevant records were found for this question.",
                "key_points": [],
                "confidence": 0.0,
                "provider": self.name,
                "citations": [],
                "departments_considered": [],
            }

        departments = sorted({e["department"] for e in evidence})
        matched = [e for e in evidence if e.get("score", 0) > 0]
        grounded = matched or evidence

        key_points = [
            {
                "department": e["department"],
                "dataset": e["dataset"],
                "detail": (e["text"][:220] + "…") if len(e["text"]) > 220 else e["text"],
            }
            for e in grounded[:5]
        ]

        # Confidence is a transparent heuristic: more corroborating evidence and
        # broader keyword overlap => higher confidence, capped so the baseline
        # never overclaims.
        overlap = sum(e.get("score", 0) for e in grounded)
        confidence = round(min(0.85, 0.25 + 0.08 * len(matched) + 0.03 * overlap), 2)
        if not matched:
            confidence = 0.15  # fell back to recency; be honest about it.

        dept_phrase = ", ".join(departments)
        recommendation = (
            f"Based on {len(grounded)} record(s) across {dept_phrase}, the "
            f"strongest evidence for \"{question.strip()}\" is summarised below. "
            "Review the cited records before acting."
        )
        if not matched:
            recommendation = (
                f"No records directly matched \"{question.strip()}\". Showing the "
                f"most recent context from {dept_phrase} instead — treat as low "
                "confidence and consider connecting more data."
            )

        return {
            "recommendation": recommendation,
            "summary": f"{len(grounded)} evidence record(s) drawn from: {dept_phrase}.",
            "key_points": key_points,
            "confidence": confidence,
            "provider": self.name,
            "citations": [
                {"record_id": e["record_id"], "dataset": e["dataset"],
                 "department": e["department"]}
                for e in grounded
            ],
            "departments_considered": departments,
        }


class ExternalLLMProvider(ModelProvider):
    """Skeleton for a real LLM. Implement ``generate`` to call your model of
    choice — pass ``evidence`` as grounding context and require citations back.

    Kept as a stub on purpose: enabling it is a deliberate sovereignty trade-off
    (data may leave the box), so it must be opted into, never on by default.
    """

    name = "external-llm"

    def generate(self, question: str, evidence: list[dict[str, Any]]) -> dict[str, Any]:
        raise NotImplementedError(
            "External LLM provider not configured. Implement generate() to call "
            "your model (e.g. Anthropic, OpenAI, or a self-hosted open model), "
            "then set DECISION_OS_PROVIDER=external."
        )


_PROVIDERS: dict[str, type[ModelProvider]] = {
    "local": LocalProvider,
    "external": ExternalLLMProvider,
}


def get_provider(name: str | None = None) -> ModelProvider:
    key = name or config.MODEL_PROVIDER
    if key not in _PROVIDERS:
        raise ValueError(f"unknown provider {key!r}; available: {sorted(_PROVIDERS)}")
    return _PROVIDERS[key]()


class DecisionEngine:
    """Orchestrates a decision end-to-end: scope -> retrieve -> reason -> audit."""

    def __init__(self, conn: sqlite3.Connection, provider: ModelProvider | None = None):
        self.conn = conn
        self.provider = provider or get_provider()

    def decide(self, user: sqlite3.Row, question: str) -> dict[str, Any]:
        # 1. Governance: only reason over data this user is allowed to see.
        departments = governance.accessible_departments(self.conn, user)
        # 2. Semantic layer: retrieve grounding evidence within that scope.
        evidence = semantic.retrieve(
            self.conn, question, departments, limit=config.RETRIEVAL_LIMIT
        )
        # 3. Reasoning: produce a grounded, cited brief.
        brief = self.provider.generate(question, evidence)
        brief["scope"] = departments
        brief["question"] = question
        # 4. Governance: record the decision for audit.
        governance.audit_log(
            self.conn,
            actor=user["username"],
            action="decision",
            detail=f"q={question!r} scope={departments} "
                   f"provider={brief['provider']} confidence={brief['confidence']}",
        )
        return brief
