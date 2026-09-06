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
