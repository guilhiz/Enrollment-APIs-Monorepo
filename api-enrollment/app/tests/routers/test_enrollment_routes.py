from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_enrollment_status():
    response = client.get("/enrollments/12345678901")
    assert response.status_code == 404


def test_request_enrollment():
    response = client.post(
        "/enrollments", json={"name": "John Doe", "cpf": "12345678901", "age": 30, "enrollment_status": "active"}
    )
    assert response.status_code == 201
