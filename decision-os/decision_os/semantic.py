"""Layer 3 — the Semantic layer ("one brain").

Data arrives from many silos in many shapes. This layer normalises every row
into a common record — a searchable text form plus the original structured
data — and stores it against a department. That is what lets a single question
reach across Sales, Finance, Operations, and more as if they were one system.

Retrieval in v1 is transparent keyword matching (no black box, no external
service). It is the seam where a vector index / knowledge graph slots in later
without changing anything above or below it.
"""
from __future__ import annotations

import json
import re
import sqlite3
from typing import Any

from .connectors import get_connector
from .db import now

_STOPWORDS = {
    "the", "a", "an", "of", "to", "in", "for", "and", "or", "is", "are", "be",
    "on", "at", "by", "we", "our", "my", "i", "should", "what", "which", "how",
    "do", "does", "with", "this", "that", "it", "as", "from", "can",
}


def tokenize(text: str) -> list[str]:
    return [
        w for w in re.findall(r"[a-z0-9]+", text.lower())
        if len(w) > 1 and w not in _STOPWORDS
    ]


def normalize_row(row: dict[str, Any]) -> tuple[str, str]:
    """Turn a raw source row into (searchable_text, json_data)."""
    text = " | ".join(f"{k}: {v}" for k, v in row.items())
    return text, json.dumps(row, default=str)


def ingest(
    conn: sqlite3.Connection,
    connector_name: str,
    config: dict[str, Any],
    dataset_name: str,
    department: str,
) -> dict[str, Any]:
    """Pull rows from a connector and land them in the unified store."""
    connector = get_connector(connector_name)
    cur = conn.execute(
        "INSERT INTO datasets (name, source_type, department, created_ts) "
        "VALUES (?, ?, ?, ?)",
        (dataset_name, connector_name, department, now()),
    )
    dataset_id = int(cur.lastrowid)

    count = 0
    for row in connector.fetch(config):
        text, data = normalize_row(row)
        conn.execute(
            "INSERT INTO records (dataset_id, department, text, data, created_ts) "
            "VALUES (?, ?, ?, ?, ?)",
            (dataset_id, department, text, data, now()),
        )
        count += 1

    conn.execute(
        "UPDATE datasets SET record_count = ? WHERE id = ?", (count, dataset_id)
    )
    conn.commit()
    return {"dataset_id": dataset_id, "name": dataset_name,
            "department": department, "record_count": count}


def list_datasets(
    conn: sqlite3.Connection, departments: list[str] | None = None
) -> list[dict[str, Any]]:
    if departments is None:
        rows = conn.execute("SELECT * FROM datasets ORDER BY id DESC").fetchall()
    else:
        if not departments:
            return []
        placeholders = ",".join("?" * len(departments))
        rows = conn.execute(
            f"SELECT * FROM datasets WHERE department IN ({placeholders}) "
            "ORDER BY id DESC",
            departments,
        ).fetchall()
    return [dict(r) for r in rows]


def retrieve(
    conn: sqlite3.Connection,
    query: str,
    departments: list[str],
    limit: int = 6,
) -> list[dict[str, Any]]:
    """Return the most relevant records the caller is allowed to see.

    Relevance = number of distinct query terms found in a record, newest first
    on ties. If nothing matches, fall back to the most recent records so a
    decision is never silently starved of context (the engine flags low
    confidence in that case).
    """
    if not departments:
        return []
    placeholders = ",".join("?" * len(departments))
    rows = conn.execute(
        f"SELECT r.*, d.name AS dataset_name FROM records r "
        f"JOIN datasets d ON d.id = r.dataset_id "
        f"WHERE r.department IN ({placeholders})",
        departments,
    ).fetchall()

    terms = set(tokenize(query))
    scored = []
    for r in rows:
        record_terms = set(tokenize(r["text"]))
        score = len(terms & record_terms)
        scored.append((score, r["id"], r))

    scored.sort(key=lambda t: (t[0], t[1]), reverse=True)
    matched = [t for t in scored if t[0] > 0]
    chosen = (matched or scored)[:limit]

    return [
        {
            "record_id": r["id"],
            "dataset": r["dataset_name"],
            "department": r["department"],
            "text": r["text"],
            "data": json.loads(r["data"]),
            "score": score,
        }
        for score, _id, r in chosen
    ]
