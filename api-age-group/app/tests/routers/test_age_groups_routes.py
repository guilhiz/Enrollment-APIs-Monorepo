from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_retrieve_list_of_age_groups_successfully():
    age_groups_response = client.get("/age-groups")
    assert age_groups_response.status_code == 200
    age_groups_data = age_groups_response.json()
    assert "max_age" in age_groups_data[0]
    assert len(age_groups_data) > 0

def test_add_new_age_group_successfully():
    add_response = client.post("/age-groups", json={"min_age": 7, "max_age": 51})
    assert add_response.status_code == 201

def test_add_new_age_group_fails_due_to_missing_parameters():
    missing_params_response = client.post("/age-groups", json={})
    assert missing_params_response.status_code == 422

def test_delete_existing_age_group_successfully():
    #cria faixa etaria
    #busco faixa etaria
    delete_response = client.delete("/age-groups/662d676dfae3b87935a62140")
    assert delete_response.status_code == 204

def test_delete_nonexistent_age_group():
    nonexistent_delete_response = client.delete("/age-groups/662d676dfae3b87935a62111")
    assert nonexistent_delete_response.status_code == 404
