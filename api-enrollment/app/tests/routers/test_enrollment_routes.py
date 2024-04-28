from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_enrollment_status_successful():
    response_success = client.get("/enrollments/12345678901")
    assert response_success.status_code == 200

def test_get_enrollment_status_not_found():
    response_not_found = client.get("/enrollments/12345678922")
    assert response_not_found.status_code == 404

def test_request_enrollment_successful():
    response_success = client.post(
        "/enrollments", json={"name": "John Doe", "cpf": "12345678942", "age": 30, "enrollment_status": "active"}
    )
    assert response_success.status_code == 201

def test_request_enrollment_cpf_already_exists():
    response_cpf_exists = client.post(
        "/enrollments", json={"name": "John Doe", "cpf": "12345678901", "age": 30, "enrollment_status": "active"}
    )
    assert response_cpf_exists.status_code == 400
