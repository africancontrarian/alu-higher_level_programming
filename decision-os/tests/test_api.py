"""End-to-end API tests via FastAPI's TestClient."""
import os

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client(tmp_path):
    os.environ["DECISION_OS_DB"] = str(tmp_path / "api.db")
    from decision_os.api import app  # imported after env is set

    with TestClient(app) as c:
        yield c
    os.environ.pop("DECISION_OS_DB", None)


def _login(client, username, password):
    r = client.post("/api/login", json={"username": username, "password": password})
    assert r.status_code == 200, r.text
    return r.json()["token"]


def _auth(token):
    return {"Authorization": "Bearer " + token}


def test_bad_login_rejected(client):
    r = client.post("/api/login", json={"username": "admin", "password": "nope"})
    assert r.status_code == 401


def test_admin_can_seed_and_decide(client):
    token = _login(client, "admin", "admin123")
    assert client.post("/api/seed", headers=_auth(token)).status_code == 200

    datasets = client.get("/api/datasets", headers=_auth(token)).json()
    depts = {d["department"] for d in datasets["datasets"]}
    assert {"Sales", "Finance", "Operations"} <= depts

    brief = client.post(
        "/api/decide", headers=_auth(token),
        json={"question": "where are we over budget or at churn risk?"},
    ).json()
    assert brief["recommendation"]
    assert brief["citations"]


def test_member_scope_and_permissions(client):
    admin = _login(client, "admin", "admin123")
    client.post("/api/seed", headers=_auth(admin))

    sales = _login(client, "sales1", "sales123")
    datasets = client.get("/api/datasets", headers=_auth(sales)).json()
    assert datasets["scope"] == ["Sales"]
    assert all(d["department"] == "Sales" for d in datasets["datasets"])

    # members cannot connect data or read the audit log
    assert client.post("/api/ingest", headers=_auth(sales), json={
        "connector": "csv", "dataset_name": "x", "department": "Sales",
        "config": {"content": "a,b\n1,2\n"}}).status_code == 403
    assert client.get("/api/audit", headers=_auth(sales)).status_code == 403


def test_unauthenticated_is_rejected(client):
    assert client.get("/api/datasets").status_code == 401


def test_home_serves_web_app(client):
    r = client.get("/")
    assert r.status_code == 200
    assert "Decision" in r.text
