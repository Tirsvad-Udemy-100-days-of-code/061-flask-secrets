"""@brief Capture the screenshot of one lecture step with a headless browser.

Runs inside the Docker container started by capture_screenshot.sh, never on the
host desktop. The step definitions live in screenshots.json.
"""

import json
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = Path("/out")
BASE_URL = "http://127.0.0.1:5000"
SERVER_CODE = "from flask_secrets.presentation.main import create_app;create_app().run(port=5000)"


def wait_for_server() -> None:
    """@brief Wait until the Flask server accepts connections."""
    import urllib.request

    for _ in range(50):
        try:
            urllib.request.urlopen(BASE_URL + "/", timeout=1)
            return
        except OSError:
            time.sleep(0.2)
    raise RuntimeError("server did not start")


def capture(step: dict[str, object]) -> None:
    """@brief Capture one step.

    @param step A step definition from screenshots.json.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 900, "height": 420})
        page.goto(BASE_URL + str(step["path"]))
        for action in step.get("actions", []):  # type: ignore[attr-defined]
            if "fill" in action:
                page.fill(action["fill"], action["value"])
            elif "click" in action:
                page.click(action["click"])
        page.screenshot(path=str(OUTPUT_DIR / f"{step['name']}.png"))
        browser.close()


def main() -> None:
    """@brief Capture the steps named on the command line."""
    steps = json.loads((ROOT / "screenshots.json").read_text(encoding="utf-8"))
    wanted = sys.argv[1:]
    server = subprocess.Popen([sys.executable, "-c", SERVER_CODE])
    try:
        wait_for_server()
        for step in steps:
            if step["name"] in wanted:
                capture(step)
    finally:
        server.terminate()


if __name__ == "__main__":
    main()
