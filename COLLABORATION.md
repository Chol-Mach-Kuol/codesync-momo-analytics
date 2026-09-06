# MindForge — Team Collaboration Guide

> One document for all 4 members. Read your section, follow the steps in order, and never push directly to `main`.

---

## Team Assignments

| Name | Email | Role | Branch |
|------|-------|------|--------|
| Chol Mach Kuol Chol | c.chol1@alustudent.com | Project Lead / Backend | `feature/project-lead` |
| Alier Akuang Alier Piel | a.piel@alustudent.com | ETL / Data Processing | `feature/etl-processing` |
| Kuol Akech Riak Kuol | k.kuol@alustudent.com | Database / API | `feature/database-api` |
| Abay Mulat Tessema | a.tessema@alustudent.com | Frontend / UI | `feature/frontend-dashboard` |

---

## STEP 0 — Everyone Does This First (One Time Setup)

```bash
# 1. Clone the repository (replace with actual repo URL)
git clone https://github.com/<repo-url>/codesync-momo-analytics.git
cd codesync-momo-analytics

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy environment config
cp .env.example .env

# 5. Create your own branch (use YOUR branch name from the table above)
git checkout -b feature/your-branch-name
```

---

## DAILY WORKFLOW — Everyone Follows This Every Day

```bash
# Before starting work each day — pull latest changes from main
git pull origin main

# After finishing your work — save and push
git add .
git commit -m "feat: short description of what you did"
git push origin feature/your-branch-name

# Then go to GitHub → open a Pull Request → assign Chol Mach to review → merge
```

### Golden Rules
- NEVER push directly to `main`
- NEVER edit files that belong to another person
- ALWAYS pull from `main` before starting work
- ONE Pull Request per feature/task

---

---

# MEMBER 1 — Chol Mach Kuol Chol
## Role: Project Lead / Backend
## Branch: `feature/project-lead`
## Files: `scripts/`, `requirements.txt`, `.env.example`, `.gitignore`, `README.md`

---

### Your Steps

**Step 1** — Protect the main branch on GitHub
```
GitHub → Settings → Branches → Add branch protection rule
Branch name pattern: main
Check: Require a pull request before merging
Save changes
```

**Step 2** — Create your branch
```bash
git checkout -b feature/project-lead
```

**Step 3** — Your files are already written. Verify they exist:
```bash
ls scripts/
# Should show: run_etl.sh  export_json.sh  serve_frontend.sh
```

**Step 4** — Update the 3 placeholder links in README.md once you have them:
```
- GitHub Repository: replace [Insert GitHub Repository Link]
- Scrum Board:       replace [Insert GitHub Projects / Trello / Jira Link]
- Architecture:      replace [Insert diagrams.net Link]
```

**Step 5** — Commit and push
```bash
git add .
git commit -m "feat: add scripts and finalize README"
git push origin feature/project-lead
```

**Step 6** — Open Pull Request on GitHub → merge into `main`

---

### Your Files (already created — verify content)

**`requirements.txt`**
```
lxml>=4.9.0
python-dateutil>=2.8.2
fastapi>=0.110.0
uvicorn>=0.29.0
pydantic>=2.0.0
pytest>=8.0.0
python-dotenv>=1.0.0
```

**`.env.example`**
```
DATABASE_URL=sqlite:///data/db.sqlite3
XML_INPUT_PATH=data/raw/momo.xml
JSON_OUTPUT_PATH=data/processed/dashboard.json
```

**`.gitignore`**
```
data/raw/
data/db.sqlite3
data/logs/
.env
__pycache__/
*.pyc
*.pyo
.venv/
venv/
*.egg-info/
.pytest_cache/
```

**`scripts/run_etl.sh`**
```bash
#!/usr/bin/env bash
set -e
python etl/run.py --xml data/raw/momo.xml
```

**`scripts/export_json.sh`**
```bash
#!/usr/bin/env bash
set -e
python etl/run.py --xml data/raw/momo.xml
echo "dashboard.json rebuilt at data/processed/dashboard.json"
```

**`scripts/serve_frontend.sh`**
```bash
#!/usr/bin/env bash
set -e
echo "Serving dashboard at http://localhost:8000"
python -m http.server 8000
```

---

### Your Responsibilities as Lead
- Review and merge all Pull Requests from teammates
- Make sure the project runs end-to-end after all branches are merged
- Run the full test suite before final submission:
```bash
pytest tests/
```

---
---

# MEMBER 2 — Alier Akuang Alier Piel
## Role: ETL / Data Processing
## Branch: `feature/etl-processing`
## Files: `etl/config.py`, `etl/parse_xml.py`, `etl/clean_normalize.py`, `etl/categorize.py`, `etl/run.py`, `etl/__init__.py`, `tests/test_parse_xml.py`, `tests/test_clean_normalize.py`, `tests/test_categorize.py`

---

### Your Steps

**Step 1** — Clone and set up (see STEP 0 above)

**Step 2** — Create your branch
```bash
git checkout -b feature/etl-processing
```

**Step 3** — Create the file `etl/__init__.py` (empty file)
```bash
touch etl/__init__.py
```

**Step 4** — Create each file below exactly as written

**Step 5** — Test your code
```bash
pytest tests/test_parse_xml.py
pytest tests/test_clean_normalize.py
pytest tests/test_categorize.py
```

**Step 6** — Commit and push
```bash
git add .
git commit -m "feat: implement ETL pipeline - parse, clean, categorize"
git push origin feature/etl-processing
```

**Step 7** — Go to GitHub → open Pull Request → assign Chol Mach to review

---

### Your Files

**`etl/__init__.py`** — leave empty

---

**`etl/config.py`**
```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

XML_INPUT   = os.path.join(BASE_DIR, "data", "raw", "momo.xml")
DB_PATH     = os.path.join(BASE_DIR, "data", "db.sqlite3")
JSON_OUTPUT = os.path.join(BASE_DIR, "data", "processed", "dashboard.json")
ETL_LOG     = os.path.join(BASE_DIR, "data", "logs", "etl.log")
DEAD_LETTER = os.path.join(BASE_DIR, "data", "logs", "dead_letter")

CATEGORIES = [
    "Send Money",
    "Receive Money",
    "Airtime",
    "Bill Payment",
    "Cash Withdrawal",
    "Cash Deposit",
    "Other",
]
```

---

**`etl/parse_xml.py`**
```python
import xml.etree.ElementTree as ET
import logging

logger = logging.getLogger(__name__)


def parse_xml(xml_path: str) -> list[dict]:
    """Parse MoMo XML file and return a list of raw transaction dicts."""
    tree = ET.parse(xml_path)
    root = tree.getroot()
    records = []
    for sms in root.findall("sms"):
        records.append(sms.attrib)
    logger.info(f"Parsed {len(records)} records from {xml_path}")
    return records
```

---

**`etl/clean_normalize.py`**
```python
import re
import logging
from dateutil import parser as date_parser

logger = logging.getLogger(__name__)


def clean_amount(raw: str) -> float | None:
    if not raw:
        return None
    cleaned = re.sub(r"[^\d.]", "", raw)
    return float(cleaned) if cleaned else None


def clean_phone(raw: str) -> str | None:
    if not raw:
        return None
    digits = re.sub(r"\D", "", raw)
    return digits if len(digits) >= 9 else None


def clean_date(raw: str) -> str | None:
    if not raw:
        return None
    try:
        return date_parser.parse(raw).isoformat()
    except (ValueError, OverflowError):
        return None


def clean_record(record: dict) -> dict | None:
    """Return a cleaned record or None if the record is invalid."""
    amount = clean_amount(record.get("amount", ""))
    date   = clean_date(record.get("date", ""))
    phone  = clean_phone(record.get("address", ""))
    body   = record.get("body", "").strip()

    if not body:
        logger.warning(f"Dropping record with empty body: {record}")
        return None

    return {
        "raw_id": record.get("_id"),
        "date":   date,
        "amount": amount,
        "phone":  phone,
        "body":   body,
    }


def clean_records(records: list[dict]) -> tuple[list[dict], list[dict]]:
    """Return (clean_records, dead_letters)."""
    clean, dead = [], []
    for r in records:
        result = clean_record(r)
        if result:
            clean.append(result)
        else:
            dead.append(r)
    logger.info(f"Cleaned: {len(clean)} valid, {len(dead)} dead-letter")
    return clean, dead
```

---

**`etl/categorize.py`**
```python
RULES = [
    ("Send Money",      ["sent", "you have transferred", "payment to"]),
    ("Receive Money",   ["received", "you have received"]),
    ("Airtime",         ["airtime", "recharge"]),
    ("Bill Payment",    ["bill", "payment of", "electricity", "water"]),
    ("Cash Withdrawal", ["withdrawn", "cash out", "agent"]),
    ("Cash Deposit",    ["deposited", "cash in"]),
]


def categorize(body: str) -> str:
    lower = body.lower()
    for category, keywords in RULES:
        if any(kw in lower for kw in keywords):
            return category
    return "Other"


def categorize_records(records: list[dict]) -> list[dict]:
    for r in records:
        r["category"] = categorize(r.get("body", ""))
    return records
```

---

**`etl/run.py`**
```python
"""
Usage: python etl/run.py --xml data/raw/momo.xml
"""
import argparse
import json
import logging
import os
from collections import Counter

from etl.config import DB_PATH, JSON_OUTPUT, ETL_LOG, DEAD_LETTER
from etl.parse_xml import parse_xml
from etl.clean_normalize import clean_records
from etl.categorize import categorize_records
from etl.load_db import load

os.makedirs(os.path.dirname(ETL_LOG), exist_ok=True)
os.makedirs(DEAD_LETTER, exist_ok=True)
os.makedirs(os.path.dirname(JSON_OUTPUT), exist_ok=True)

logging.basicConfig(
    filename=ETL_LOG,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def export_json(records: list[dict]) -> None:
    counts = Counter(r["category"] for r in records)
    amounts = [r["amount"] for r in records if r["amount"]]
    dashboard = {
        "kpis": {
            "Total Transactions": len(records),
            "Total Amount": f"{sum(amounts):,.0f}",
            "Avg Amount": f"{sum(amounts)/len(amounts):,.0f}" if amounts else "0",
        },
        "categories": [{"name": k, "count": v} for k, v in counts.items()],
    }
    with open(JSON_OUTPUT, "w") as f:
        json.dump(dashboard, f, indent=2)


def run(xml_path: str) -> None:
    raw = parse_xml(xml_path)
    clean, dead = clean_records(raw)

    for i, d in enumerate(dead):
        with open(os.path.join(DEAD_LETTER, f"dead_{i}.xml"), "w") as f:
            f.write(str(d))

    categorized = categorize_records(clean)
    load(categorized, DB_PATH)
    export_json(categorized)
    print(f"Done. {len(categorized)} records loaded. {len(dead)} dead-letter.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--xml", required=True)
    args = parser.parse_args()
    run(args.xml)
```

---

**`tests/test_parse_xml.py`**
```python
import pytest
from etl.parse_xml import parse_xml

SAMPLE_XML = """<?xml version="1.0"?>
<smses>
  <sms _id="1" address="+250788000001" date="2024-01-01" body="You have received 5,000 RWF" />
  <sms _id="2" address="+250788000002" date="2024-01-02" body="You have transferred 2,000 RWF" />
</smses>"""


@pytest.fixture
def xml_file(tmp_path):
    f = tmp_path / "test.xml"
    f.write_text(SAMPLE_XML)
    return str(f)


def test_parse_returns_list(xml_file):
    records = parse_xml(xml_file)
    assert isinstance(records, list)


def test_parse_count(xml_file):
    records = parse_xml(xml_file)
    assert len(records) == 2


def test_parse_fields(xml_file):
    records = parse_xml(xml_file)
    assert records[0]["_id"] == "1"
    assert "body" in records[0]
```

---

**`tests/test_clean_normalize.py`**
```python
from etl.clean_normalize import clean_amount, clean_phone, clean_date, clean_record


def test_clean_amount_strips_commas():
    assert clean_amount("5,000 RWF") == 5000.0


def test_clean_amount_none():
    assert clean_amount("") is None


def test_clean_phone_valid():
    assert clean_phone("+250788000001") == "250788000001"


def test_clean_phone_short():
    assert clean_phone("123") is None


def test_clean_date_iso():
    result = clean_date("Jan 1, 2024 10:00:00")
    assert result.startswith("2024-01-01")


def test_clean_record_drops_empty_body():
    assert clean_record({"body": "", "amount": "100", "date": "2024-01-01"}) is None


def test_clean_record_valid():
    r = clean_record({"_id": "1", "body": "received 500", "amount": "500",
                      "date": "2024-01-01", "address": "+250788000001"})
    assert r is not None
    assert r["amount"] == 500.0
```

---

**`tests/test_categorize.py`**
```python
from etl.categorize import categorize


def test_receive_money():
    assert categorize("You have received 5,000 RWF from 0788000001") == "Receive Money"


def test_send_money():
    assert categorize("You have transferred 2,000 RWF to 0788000002") == "Send Money"


def test_airtime():
    assert categorize("Your airtime recharge of 500 RWF was successful") == "Airtime"


def test_bill_payment():
    assert categorize("Bill payment of 10,000 RWF completed") == "Bill Payment"


def test_cash_withdrawal():
    assert categorize("You have withdrawn 20,000 RWF from agent") == "Cash Withdrawal"


def test_other():
    assert categorize("Some unrecognized message") == "Other"
```

---
---

# MEMBER 3 — Kuol Akech Riak Kuol
## Role: Database / API
## Branch: `feature/database-api`
## Files: `etl/load_db.py`, `api/__init__.py`, `api/db.py`, `api/schemas.py`, `api/app.py`

---

### Your Steps

**Step 1** — Clone and set up (see STEP 0 above)

**Step 2** — Create your branch
```bash
git checkout -b feature/database-api
```

**Step 3** — Wait for Alier to merge `feature/etl-processing` into `main` first, then pull:
```bash
git pull origin main
```
> This is important because your `load_db.py` imports from `etl/config.py` which Alier owns.

**Step 4** — Create each file below exactly as written

**Step 5** — Test your API
```bash
uvicorn api.app:app --reload
# Open http://localhost:8000/docs in your browser
# You should see all 4 endpoints listed
```

**Step 6** — Commit and push
```bash
git add .
git commit -m "feat: implement SQLite database layer and FastAPI endpoints"
git push origin feature/database-api
```

**Step 7** — Go to GitHub → open Pull Request → assign Chol Mach to review

---

### Your Files

**`api/__init__.py`** — leave empty
```bash
touch api/__init__.py
```

---

**`etl/load_db.py`**
```python
import sqlite3
import logging
from etl.config import DB_PATH

logger = logging.getLogger(__name__)

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS transactions (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    raw_id   TEXT UNIQUE,
    date     TEXT,
    amount   REAL,
    phone    TEXT,
    body     TEXT,
    category TEXT
);
"""

UPSERT = """
INSERT INTO transactions (raw_id, date, amount, phone, body, category)
VALUES (:raw_id, :date, :amount, :phone, :body, :category)
ON CONFLICT(raw_id) DO UPDATE SET
    date=excluded.date, amount=excluded.amount,
    phone=excluded.phone, body=excluded.body, category=excluded.category;
"""


def load(records: list[dict], db_path: str = DB_PATH) -> None:
    with sqlite3.connect(db_path) as conn:
        conn.execute(CREATE_TABLE)
        conn.executemany(UPSERT, records)
        conn.commit()
    logger.info(f"Loaded {len(records)} records into {db_path}")
```

---

**`api/db.py`**
```python
import sqlite3
from etl.config import DB_PATH


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
```

---

**`api/schemas.py`**
```python
from pydantic import BaseModel


class Transaction(BaseModel):
    id: int
    raw_id: str | None
    date: str | None
    amount: float | None
    phone: str | None
    category: str | None


class CategorySummary(BaseModel):
    category: str
    count: int
    total_amount: float
```

---

**`api/app.py`**
```python
from fastapi import FastAPI, HTTPException
from api.db import get_connection
from api.schemas import Transaction, CategorySummary

app = FastAPI(title="MoMo Analytics API")


@app.get("/transactions", response_model=list[Transaction])
def list_transactions(limit: int = 100, offset: int = 0):
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM transactions LIMIT ? OFFSET ?", (limit, offset)
        ).fetchall()
    return [dict(r) for r in rows]


@app.get("/transactions/{tx_id}", response_model=Transaction)
def get_transaction(tx_id: int):
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM transactions WHERE id = ?", (tx_id,)
        ).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return dict(row)


@app.get("/analytics", response_model=list[CategorySummary])
def analytics():
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT category,
                   COUNT(*)    AS count,
                   SUM(amount) AS total_amount
            FROM transactions
            GROUP BY category
        """).fetchall()
    return [dict(r) for r in rows]


@app.get("/categories")
def categories():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT DISTINCT category FROM transactions"
        ).fetchall()
    return [r["category"] for r in rows]
```

---

### How to run the API
```bash
# From the project root with venv active
uvicorn api.app:app --reload

# Interactive API docs
http://localhost:8000/docs

# Available endpoints
GET http://localhost:8000/transactions
GET http://localhost:8000/transactions/1
GET http://localhost:8000/analytics
GET http://localhost:8000/categories
```

---
---

# MEMBER 4 — Abay Mulat Tessema
## Role: Frontend / UI
## Branch: `feature/frontend-dashboard`
## Files: `index.html`, `web/styles.css`, `web/chart_handler.js`

---

### Your Steps

**Step 1** — Clone and set up (see STEP 0 above)

**Step 2** — Create your branch
```bash
git checkout -b feature/frontend-dashboard
```

**Step 3** — Create each file below exactly as written

**Step 4** — To preview your dashboard locally, you need a sample `dashboard.json`.
Create this temporary file at `data/processed/dashboard.json` for testing:
```json
{
  "kpis": {
    "Total Transactions": 1500,
    "Total Amount": "4,250,000",
    "Avg Amount": "2,833"
  },
  "categories": [
    { "name": "Send Money",      "count": 420 },
    { "name": "Receive Money",   "count": 380 },
    { "name": "Airtime",         "count": 310 },
    { "name": "Bill Payment",    "count": 200 },
    { "name": "Cash Withdrawal", "count": 150 },
    { "name": "Cash Deposit",    "count": 40  }
  ]
}
```

**Step 5** — Serve and preview
```bash
# From the project root
python -m http.server 8000
# Open http://localhost:8000 in your browser
```

**Step 6** — Commit and push
```bash
git add .
git commit -m "feat: implement dashboard UI with KPI cards and category chart"
git push origin feature/frontend-dashboard
```

**Step 7** — Go to GitHub → open Pull Request → assign Chol Mach to review

---

### Your Files

**`index.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MoMo Analytics Dashboard</title>
  <link rel="stylesheet" href="web/styles.css" />
</head>
<body>
  <header>
    <h1>MoMo Analytics Dashboard</h1>
  </header>

  <main>
    <section id="kpis"></section>
    <section id="charts"></section>
    <section id="transactions"></section>
  </main>

  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="web/chart_handler.js"></script>
</body>
</html>
```

---

**`web/styles.css`**
```css
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: system-ui, sans-serif;
  background: #f8fafc;
  color: #1e293b;
}

header {
  background: #2563eb;
  color: white;
  padding: 1rem 2rem;
}

main {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1rem;
  display: grid;
  gap: 2rem;
}

#kpis {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.kpi-card {
  background: white;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.kpi-card h3 { font-size: 0.85rem; color: #64748b; margin-bottom: 0.5rem; }
.kpi-card p  { font-size: 1.75rem; font-weight: 700; color: #2563eb; }

canvas { background: white; border-radius: 8px; padding: 1rem; }
```

---

**`web/chart_handler.js`**
```javascript
const DATA_URL = "data/processed/dashboard.json";

async function loadDashboard() {
  const res = await fetch(DATA_URL);
  const data = await res.json();
  renderKPIs(data.kpis);
  renderCategoryChart(data.categories);
}

function renderKPIs(kpis) {
  const section = document.getElementById("kpis");
  section.innerHTML = Object.entries(kpis)
    .map(([label, value]) => `
      <div class="kpi-card">
        <h3>${label}</h3>
        <p>${value}</p>
      </div>`)
    .join("");
}

function renderCategoryChart(categories) {
  const canvas = document.createElement("canvas");
  document.getElementById("charts").appendChild(canvas);
  new Chart(canvas, {
    type: "doughnut",
    data: {
      labels: categories.map(c => c.name),
      datasets: [{
        data: categories.map(c => c.count),
        backgroundColor: [
          "#2563eb", "#0d9488", "#7c3aed",
          "#16a34a", "#ea580c", "#0f172a"
        ]
      }]
    },
    options: {
      plugins: {
        legend: { position: "bottom" }
      }
    }
  });
}

loadDashboard();
```

---
---

# MERGE ORDER — Chol Mach Follows This

Merge Pull Requests in this exact order to avoid dependency errors:

```
1. feature/project-lead        (Chol Mach)   — no dependencies
2. feature/etl-processing      (Alier)        — no dependencies
3. feature/database-api        (Kuol)         — depends on etl/config.py from step 2
4. feature/frontend-dashboard  (Abay)         — no code dependencies, can go anytime
```

After all 4 are merged, run the full pipeline to verify everything works:
```bash
git pull origin main
source venv/bin/activate
bash scripts/run_etl.sh
bash scripts/serve_frontend.sh
# Open http://localhost:8000
```

---

# TROUBLESHOOTING

**Problem: `ModuleNotFoundError: No module named 'etl'`**
```bash
# Always run Python from the project root, not from inside a subfolder
cd codesync-momo-analytics
python etl/run.py --xml data/raw/momo.xml   # correct
```

**Problem: merge conflict**
```bash
git pull origin main
# Git will mark conflicts in the file with <<<< ==== >>>>
# Open the file, keep the correct version, delete the markers
git add <conflicted-file>
git commit -m "fix: resolve merge conflict"
```

**Problem: accidentally pushed to main**
```bash
# Tell Chol Mach immediately — he can revert it from GitHub
```

**Problem: tests failing**
```bash
# Run tests from the project root
cd codesync-momo-analytics
pytest tests/
```
