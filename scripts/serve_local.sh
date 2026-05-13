#!/usr/bin/env bash
set -euo pipefail
python -m http.server 8000 --directory docs
