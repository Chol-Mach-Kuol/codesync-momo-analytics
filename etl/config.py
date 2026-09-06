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
