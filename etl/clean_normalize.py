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
        "raw_id":  record.get("_id"),
        "date":    date,
        "amount":  amount,
        "phone":   phone,
        "body":    body,
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
