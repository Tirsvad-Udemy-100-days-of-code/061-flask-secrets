"""@brief Capture the screenshot of one lecture step with a headless browser.

Runs inside the Docker container started by capture_screenshot.sh, never on the
host desktop, against a server that capture_in_container.sh has already started.
The step definitions live in screenshots.json.
"""

import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = Path("/out")
BASE_URL = "http://127.0.0.1:5000"


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
    for step in steps:
        if step["name"] in sys.argv[1:]:
            capture(step)


if __name__ == "__main__":
    main()
