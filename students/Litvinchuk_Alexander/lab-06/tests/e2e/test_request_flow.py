import os
import sys

from fastapi.testclient import TestClient

LAB05_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "lab-05")
)
sys.path.insert(0, LAB05_PATH)

from main import app


client = TestClient(app)


def test_request_flow():
    # 1. Создать сессию
    create_response = client.post(
        "/api/requests",
        json={
            "session_id": "e2e-1",
            "task_id": "task-1",
            "user_id": "user-1",
            "duration_minutes": 25,
            "status": "ACTIVE",
        },
    )

    assert create_response.status_code == 200
    assert create_response.json()["request_id"] == "e2e-1"

    # 2. Получить сессию
    get_response = client.get("/api/requests/e2e-1")

    assert get_response.status_code == 200
    data = get_response.json()
    assert data["session_id"] == "e2e-1"
    assert data["status"] == "ACTIVE"