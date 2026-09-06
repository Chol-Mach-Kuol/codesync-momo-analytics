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
                   COUNT(*)      AS count,
                   SUM(amount)   AS total_amount
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
