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
