#!/usr/bin/env bash
set -e
echo "Serving dashboard at http://localhost:8000"
python -m http.server 8000
