"""Layer 0 (substrate) — the local data store.

A thin wrapper over the standard-library ``sqlite3`` module. We deliberately
avoid a heavyweight database or ORM for v1: a single local file is the simplest
thing that is genuinely *sovereign* (nothing leaves the machine) and trivial to
self-host. The schema is small on purpose — each table maps to a concept a
non-technical founder can hold in their head.
"""
from __future__ import annotations

import os
import sqlite3
from datetime import datetime, timezone

from . import config


def now() -> str:
    """UTC timestamp, second precision — used everywhere for audit consistency."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def connect(path: str | None = None) -> sqlite3.Connection:
    """Open a connection. ``check_same_thread=False`` lets the API server share
    one connection across request threads (fine for a single-process v1)."""
    resolved = path or os.environ.get("DECISION_OS_DB", config.DB_PATH)
    conn = sqlite3.connect(resolved, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    username      TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    salt          TEXT NOT NULL,
    role          TEXT NOT NULL,          -- admin | executive | member
    department    TEXT NOT NULL,
    display_name  TEXT NOT NULL,
    created_ts    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tokens (
    token      TEXT PRIMARY KEY,
    user_id    INTEGER NOT NULL REFERENCES users(id),
    created_ts TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS datasets (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    name         TEXT NOT NULL,
    source_type  TEXT NOT NULL,           -- which connector produced it
    department   TEXT NOT NULL,
    created_ts   TEXT NOT NULL,
    record_count INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS records (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    dataset_id INTEGER NOT NULL REFERENCES datasets(id),
    department TEXT NOT NULL,
    text       TEXT NOT NULL,             -- searchable, human-readable form
    data       TEXT NOT NULL,             -- original row as JSON
    created_ts TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS audit (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    ts     TEXT NOT NULL,
    actor  TEXT NOT NULL,
    action TEXT NOT NULL,
    detail TEXT NOT NULL
);
"""


def init_db(conn: sqlite3.Connection) -> None:
    """Create tables if they do not exist. Safe to call on every startup."""
    conn.executescript(SCHEMA)
    conn.commit()
