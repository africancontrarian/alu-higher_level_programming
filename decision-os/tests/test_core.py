"""Core-layer tests — no web server required (standard library only)."""
import pytest

from decision_os import governance, semantic
from decision_os.db import connect, init_db
from decision_os.reasoning import DecisionEngine, LocalProvider

SALES_CSV = (
    "account,stage,note\n"
    "Northwind,Negotiation,high churn risk flagged\n"
    "Contoso,Proposal,expansion opportunity\n"
    "Fabrikam,Discovery,healthy pipeline\n"
)
FINANCE_CSV = (
    "line_item,budget,spent,note\n"
    "Cloud,200000,240000,over budget\n"
    "Marketing,150000,90000,underspent\n"
)


@pytest.fixture
def conn(tmp_path):
    c = connect(str(tmp_path / "core.db"))
    init_db(c)
    governance.create_user(c, "ceo", "pw", "executive", "Executive", "Chief")
    governance.create_user(c, "sales1", "pw", "member", "Sales", "Sales Analyst")
    semantic.ingest(c, "csv", {"content": SALES_CSV}, "Sales data", "Sales")
    semantic.ingest(c, "csv", {"content": FINANCE_CSV}, "Finance data", "Finance")
    yield c
    c.close()


def test_password_hashing_roundtrip():
    h, salt = governance.hash_password("secret")
    assert governance.verify_password("secret", salt, h)
    assert not governance.verify_password("wrong", salt, h)


def test_ingest_counts_records(conn):
    datasets = {d["name"]: d for d in semantic.list_datasets(conn)}
    assert datasets["Sales data"]["record_count"] == 3
    assert datasets["Finance data"]["record_count"] == 2


def test_retrieval_ranks_relevant_record_first(conn):
    hits = semantic.retrieve(conn, "which account has churn risk", ["Sales", "Finance"])
    assert hits, "expected at least one hit"
    assert "churn" in hits[0]["text"].lower()
    assert hits[0]["score"] >= 1


def test_rbac_scopes_departments(conn):
    ceo = governance.get_user_by_username(conn, "ceo")
    sales = governance.get_user_by_username(conn, "sales1")
    assert set(governance.accessible_departments(conn, ceo)) == {"Sales", "Finance"}
    assert governance.accessible_departments(conn, sales) == ["Sales"]


def test_executive_decision_spans_departments(conn):
    ceo = governance.get_user_by_username(conn, "ceo")
    brief = DecisionEngine(conn, LocalProvider()).decide(ceo, "budget and churn risks")
    assert brief["citations"], "executive brief should cite evidence"
    assert brief["confidence"] > 0
    # cross-silo: evidence can come from more than one department
    assert set(brief["departments_considered"]) <= {"Sales", "Finance"}


def test_member_decision_is_scoped_to_own_department(conn):
    sales = governance.get_user_by_username(conn, "sales1")
    brief = DecisionEngine(conn, LocalProvider()).decide(sales, "over budget items")
    # A Sales member must never see Finance records, even when asking about them.
    assert all(c["department"] == "Sales" for c in brief["citations"])


def test_decision_is_audited(conn):
    ceo = governance.get_user_by_username(conn, "ceo")
    DecisionEngine(conn, LocalProvider()).decide(ceo, "anything")
    actions = [row["action"] for row in governance.get_audit(conn)]
    assert "decision" in actions
