# CodeSync — Team Collaboration Guide (Week 1)

> This week is about setup and planning only. No code is required.
> There are 3 things to complete before Monday 8am.

---

## Team

| Name | Email | Role | GitHub Branch |
|------|-------|------|---------------|
| Chol Mach Kuol Chol | c.chol1@alustudent.com | Project Lead / Backend | `feature/project-lead` |
| Alier Akuang Alier Piel | a.piel@alustudent.com | ETL / Data Processing | `feature/etl-processing` |
| Kuol Akech Riak Kuol | k.kuol@alustudent.com | Database / API | `feature/database-api` |
| Abay Mulat Tessema | a.tessema@alustudent.com | Frontend / UI | `feature/frontend-dashboard` |

---

## What Is Due — Monday 8am

| # | Task | Who | Status |
|---|------|-----|--------|
| 1 | GitHub repo created | Chol Mach | ✅ Done |
| 2 | All teammates invited as collaborators | Chol Mach | ⚠️ Pending |
| 3 | README has team name + all members | Chol Mach | ✅ Done |
| 4 | Architecture diagram created and committed as `docs/architecture.png` | All (Chol Mach commits) | ❌ Not done |
| 5 | Architecture diagram link added to README | Chol Mach | ❌ Not done |
| 6 | Scrum board created with To Do, In Progress, Done columns | All | ❌ Not done |
| 7 | At least 3 tasks added to Scrum board | All | ❌ Not done |
| 8 | Scrum board link added to README | Chol Mach | ❌ Not done |

---

## TASK 1 — GitHub Collaborators (Chol Mach)

1. Go to `https://github.com/Chol-Mach-Kuol/codesync-momo-analytics`
2. Click **Settings** → **Collaborators** → **Add people**
3. Invite each teammate by their email:
   - `a.piel@alustudent.com`
   - `k.kuol@alustudent.com`
   - `a.tessema@alustudent.com`
4. Each teammate accepts the invite from their email

---

## TASK 2 — Architecture Diagram (Everyone contributes, Chol Mach commits)

### Step 1 — Create the diagram
1. Go to [https://app.diagrams.net](https://app.diagrams.net)
2. Click **Create New Diagram** → choose **Blank**
3. Build the following layered architecture:

```
┌─────────────────────────────────┐
│          DATA SOURCE            │
│     data/raw/momo.xml           │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│      DATA INGESTION LAYER       │
│         parse_xml.py            │
│    Extract + Validate Records   │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│      TRANSFORMATION LAYER       │
│       clean_normalize.py        │
│  Amounts │ Dates │ Phone Numbers│
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│      CLASSIFICATION LAYER       │
│          categorize.py          │
│ Send │ Receive │ Airtime │ Bills│
└────────────────┬────────────────┘
                 │
        ┌────────┴────────┐
        ▼                 ▼
┌───────────────┐  ┌──────────────────┐
│ ERROR HANDLING│  │   DATA STORAGE   │
│ dead_letter/  │  │   db.sqlite3     │
│ etl.log       │  │   Transactions   │
└───────────────┘  └────────┬─────────┘
                            │
                   ┌────────┴────────┐
                   ▼                 ▼
         ┌──────────────┐  ┌──────────────────┐
         │  ANALYTICS   │  │    API LAYER     │
         │  KPIs        │  │    FastAPI       │
         │  Trends      │  │ /transactions    │
         │  Categories  │  │ /analytics       │
         └──────┬───────┘  └───────┬──────────┘
                │                  │
                └────────┬─────────┘
                         ▼
              ┌─────────────────────┐
              │  PRESENTATION LAYER │
              │   MoMo Dashboard    │
              │  HTML + CSS + JS    │
              │  KPIs │ Charts      │
              │  Tables │ Filters   │
              └─────────────────────┘
```

### Step 2 — Use these colors
| Layer | Color |
|-------|-------|
| Data Source | `#2563EB` (Blue) |
| Ingestion | `#0D9488` (Teal) |
| Transformation | `#0D9488` (Teal) |
| Classification | `#7C3AED` (Purple) |
| Database | `#16A34A` (Green) |
| Analytics | `#0F172A` (Navy) |
| API | `#2563EB` (Blue) |
| Dashboard | `#0F172A` (Navy) |
| Error Handling | `#EA580C` (Orange) |

### Step 3 — Export and commit (Chol Mach does this)
1. In diagrams.net click **File** → **Export As** → **PNG**
2. Save the file as `architecture.png`
3. Run these commands:

```bash
# Copy the exported file into the docs folder
cp /path/to/architecture.png /Users/ghz/codesync-momo-analytics/docs/architecture.png

# Commit and push
cd /Users/ghz/codesync-momo-analytics
git checkout main
git add docs/architecture.png
git commit -m "docs: add system architecture diagram"
git push origin main
```

### Step 4 — Update README
Replace this line in `README.md`:
```
- **Architecture Diagram:** [Insert diagrams.net Link]
```
With your actual diagrams.net share link.

---

## TASK 3 — Scrum Board (Everyone adds tasks, Chol Mach shares link)

### Step 1 — Create the board
1. Go to `https://github.com/Chol-Mach-Kuol/codesync-momo-analytics`
2. Click the **Projects** tab → **New project**
3. Choose **Board** layout
4. Name it: `CodeSync Scrum Board`

### Step 2 — Add these 3 columns
- `To Do`
- `In Progress`
- `Done`

### Step 3 — Add tasks to each column

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

### Step 4 — Copy the board URL and update README
Replace this line in `README.md`:
```
- **Scrum Board:** [Insert GitHub Projects / Trello / Jira Link]
```
With the actual board URL.

Then commit:
```bash
cd /Users/ghz/codesync-momo-analytics
git checkout main
git add README.md
git commit -m "docs: add scrum board and architecture links to README"
git push origin main
```

---

## Final Checklist Before Submitting Monday 8am

- [ ] GitHub repository exists at `https://github.com/Chol-Mach-Kuol/codesync-momo-analytics`
- [ ] All 3 teammates accepted collaborator invites
- [ ] README has team name **CodeSync**
- [ ] README has all 4 member names and emails
- [ ] `docs/architecture.png` exists in the repo
- [ ] Architecture diagram clearly shows data flow
- [ ] Architecture diagram link is in README
- [ ] Scrum board exists with To Do, In Progress, Done columns
- [ ] At least 3 tasks are on the board
- [ ] Scrum board link is in README
- [ ] GitHub repository link is ready to submit on Canvas

---

## Expected Score

| Criterion | Points |
|-----------|--------|
| GitHub Repository Setup | 5/5 |
| Architecture Diagram | 5/5 |
| Scrum Board | 3/3 |
| **Total** | **13/13** |

---

## Note on the Code Files

The empty files in `etl/`, `api/`, `web/`, and `tests/` are placeholders.
Each teammate will fill in their own files in the coming weeks through their own branch and Pull Request.
The code is **not required this week**.
