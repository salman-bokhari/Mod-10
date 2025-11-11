# tests/e2e/test_playwright_e2e.py
from playwright.sync_api import sync_playwright

def test_e2e_calculation():
    """
    Example Playwright E2E test — ensures the FastAPI app is reachable.
    You can expand this later to click buttons or test API calls.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000/")
        
        # Example validation — update as needed
        assert page.title() == "" or "Calculator" in page.content()

        browser.close()
