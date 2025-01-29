import sys
sys.path.insert(0, "..")
from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_tasks_list():
    response = client.get("/tasks/list/")

    assert response.status_code == 200
    res = response.json()
    for i in ["status", "data"]:
        assert i in res

def test_task_details():
    response = client.get("/tasks/details/1")

    assert response.status_code == 200
    res = response.json()
    for i in ["status", "data"]:
        assert i in res