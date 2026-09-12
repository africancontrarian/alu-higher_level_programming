"""Layer 5 — Experience (the REST API + web app).

This is how every department interacts with the platform. The API is thin on
purpose: it enforces auth, delegates to the layers below, and returns JSON. The
single-page web app in ``web/index.html`` is served from ``/``.
"""
from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from . import config, connectors, governance, semantic
from .db import connect, init_db
from .reasoning import DecisionEngine
from .seed import ensure_demo_users, seed_demo_data

WEB_DIR = Path(__file__).parent / "web"


@asynccontextmanager
async def lifespan(app: FastAPI):
    conn = connect()
    init_db(conn)
    ensure_demo_users(conn)  # so you can log in on first run
    app.state.conn = conn
    yield
    conn.close()


app = FastAPI(title=config.APP_NAME, version="0.1.0", lifespan=lifespan)


# --- request models --------------------------------------------------------
class LoginIn(BaseModel):
    username: str
    password: str


class IngestIn(BaseModel):
    connector: str
    dataset_name: str
    department: str
    config: dict = {}


class DecideIn(BaseModel):
    question: str


# --- helpers ---------------------------------------------------------------
def _public_user(user) -> dict:
    return {
        "username": user["username"],
        "display_name": user["display_name"],
        "role": user["role"],
        "department": user["department"],
    }


def current_user(authorization: str = Header(default=""), ):
    """Resolve the caller from an ``Authorization: Bearer <token>`` header."""
    token = authorization[7:] if authorization.startswith("Bearer ") else authorization
    user = governance.resolve_token(app.state.conn, token) if token else None
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user


# --- routes ----------------------------------------------------------------
@app.get("/")
def home():
    return FileResponse(WEB_DIR / "index.html")


@app.post("/api/login")
def login(body: LoginIn):
    conn = app.state.conn
    user = governance.authenticate(conn, body.username, body.password)
    if user is None:
        governance.audit_log(conn, body.username, "login_failed", "bad credentials")
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = governance.issue_token(conn, user["id"])
    governance.audit_log(conn, user["username"], "login", "ok")
    return {"token": token, "user": _public_user(user)}


@app.get("/api/me")
def me(user=Depends(current_user)):
    return _public_user(user)


@app.get("/api/connectors")
def list_connectors(user=Depends(current_user)):
    return {"connectors": connectors.available_connectors()}


@app.get("/api/datasets")
def datasets(user=Depends(current_user)):
    depts = governance.accessible_departments(app.state.conn, user)
    return {"scope": depts, "datasets": semantic.list_datasets(app.state.conn, depts)}


@app.post("/api/ingest")
def ingest(body: IngestIn, user=Depends(current_user)):
    if not governance.can_manage(user):
        raise HTTPException(status_code=403, detail="Admin role required to connect data")
    conn = app.state.conn
    try:
        result = semantic.ingest(
            conn, body.connector, body.config, body.dataset_name, body.department
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from None
    governance.audit_log(
        conn, user["username"], "ingest",
        f"connector={body.connector} dataset={body.dataset_name!r} "
        f"dept={body.department} rows={result['record_count']}",
    )
    return result


@app.post("/api/decide")
def decide(body: DecideIn, user=Depends(current_user)):
    if not body.question.strip():
        raise HTTPException(status_code=400, detail="Question must not be empty")
    engine = DecisionEngine(app.state.conn)
    return engine.decide(user, body.question)


@app.get("/api/audit")
def audit(user=Depends(current_user)):
    if not governance.can_view_audit(user):
        raise HTTPException(status_code=403, detail="Not permitted to view the audit log")
    rows = governance.get_audit(app.state.conn)
    return {"entries": [dict(r) for r in rows]}


@app.post("/api/seed")
def seed(user=Depends(current_user)):
    if not governance.can_manage(user):
        raise HTTPException(status_code=403, detail="Admin role required")
    loaded = seed_demo_data(app.state.conn)
    governance.audit_log(
        app.state.conn, user["username"], "seed_demo", f"datasets={len(loaded)}"
    )
    return {"loaded": loaded}
