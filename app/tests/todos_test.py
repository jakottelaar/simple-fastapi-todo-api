from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert response.json() == []