from fastapi.testclient import TestClient
from env import settings
from faker import Faker

from main import app

client = TestClient(app)
fake = Faker()
local_prefix = "/users/"

fake_email = fake.email()
fake_password = fake.password()


def test_create_user():
    response = client.post(
        settings.API_PREFIX+local_prefix,
        json={"email": fake_email, "password": fake_password},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == fake_email
    assert "id" in data
    user_id = data["id"]

    response = client.get(f"{settings.API_PREFIX}{local_prefix}{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == fake_email
    assert data["id"] == user_id


def test_create_token():
    response = client.post(
        settings.API_PREFIX+local_prefix+"token",
        data={"username": fake_email, "password": fake_password},
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data['token_type'] is not None
    assert data['access_token'] is not None

    headers = {"Authorization":
               f"{data['token_type']} {data['access_token']}"}
    response = client.get(
        f"{settings.API_PREFIX}{local_prefix}me/",
        headers=headers
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert id is not None
    assert data["email"] == fake_email


def test_create_token_with_invalid_credentials():
    response = client.post(
        settings.API_PREFIX+local_prefix+"token",
        data={"username": fake_email, "password": 'wrong_email'},
    )

    assert response.status_code == 401


def test_create_user_duplicate():
    response = client.post(
        settings.API_PREFIX+local_prefix,
        json={"email": fake_email, "password": fake_password},
    )
    assert response.status_code == 400, response.text


def test_read_users():
    response = client.get(settings.API_PREFIX+local_prefix)
    assert response.status_code == 200
    # assert response.json() == {"detail": "Not Found"}


# def test_read_me():
#     response = client.get(settings.API_PREFIX+"/users/me/")
#     assert response.status_code == 200
#     # assert response.json() == {"detail": "Not Found"}


# def test_read_user():
#     response = client.get(settings.API_PREFIX+"/users/1")
#     assert response.status_code == 200
#     # assert response.json() == {"detail": "Not Found"}


def test_read_user_doesnt_exist():
    response = client.get(settings.API_PREFIX+local_prefix+"987654321")
    assert response.status_code == 404
    # assert response.json() == {"detail": "Not Found"}
