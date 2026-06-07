"""Exporta el diagrama HTML a PNG con Playwright."""

from pathlib import Path

from playwright.sync_api import sync_playwright

HTML = Path(__file__).resolve().parent / "estructura_diagram.html"
OUTPUT = Path(__file__).resolve().parent.parent / "docs" / "Estructura Proyecto.png"


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1500, "height": 920}, device_scale_factor=2)
        page.goto(HTML.as_uri())
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(800)
        page.locator("#diagram").screenshot(path=str(OUTPUT), type="png")
        browser.close()
    print(f"Diagrama guardado en: {OUTPUT}")


if __name__ == "__main__":
    main()
