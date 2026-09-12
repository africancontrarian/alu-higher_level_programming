#!/usr/bin/env bash
# One command to run Decision OS locally.
set -euo pipefail
cd "$(dirname "$0")"

python3 -m venv .venv 2>/dev/null || true
./.venv/bin/pip install -q -r requirements.txt
./.venv/bin/python -m decision_os.seed

echo ""
echo "Decision OS is starting at http://localhost:8000"
echo "Sign in with  admin / admin123  (see README for other demo logins)."
echo ""
exec ./.venv/bin/uvicorn decision_os.api:app --port 8000
