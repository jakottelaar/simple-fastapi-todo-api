from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

todo_id = ""

def test_create_todo():
    response = client.post("/api/v1/todos", json={"title": "Test Todo"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Todo"
    assert response.json()["completed"] == False
    assert "id" in response.json()
    
    global todo_id
    todo_id = response.json()["id"]

def test_get_todos():
    response = client.get("/api/v1/todos")
    assert response.status_code == 200
    assert response.json() != []

def test_get_todo_by_id():
    response = client.get(f"/api/v1/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Todo"
    assert response.json()["completed"] == False
    assert "id" in response.json()

def test_update_todo():
    response = client.put(f"/api/v1/todos/{todo_id}", json={"title": "Updated Todo"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Todo"
    assert response.json()["completed"] == False
    assert "id" in response.json()

def test_delete_todo():
    response = client.delete(f"/api/v1/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted successfully"}