"""Layer 1 — Governance & sovereignty.

In the enterprise, this layer is the *license to walk in the door*, not a
finishing touch. v1 covers the essentials so the guarantees are real from day
one:

  * Identity & auth       - salted PBKDF2 password hashing, opaque session tokens.
  * Role-based access      - who can see which departments' data, and who can
                            administer the platform.
  * Audit trail           - every consequential action is recorded with who,
                            what, and when.

The RBAC model is deliberately small and department-agnostic: departments are
just strings, so the platform stays horizontal — Sales, Legal, or a department
that doesn't exist yet all work the same way.
"""
from __future__ import annotations

import hashlib
import hmac
import secrets
import sqlite3

from .db import now

# --- Roles -----------------------------------------------------------------
# admin      : manage users, connect data sources, see everything + audit log.
# executive  : read across ALL departments (this is what powers cross-silo,
#              enterprise-wide decisions), plus the audit log.
# member     : read only their OWN department's data.
ROLES = ("admin", "executive", "member")

_PBKDF2_ROUNDS = 200_000


# --- Password hashing ------------------------------------------------------
def hash_password(password: str, salt: str | None = None) -> tuple[str, str]:
    """Return ``(hash_hex, salt_hex)``. Never store raw passwords."""
    salt = salt or secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), bytes.fromhex(salt), _PBKDF2_ROUNDS
    )
    return digest.hex(), salt


def verify_password(password: str, salt: str, expected_hash: str) -> bool:
    candidate, _ = hash_password(password, salt)
    return hmac.compare_digest(candidate, expected_hash)


# --- Users & sessions ------------------------------------------------------
def create_user(
    conn: sqlite3.Connection,
    username: str,
    password: str,
    role: str,
    department: str,
    display_name: str,
) -> int:
    if role not in ROLES:
        raise ValueError(f"role must be one of {ROLES}, got {role!r}")
    pw_hash, salt = hash_password(password)
    cur = conn.execute(
        "INSERT INTO users (username, password_hash, salt, role, department, "
        "display_name, created_ts) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (username, pw_hash, salt, role, department, display_name, now()),
    )
    conn.commit()
    return int(cur.lastrowid)


def get_user_by_username(conn: sqlite3.Connection, username: str) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM users WHERE username = ?", (username,)
    ).fetchone()


def authenticate(
    conn: sqlite3.Connection, username: str, password: str
) -> sqlite3.Row | None:
    user = get_user_by_username(conn, username)
    if user and verify_password(password, user["salt"], user["password_hash"]):
        return user
    return None


def issue_token(conn: sqlite3.Connection, user_id: int) -> str:
    token = secrets.token_urlsafe(32)
    conn.execute(
        "INSERT INTO tokens (token, user_id, created_ts) VALUES (?, ?, ?)",
        (token, user_id, now()),
    )
    conn.commit()
    return token


def resolve_token(conn: sqlite3.Connection, token: str) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT u.* FROM tokens t JOIN users u ON u.id = t.user_id "
        "WHERE t.token = ?",
        (token,),
    ).fetchone()


# --- Authorisation ---------------------------------------------------------
def all_departments(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute(
        "SELECT DISTINCT department FROM datasets ORDER BY department"
    ).fetchall()
    return [r["department"] for r in rows]


def accessible_departments(conn: sqlite3.Connection, user: sqlite3.Row) -> list[str]:
    """The departments this user is allowed to see data from."""
    if user["role"] in ("admin", "executive"):
        return all_departments(conn)
    return [user["department"]]


def can_manage(user: sqlite3.Row) -> bool:
    """Connect data sources, manage users, load demo data."""
    return user["role"] == "admin"


def can_view_audit(user: sqlite3.Row) -> bool:
    return user["role"] in ("admin", "executive")


# --- Audit trail -----------------------------------------------------------
def audit_log(conn: sqlite3.Connection, actor: str, action: str, detail: str) -> None:
    conn.execute(
        "INSERT INTO audit (ts, actor, action, detail) VALUES (?, ?, ?, ?)",
        (now(), actor, action, detail),
    )
    conn.commit()


def get_audit(conn: sqlite3.Connection, limit: int = 100) -> list[sqlite3.Row]:
    return conn.execute(
        "SELECT * FROM audit ORDER BY id DESC LIMIT ?", (limit,)
    ).fetchall()
