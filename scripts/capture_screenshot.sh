#!/usr/bin/env bash
# Capture the screenshots of the named lecture steps inside a Docker container
# (never on the host desktop, see framework/process/gui-testing.md).
# Usage: bash scripts/capture_screenshot.sh step-01-login-route [step-name ...]
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && { pwd -W 2>/dev/null || pwd; })"
export MSYS_NO_PATHCONV=1
docker build -q -t flask-secrets-screenshots -f "$root/scripts/Dockerfile.screenshots" "$root/scripts" >/dev/null
docker run --rm \
  -v "$root:/repo:ro" \
  -v "$root/docs/images:/out" \
  -e PYTHONDONTWRITEBYTECODE=1 \
  flask-secrets-screenshots \
  bash -c 'cp -r /repo /tmp/app && cd /tmp/app && rm -rf .venv framework && pip install -q . && python scripts/capture_screenshot.py "$@"' _ "$@"
