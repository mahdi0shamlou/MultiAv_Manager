import sys
sys.path.insert(0, "..")
from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_status_cape():
    response = client.get("/tasks/list/")

    assert response.status_code == 200
    res = response.json()
    for i in ["status", "data"]:
        assert i in res



