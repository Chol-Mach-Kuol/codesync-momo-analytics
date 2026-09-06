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
