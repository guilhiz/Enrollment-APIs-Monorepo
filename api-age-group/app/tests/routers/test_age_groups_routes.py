from app.config.auth.auth import get_basic_auth_header
from fastapi.testclient import TestClient
from app.config.mongodb import db_manager

from app.main import app

client = TestClient(app)

auth_header = get_basic_auth_header("admin", "secret")

def test_retrieve_list_of_age_groups_successfully():
    age_groups_response = client.get("/age-groups", headers=auth_header)
    assert age_groups_response.status_code == 200
    age_groups_data = age_groups_response.json()
    assert "max_age" in age_groups_data[0]
    assert len(age_groups_data) > 0


def test_add_new_age_group_successfully():
    add_response = client.post("/age-groups", json={"min_age": 7, "max_age": 51}, headers=auth_header)
    assert add_response.status_code == 201
    age_group_data = add_response.json()
    assert "max_age" in age_group_data
    db_manager.delete_item(age_group_data["id"])

def test_add_new_age_group_fails_due_to_missing_parameters():
    missing_params_response = client.post("/age-groups", json={}, headers=auth_header)
    assert missing_params_response.status_code == 422


def test_delete_existing_age_group_successfully():
    age_group_id = db_manager.add_item({"min_age": 7, "max_age": 51})["id"]

    delete_response = client.delete(f"/age-groups/{age_group_id}", headers=auth_header)
    assert delete_response.status_code == 204


def test_delete_nonexistent_age_group():
    nonexistent_delete_response = client.delete("/age-groups/662d676dfae3b87935a62111", headers=auth_header)
    assert nonexistent_delete_response.status_code == 404
