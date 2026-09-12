"""Demo users and example data.

``ensure_demo_users`` runs on startup so you can log in immediately. The demo
datasets are loaded on demand (the "Load demo data" button, or ``python -m
decision_os.seed``). Everything here is clearly-marked EXAMPLE data — replace it
by connecting your own sources.
"""
from __future__ import annotations

import sqlite3

from . import governance, semantic
from .db import connect, init_db

# username -> (password, role, department, display_name)
DEMO_USERS = {
    "admin":    ("admin123",   "admin",     "IT",         "Platform Admin"),
    "ceo":      ("ceo123",     "executive", "Executive",  "Chief Executive"),
    "sales1":   ("sales123",   "member",    "Sales",      "Sales Analyst"),
    "finance1": ("finance123", "member",    "Finance",    "Finance Analyst"),
}

# Example rows per department (CSV text -> ingested via the csv connector).
DEMO_DATASETS = {
    "Sales": (
        "opportunity,account,stage,amount_usd,close_quarter,risk\n"
        "Renewal - Northwind,Northwind Traders,Negotiation,120000,Q4,high churn risk flagged\n"
        "Expansion - Contoso,Contoso Ltd,Proposal,85000,Q4,expansion into EU region\n"
        "New logo - Fabrikam,Fabrikam Inc,Discovery,45000,Q1,long sales cycle expected\n"
        "Renewal - Tailspin,Tailspin Toys,Closed Won,60000,Q3,reference customer\n"
    ),
    "Finance": (
        "line_item,department,budget_usd,spent_usd,quarter,note\n"
        "Cloud infrastructure,Operations,200000,240000,Q4,over budget - review contracts\n"
        "Marketing campaigns,Marketing,150000,90000,Q4,underspent - reallocate\n"
        "Sales tooling,Sales,50000,52000,Q4,near budget\n"
        "Headcount - Engineering,Engineering,600000,580000,Q4,on track\n"
    ),
    "Operations": (
        "service,region,uptime_pct,incidents,sla_target_pct,note\n"
        "Order fulfilment,EU,98.9,3,99.5,below SLA - EU region churn risk\n"
        "Order fulfilment,US,99.7,1,99.5,healthy\n"
        "Customer support,EU,97.2,5,98.0,staffing shortfall\n"
        "Billing,Global,99.9,0,99.5,healthy\n"
    ),
}


def ensure_demo_users(conn: sqlite3.Connection) -> None:
    """Idempotent: create demo logins only if they don't already exist."""
    for username, (password, role, dept, name) in DEMO_USERS.items():
        if governance.get_user_by_username(conn, username) is None:
            governance.create_user(conn, username, password, role, dept, name)


def seed_demo_data(conn: sqlite3.Connection) -> list[dict]:
    """Load the example datasets (skips departments already loaded)."""
    existing = {d["department"] for d in semantic.list_datasets(conn)}
    results = []
    for department, csv_text in DEMO_DATASETS.items():
        if department in existing:
            continue
        results.append(
            semantic.ingest(
                conn,
                connector_name="csv",
                config={"content": csv_text},
                dataset_name=f"[EXAMPLE] {department} data",
                department=department,
            )
        )
    return results


def main() -> None:
    conn = connect()
    init_db(conn)
    ensure_demo_users(conn)
    loaded = seed_demo_data(conn)
    if loaded:
        for r in loaded:
            print(f"loaded {r['record_count']:>3} records into {r['name']}")
    else:
        print("demo data already present — nothing to load")
    print("demo users:", ", ".join(DEMO_USERS))


if __name__ == "__main__":
    main()
