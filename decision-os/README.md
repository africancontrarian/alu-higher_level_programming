# Decision OS

**A sovereign, agnostic decision platform for the enterprise — v1.**

Decision OS plugs into an enterprise's existing data, unifies it across
departments, and turns a plain-language question into a **grounded, cited
decision** — with governance and audit built in. It runs entirely on your own
machine and, by default, makes **zero external network calls**: your data never
leaves the box.

This is the first working version (v1). It is intentionally a small, honest
foundation that implements every layer of the architecture end-to-end, so you
can run it, demo it, and hand it to a technical co-founder to extend.

---

## Run it (one command)

```bash
cd decision-os
./run.sh
```

Then open **http://localhost:8000** and sign in.

| Login | Password | Sees |
|-------|----------|------|
| `admin` | `admin123` | everything + can connect data + audit log |
| `ceo` | `ceo123` | **all departments** (cross-silo decisions) + audit log |
| `sales1` | `sales123` | **Sales only** |
| `finance1` | `finance123` | **Finance only** |

> These are demo logins — change them before any real use.

Click **Load demo data** (as `admin`) to load example Sales, Finance, and
Operations data, then ask something like *“Where are we over budget or at churn
risk this quarter?”* Sign in as `ceo` to see a cross-department answer; sign in
as `sales1` to see the same engine correctly scoped to one department.

### Run the tests

```bash
cd decision-os
./.venv/bin/pytest        # after run.sh has created the venv
# or:  python -m venv .venv && ./.venv/bin/pip install -r requirements.txt && ./.venv/bin/pytest
```

---

## The architecture (the six layers)

The code mirrors the plan's architecture — each layer is one module.

| Layer | Module | What it does | Build / Rent |
|------:|--------|--------------|--------------|
| **5 · Experience** | `api.py`, `web/index.html` | How each department asks and gets decisions | Build |
| **4 · Reasoning & agents** | `reasoning.py` | The decision engine + a **model-agnostic** provider interface | Build orchestration, rent the model |
| **3 · Semantic layer** | `semantic.py` | The "one brain": normalises every source into a searchable, unified store | Build |
| **2 · Connective tissue** | `connectors.py` | **Agnostic** plug-and-play: one interface per integration | Build |
| **1 · Governance & sovereignty** | `governance.py` | Auth, role-based access, audit trail | Build |
| **0 · Substrate** | `db.py`, `config.py` | Local, in-boundary storage & config | Rent (standard infra) |

**Why this proves the vision in miniature:** data flows *connector → unified
store → decision engine → answer*, every step is *governed* (who can see which
department) and *audited*, and it is *sovereign* (local + offline by default).
Nothing is hardcoded to a department, so the platform stays *horizontal*.

---

## How it stays *agnostic* (plug-and-play)

Adding a new data source is implementing **one method**:

```python
from decision_os.connectors import Connector, register_connector

class SalesforceConnector(Connector):
    name = "salesforce"
    def fetch(self, config):
        # ... call the Salesforce API, yield each record as a dict ...
        yield {"account": "...", "stage": "...", "amount": 1000}

register_connector(SalesforceConnector())
```

Nothing else in the platform changes. v1 ships `csv` (any export/spreadsheet)
and `sqlite` (any existing SQLite database) connectors.

## How it stays *model-agnostic*

The decision engine talks to a `ModelProvider` interface, never to a vendor.

- **`local`** (default) — deterministic, offline, no API keys. Grounds every
  answer in retrieved evidence and cites sources. **Nothing leaves the box.**
- **`external`** — a skeleton (`ExternalLLMProvider` in `reasoning.py`) where you
  drop in a real LLM (Anthropic, OpenAI, or a self-hosted open-weight model).
  It is **off by default** because enabling it is a deliberate sovereignty
  trade-off. Set `DECISION_OS_PROVIDER=external` once implemented.

---

## Configuration

All via environment variables (so it self-hosts anywhere without code changes):

| Variable | Default | Meaning |
|----------|---------|---------|
| `DECISION_OS_DB` | `decision_os.db` | Path to the local data store |
| `DECISION_OS_PROVIDER` | `local` | `local` (offline) or `external` (LLM) |
| `DECISION_OS_RETRIEVAL_LIMIT` | `6` | Evidence records fed to the engine per decision |

---

## Honest v1 boundaries (what to build next)

This is a foundation, not the finished platform. Deliberately **not yet** here:

- **Real intelligence** — the local provider is a transparent baseline; plug in
  an LLM via the provider interface for fluent reasoning.
- **Smarter retrieval** — keyword matching now; a vector index / knowledge graph
  slots into `semantic.py` behind the same `retrieve()` seam.
- **Production auth** — v1 uses simple session tokens; add SSO/OIDC and token
  expiry in `governance.py`.
- **More connectors** — CRM, ERP, warehouses, document stores.
- **Encryption at rest, secrets management, and a hardened deploy** for real
  in-VPC / on-prem installs.

Each maps to a phase in the execution plan: prove one decision deeply, then
generalise into the OS.

## Project layout

```
decision-os/
├── run.sh                 # one-command local run
├── requirements.txt
├── pyproject.toml
├── decision_os/
│   ├── config.py          # Layer 0
│   ├── db.py              # Layer 0
│   ├── governance.py      # Layer 1
│   ├── connectors.py      # Layer 2
│   ├── semantic.py        # Layer 3
│   ├── reasoning.py       # Layer 4
│   ├── api.py             # Layer 5
│   ├── seed.py            # demo users + example data
│   └── web/index.html     # Layer 5 (the app)
└── tests/
    ├── test_core.py       # layers 1–4, no server needed
    └── test_api.py        # end-to-end API
```
