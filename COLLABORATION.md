# CodeSync — Week 1 Collaboration Guide

> This week is setup and planning only. No code is required.
> Each person has their own section below. Read ONLY your section and follow the steps.

---

## Team

| Name | Email | Role |
|------|-------|------|
| Chol Mach Kuol Chol | c.chol1@alustudent.com | Project Lead / Backend |
| Alier Akuang Alier Piel | a.piel@alustudent.com | ETL / Data Processing |
| Kuol Akech Riak Kuol | k.kuol@alustudent.com | Database / API |
| Abay Mulat Tessema | a.tessema@alustudent.com | Frontend / UI |

---

## Repo Link
```
https://github.com/Chol-Mach-Kuol/codesync-momo-analytics
```

---
---

# 👤 CHOL MACH — Project Lead

## Your tasks this week
1. Invite teammates to the repo
2. Create the architecture diagram and commit it
3. Create the Scrum board
4. Update the README with both links

---

### Step 1 — Invite teammates as collaborators
1. Go to `https://github.com/Chol-Mach-Kuol/codesync-momo-analytics`
2. Click **Settings** → **Collaborators** → **Add people**
3. Add each person one by one using their email:
   - `a.piel@alustudent.com`
   - `k.kuol@alustudent.com`
   - `a.tessema@alustudent.com`
4. Wait for them to accept — you will see a green tick next to their name when they do

---

### Step 2 — Create the architecture diagram
1. Go to [https://app.diagrams.net](https://app.diagrams.net)
2. Click **Create New Diagram** → select **Blank** → click **Create**
3. Build these boxes connected by arrows from top to bottom:

```
[ DATA SOURCE ]
data/raw/momo.xml
        ↓
[ DATA INGESTION LAYER ]
parse_xml.py — Extract + Validate Records
        ↓
[ TRANSFORMATION LAYER ]
clean_normalize.py — Amounts, Dates, Phone Numbers
        ↓
[ CLASSIFICATION LAYER ]
categorize.py — Send Money, Receive Money, Airtime, Bills, Withdrawal
        ↓
    ↙       ↘
[ ERROR HANDLING ]     [ DATA STORAGE ]
dead_letter/           db.sqlite3
etl.log                Transactions Table
                            ↓
                    ↙           ↘
          [ ANALYTICS ]     [ API LAYER ]
          KPIs               FastAPI
          Trends             /transactions
          Categories         /analytics
                    ↘           ↙
                [ PRESENTATION LAYER ]
                MoMo Dashboard
                HTML + CSS + JavaScript
                KPIs | Charts | Tables | Filters
```

4. Color each box:

| Box | Color to use |
|-----|-------------|
| Data Source | Blue `#2563EB` |
| Data Ingestion | Teal `#0D9488` |
| Transformation | Teal `#0D9488` |
| Classification | Purple `#7C3AED` |
| Data Storage | Green `#16A34A` |
| Error Handling | Orange `#EA580C` |
| Analytics | Navy `#0F172A` |
| API Layer | Blue `#2563EB` |
| Presentation | Navy `#0F172A` |

5. Export: click **File** → **Export As** → **PNG** → save as `architecture.png`

---

### Step 3 — Commit the diagram to the repo
Open your terminal and run:
```bash
cd /Users/ghz/codesync-momo-analytics

# Copy your exported PNG into the docs folder
cp ~/Downloads/architecture.png docs/architecture.png

git checkout main
git add docs/architecture.png
git commit -m "docs: add system architecture diagram"
git push origin main
```

---

### Step 4 — Create the Scrum board
1. Go to `https://github.com/Chol-Mach-Kuol/codesync-momo-analytics`
2. Click the **Projects** tab → **New project**
3. Select **Board** layout → name it `CodeSync Scrum Board` → click **Create**
4. Add 3 columns: **To Do**, **In Progress**, **Done**
5. Add these cards:

**To Do column — click + Add item for each:**
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

**In Progress column:**
- Architecture design
- Project structure
- Database schema

**Done column:**
- GitHub repository created
- Team members invited
- README created
- Scrum board created
- Initial architecture planned

---

### Step 5 — Update README with both links
1. Copy the Scrum board URL from your browser
2. Copy the diagrams.net share link: click **File** → **Share** → copy link
3. Open `README.md` and replace these two lines:

```
- **Scrum Board:** [Insert GitHub Projects / Trello / Jira Link]
- **Architecture Diagram:** [Insert diagrams.net Link]
```

With the actual URLs, then run:
```bash
cd /Users/ghz/codesync-momo-analytics
git add README.md
git commit -m "docs: add scrum board and architecture links"
git push origin main
```

---

### Your checklist
- [ ] All 3 teammates invited as collaborators
- [ ] `docs/architecture.png` committed to the repo
- [ ] Architecture diagram link added to README
- [ ] Scrum board created with To Do, In Progress, Done columns
- [ ] All tasks added to the board
- [ ] Scrum board link added to README
- [ ] GitHub repo link ready to submit on Canvas

---
---

# 👤 ALIER AKUANG — ETL / Data Processing

## Your tasks this week
1. Accept the GitHub invite
2. Clone the repo and set up your environment
3. Create your branch
4. Add your tasks to the Scrum board

---

### Step 1 — Accept the GitHub collaborator invite
1. Check your email at `a.piel@alustudent.com`
2. Look for an email from GitHub with subject: **"You've been invited to collaborate"**
3. Open it and click **Accept invitation**
4. You will be taken to the GitHub repo page

---

### Step 2 — Clone the repo
Open your terminal and run:
```bash
git clone https://github.com/Chol-Mach-Kuol/codesync-momo-analytics.git
cd codesync-momo-analytics
```

---

### Step 3 — Set up your environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
cp .env.example .env
```

---

### Step 4 — Create your branch
```bash
git checkout -b feature/etl-processing
git push origin feature/etl-processing
```

---

### Step 5 — Confirm everything is working
```bash
# You should see these folders
ls
# README.md  etl/  api/  web/  data/  tests/  scripts/  docs/
```

---

### Step 6 — Add your tasks to the Scrum board
1. Go to `https://github.com/Chol-Mach-Kuol/codesync-momo-analytics`
2. Click the **Projects** tab → open **CodeSync Scrum Board**
3. In the **To Do** column, confirm these tasks are there (Chol Mach adds them, you just verify):
   - Research MoMo XML structure
   - Implement XML parser
   - Implement data cleaning
   - Implement categorization rules
   - Write unit tests

> That is all for this week. Your code will be written in the coming weeks.

---

### Your checklist
- [ ] Accepted GitHub collaborator invite
- [ ] Cloned the repo successfully
- [ ] Virtual environment set up and dependencies installed
- [ ] Branch `feature/etl-processing` created and pushed
- [ ] Verified your tasks are on the Scrum board

---
---

# 👤 KUOL AKECH — Database / API

## Your tasks this week
1. Accept the GitHub invite
2. Clone the repo and set up your environment
3. Create your branch
4. Add your tasks to the Scrum board

---

### Step 1 — Accept the GitHub collaborator invite
1. Check your email at `k.kuol@alustudent.com`
2. Look for an email from GitHub with subject: **"You've been invited to collaborate"**
3. Open it and click **Accept invitation**
4. You will be taken to the GitHub repo page

---

### Step 2 — Clone the repo
Open your terminal and run:
```bash
git clone https://github.com/Chol-Mach-Kuol/codesync-momo-analytics.git
cd codesync-momo-analytics
```

---

### Step 3 — Set up your environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
cp .env.example .env
```

---

### Step 4 — Create your branch
```bash
git checkout -b feature/database-api
git push origin feature/database-api
```

---

### Step 5 — Confirm everything is working
```bash
# You should see these folders
ls
# README.md  etl/  api/  web/  data/  tests/  scripts/  docs/
```

---

### Step 6 — Add your tasks to the Scrum board
1. Go to `https://github.com/Chol-Mach-Kuol/codesync-momo-analytics`
2. Click the **Projects** tab → open **CodeSync Scrum Board**
3. In the **To Do** column, confirm these tasks are there (Chol Mach adds them, you just verify):
   - Define database schema
   - Implement database layer
   - Develop FastAPI endpoints

> That is all for this week. Your code will be written in the coming weeks.

---

### Your checklist
- [ ] Accepted GitHub collaborator invite
- [ ] Cloned the repo successfully
- [ ] Virtual environment set up and dependencies installed
- [ ] Branch `feature/database-api` created and pushed
- [ ] Verified your tasks are on the Scrum board

---
---

# 👤 ABAY MULAT — Frontend / UI

## Your tasks this week
1. Accept the GitHub invite
2. Clone the repo and set up your environment
3. Create your branch
4. Add your tasks to the Scrum board

---

### Step 1 — Accept the GitHub collaborator invite
1. Check your email at `a.tessema@alustudent.com`
2. Look for an email from GitHub with subject: **"You've been invited to collaborate"**
3. Open it and click **Accept invitation**
4. You will be taken to the GitHub repo page

---

### Step 2 — Clone the repo
Open your terminal and run:
```bash
git clone https://github.com/Chol-Mach-Kuol/codesync-momo-analytics.git
cd codesync-momo-analytics
```

---

### Step 3 — Set up your environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
cp .env.example .env
```

---

### Step 4 — Create your branch
```bash
git checkout -b feature/frontend-dashboard
git push origin feature/frontend-dashboard
```

---

### Step 5 — Confirm everything is working
```bash
# You should see these folders
ls
# README.md  etl/  api/  web/  data/  tests/  scripts/  docs/
```

---

### Step 6 — Add your tasks to the Scrum board
1. Go to `https://github.com/Chol-Mach-Kuol/codesync-momo-analytics`
2. Click the **Projects** tab → open **CodeSync Scrum Board**
3. In the **To Do** column, confirm these tasks are there (Chol Mach adds them, you just verify):
   - Design dashboard
   - Implement dashboard charts
   - Integrate frontend and backend

> That is all for this week. Your code will be written in the coming weeks.

---

### Your checklist
- [ ] Accepted GitHub collaborator invite
- [ ] Cloned the repo successfully
- [ ] Virtual environment set up and dependencies installed
- [ ] Branch `feature/frontend-dashboard` created and pushed
- [ ] Verified your tasks are on the Scrum board

---
---

## Expected Rubric Score

| Criterion | Points |
|-----------|--------|
| GitHub Repository Setup | 5/5 |
| Architecture Diagram | 5/5 |
| Scrum Board | 3/3 |
| **Total** | **13/13** |
