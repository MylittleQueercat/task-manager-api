import uuid
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

TEST_USER = f"testuser_{uuid.uuid4().hex[:8]}"

def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello 42!"}

def test_register():
    response = client.post("/register", json={
        "username": TEST_USER,
        "password": "testpass"
    })
    assert response.status_code == 200

def test_login():
    response = client.post("/login", data={
        "username": TEST_USER,
        "password": "testpass"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_task():
    login_response = client.post("/login", data={
        "username": TEST_USER,
        "password": "testpass"
    })
    token = login_response.json()["access_token"]
    response = client.post("/tasks",
        json={"title": "Test task"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test task"