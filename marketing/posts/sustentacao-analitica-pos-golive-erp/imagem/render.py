from playwright.sync_api import sync_playwright
import pathlib

html_path = pathlib.Path(__file__).parent / "featured.html"
out_path = pathlib.Path(__file__).parent / "sustentacao-analitica-sap-featured.png"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 628})
    page.goto(html_path.resolve().as_uri())
    page.wait_for_timeout(500)
    page.screenshot(path=str(out_path))
    browser.close()

print("saved:", out_path)
