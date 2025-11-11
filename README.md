# FastAPI Calculator

This repository contains a simple FastAPI-based calculator with unit, integration, and Playwright end-to-end tests, plus a GitHub Actions workflow to run tests on push.

## Run locally
1. Create virtualenv, install requirements: `pip install -r requirements.txt`
2. Install playwright browsers: `python -m playwright install`
3. Start the app: `uvicorn main:app --reload --host 127.0.0.1 --port 8000`
4. Open http://127.0.0.1:8000 in the browser

## Tests
- Unit tests: `pytest tests/test_operations_unit.py`
- Integration tests: `pytest tests/test_integration_api.py`
- E2E Playwright tests: start server then `pytest tests/e2e`

