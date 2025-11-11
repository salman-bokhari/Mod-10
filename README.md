# FastAPI Calculator & User Management

A FastAPI application combining a simple calculator and secure user registration with hashed passwords and Pydantic validation. Uses PostgreSQL as the backend and includes unit, integration, and end-to-end tests.

---

## Requirements

- Python 3.12
- Docker & Docker Compose
- PostgreSQL (or via Docker)
- Playwright for e2e tests

---

## Setup & Run Locally

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/fastapi-calculator.git
cd fastapi-calculator
```

2. Create a .env file with:

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/fastapi_db
PGADMIN_EMAIL=admin@example.com
PGADMIN_PASSWORD=admin
``` 

3. Start the services
```
docker-compose up --build
```

4. Access:
```
FastAPI Calculator: http://localhost:8000
pgAdmin: http://localhost:5050
```


## Run Tests Locally

1. Activate virtual environment:
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

2. Install dependencies and Playwright:
```
pip install -r requirements.txt
python -m playwright install chromium
```

3. Run all tests:
```
pytest -q
```

4. Run only end-to-end tests:
```
pytest -q tests/e2e -k playwright_e2e
```