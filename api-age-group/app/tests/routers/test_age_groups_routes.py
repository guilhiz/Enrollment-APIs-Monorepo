from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_age_groups():
    response = client.get("/age-groups")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data[0]
    assert len(data) > 0


def test_add_age_group():
    response = client.post("/age-groups", json={"id": 12, "min_age": 7, "max_age": 51})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data


def test_delete_age_group():
    response = client.delete("/age-groups/12")
    assert response.status_code == 204
