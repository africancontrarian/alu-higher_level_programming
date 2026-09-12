"""Layer 0 (substrate) — configuration.

Everything is configured through plain environment variables so the platform
can be self-hosted inside a customer's own cloud, VPC, or on-prem box without
code changes. Sensible sovereign defaults: a local SQLite file and the offline
model provider.
"""
from __future__ import annotations

import os

# The unified data store. A single local file by default — data stays in the
# customer's boundary. Point this at a path on an encrypted volume in prod.
DB_PATH: str = os.environ.get("DECISION_OS_DB", "decision_os.db")

# Which reasoning provider the decision engine uses.
#   "local"    -> deterministic, offline, no API keys, nothing leaves the box.
#   "external" -> plug in a real LLM (see reasoning.py). Off by default so the
#                 sovereign guarantee holds until you deliberately opt in.
MODEL_PROVIDER: str = os.environ.get("DECISION_OS_PROVIDER", "local")

# How many pieces of evidence the semantic layer feeds the engine per decision.
RETRIEVAL_LIMIT: int = int(os.environ.get("DECISION_OS_RETRIEVAL_LIMIT", "6"))

APP_NAME: str = "Decision OS"
