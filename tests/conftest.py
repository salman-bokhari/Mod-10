# tests/conftest.py
import pytest
import subprocess
import time
import os
import signal

@pytest.fixture(scope="session", autouse=True)
def start_fastapi_server():
    """
    Starts FastAPI app in background for e2e tests.
    Runs once per test session.
    """
    # Start the FastAPI app using uvicorn
    process = subprocess.Popen(
        ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    # Wait for server to start
    time.sleep(3)
    yield
    # Clean up: terminate process after tests complete
    os.kill(process.pid, signal.SIGTERM)
