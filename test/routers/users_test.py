from fastapi.testclient import TestClient
from env import settings
from faker import Faker
from app.middlewares import auth
from typing import Optional
from app.utils.uuid import generate_uuid

from main import app

client = TestClient(app)
fake = Faker()
local_prefix = "/users/"

fake_email = fake.email()
fake_name = fake.name()
fake_password = fake.password()


async def override_dependency(email: Optional[str] = fake_email,):
    return {"id": generate_uuid(), "email": email,
            "full_name": fake_name, "is_active": 1}

app.dependency_overrides[auth.get_current_active_user] = override_dependency


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

    # GET TOKEN FOR AUTHORIZE READ USER BY ID
    response = client.post(
        settings.API_PREFIX+local_prefix+"token",
        data={"username": fake_email, "password": fake_password},
    )
    assert response.status_code == 200, response.text
    token_data = response.json()
    assert token_data['token_type'] is not None
    assert token_data['access_token'] is not None

    # READ USER BY ID
    headers = {"Authorization":
               f"{token_data['token_type']} {token_data['access_token']}"}
    response = client.get(f"{settings.API_PREFIX}{local_prefix}{user_id}",
                          headers=headers)
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
    token_data = response.json()
    assert token_data['token_type'] is not None
    assert token_data['access_token'] is not None

    # READ ME
    headers = {"Authorization":
               f"{token_data['token_type']} {token_data['access_token']}"}
    response = client.get(
        f"{settings.API_PREFIX}{local_prefix}me/",
        headers=headers
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert id is not None
    assert data["email"] == fake_email

    # READ USERS
    response = client.get(settings.API_PREFIX+local_prefix,
                          headers=headers)
    assert response.status_code == 200

    # READ USER DOESNT EXIST
    response = client.get(settings.API_PREFIX+local_prefix+"987654321",
                          headers=headers)
    assert response.status_code == 404


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
