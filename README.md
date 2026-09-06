# MoMo Analytics Platform

## Team

**Team Name:** MindForge

## Project Description

MoMo Analytics Platform is an enterprise-level fullstack application designed to process Mobile Money (MoMo) SMS transaction data provided in XML format.

The system extracts transaction data from XML files, cleans and normalizes the records, categorizes transactions, stores the structured data in a relational SQLite database, and presents useful insights through an interactive web dashboard.

The platform is built around a modular ETL architecture that separates data ingestion, transformation, classification, storage, analytics, API services, and frontend presentation into distinct layers.

## Team Members

| Name | Email | Role |
|------|-------|------|
| Chol Mach Kuol Chol | c.chol1@alustudent.com | Project Lead / Backend |
| Alier Akuang Alier Piel | a.piel@alustudent.com | ETL / Data Processing |
| Kuol Akech Riak Kuol | k.kuol@alustudent.com | Database / API |
| Abay Mulat Tessema | a.tessema@alustudent.com | Frontend / UI |

---

## Links

- **GitHub Repository:** [Insert GitHub Repository Link]
- **Scrum Board:** [Insert GitHub Projects / Trello / Jira Link]
- **Architecture Diagram:** [Insert diagrams.net Link]

---

## System Architecture

The system follows a layered ETL and fullstack architecture:

```
MoMo XML → Data Ingestion → Cleaning & Normalization → Categorization → Database → Analytics/API → Dashboard
```

The architecture diagram is committed at [`docs/architecture.png`](docs/architecture.png).

### Architecture Layers

1. **Data Source** — MoMo XML transactions (`data/raw/momo.xml`)
2. **Data Ingestion** — XML parser extracts and validates records (`etl/parse_xml.py`)
3. **Transformation** — Cleans amounts, dates, phone numbers, missing values (`etl/clean_normalize.py`)
4. **Classification** — Categorizes transactions by type (`etl/categorize.py`)
5. **Data Storage** — SQLite relational database (`data/db.sqlite3`)
6. **Analytics & API** — KPIs, trends, FastAPI endpoints (`api/app.py`)
7. **Presentation** — Interactive web dashboard (`index.html`, `web/`)

### Error Handling

Invalid records are routed to `data/logs/dead_letter/`. All ETL activity is logged to `data/logs/etl.log`.

---

## Project Structure

```
momo-analytics/
├── README.md
├── .env.example
├── requirements.txt
├── index.html
├── web/
│   ├── styles.css
│   ├── chart_handler.js
│   └── assets/
├── data/
│   ├── raw/                        # git-ignored
│   ├── processed/
│   │   └── dashboard.json
│   ├── logs/
│   │   ├── etl.log
│   │   └── dead_letter/
│   └── db.sqlite3
├── etl/
│   ├── __init__.py
│   ├── config.py
│   ├── parse_xml.py
│   ├── clean_normalize.py
│   ├── categorize.py
│   ├── load_db.py
│   └── run.py
├── api/
│   ├── __init__.py
│   ├── app.py
│   ├── db.py
│   └── schemas.py
├── scripts/
│   ├── run_etl.sh
│   ├── export_json.sh
│   └── serve_frontend.sh
├── tests/
│   ├── test_parse_xml.py
│   ├── test_clean_normalize.py
│   └── test_categorize.py
└── docs/
    └── architecture.png
```

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Data Processing | Python |
| XML Processing | ElementTree / lxml |
| Database | SQLite |
| Backend API | FastAPI |
| API Validation | Pydantic |
| Frontend | HTML, CSS, JavaScript |
| Data Visualization | Chart.js |
| Testing | Pytest |
| Version Control | Git / GitHub |

---

## ETL Pipeline

```
XML File → Parse → Validate → Clean → Normalize → Categorize → Store in DB → Generate Analytics → Expose via API → Display on Dashboard
```

---

## Getting Started

```bash
# 1. Clone the repository
git clone <repo-url>
cd momo-analytics

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy environment config
cp .env.example .env

# 5. Place your MoMo XML file
cp /path/to/momo.xml data/raw/momo.xml

# 6. Run the ETL pipeline
bash scripts/run_etl.sh

# 7. Serve the dashboard
bash scripts/serve_frontend.sh
```

---

## Scrum Board

**Project Board:** [Insert Scrum Board Link]

### Current Sprint

**To Do**
- Research MoMo XML structure
- Define database schema
- Implement XML parser
- Implement data cleaning
- Implement categorization rules
- Implement database layer
- Develop FastAPI endpoints
- Design dashboard
- Implement dashboard charts
- Write unit tests
- Integrate frontend and backend
- Test complete ETL pipeline
- Prepare final documentation

**In Progress**
- Architecture design
- Project structure
- Database schema

**Done**
- GitHub repository created
- Team members invited
- README created
- Scrum board created
- Initial architecture planned

---

## Development Workflow

```
Create Issue → Feature Branch → Implement → Test → Commit → Push → Pull Request → Code Review → Merge
```
