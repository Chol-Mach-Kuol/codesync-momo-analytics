#!/usr/bin/env bash
set -e
python etl/run.py --xml data/raw/momo.xml
echo "dashboard.json rebuilt at data/processed/dashboard.json"
