import os
import pytest
from fastapi.testclient import TestClient
from main import app
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/fastapi_db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_user_success():
    resp = client.post("/users", json={
        "username": "alice",
        "email": "alice@example.com",
        "password": "password123"
    })
    assert resp.status_code == 201
    assert resp.json()["username"] == "alice"

def test_create_user_duplicate():
    client.post("/users", json={"username":"bob","email":"bob@example.com","password":"pass123"})
    resp = client.post("/users", json={"username":"bob","email":"bob@example.com","password":"pass123"})
    assert resp.status_code == 400
