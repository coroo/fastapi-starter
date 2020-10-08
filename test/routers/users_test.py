from fastapi.testclient import TestClient
from env import settings
from faker import Faker

from main import app

client = TestClient(app)
fake = Faker()

fake_email = fake.email()
fake_password = fake.password()

def test_create_user():
    response = client.post(
        settings.API_PREFIX+"/users/",
        json={"email": fake_email, "password": fake_password},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == fake_email
    assert "id" in data
    user_id = data["id"]

    response = client.get(f"{settings.API_PREFIX}/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == fake_email
    assert data["id"] == user_id

def test_create_user_duplicate():
    response = client.post(
        settings.API_PREFIX+"/users/",
        json={"email": fake_email, "password": fake_password},
    )
    assert response.status_code == 400, response.text

def test_read_users():
    response = client.get(settings.API_PREFIX+"/users/")
    assert response.status_code == 200
    # assert response.json() == {"detail": "Not Found"}

def test_read_user():
    response = client.get(settings.API_PREFIX+"/users/1")
    assert response.status_code == 200
    # assert response.json() == {"detail": "Not Found"}

def test_read_user_doesnt_exist():
    response = client.get(settings.API_PREFIX+"/users/987654321")
    assert response.status_code == 404
    # assert response.json() == {"detail": "Not Found"}