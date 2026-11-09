#!/usr/bin/env bash
# Runs inside the Docker container: installs the project, starts the server and
# takes the screenshots. Started by capture_screenshot.sh.
set -euo pipefail
cp -r /repo /tmp/app
cd /tmp/app
rm -rf .venv framework
pip install -q .
python -c "from flask_secrets.presentation.main import create_app; create_app().run(port=5000)" &
server=$!
trap 'kill "$server"' EXIT
until python -c "import urllib.request as u; u.urlopen('http://127.0.0.1:5000/')" 2>/dev/null; do
  sleep 0.3
done
python scripts/capture_screenshot.py "$@"
