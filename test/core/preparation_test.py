from fastapi.testclient import TestClient
from env import settings
from app.middlewares import auth
from typing import Optional
from app.utils.uuid import generate_uuid

from main import app

client = TestClient(app)
local_prefix = "/users/"

email = "coroo.wicaksono@gmail.com"
name = "Kuncoro Wicaksono"
password = "mysecretpass"


async def override_dependency(email: Optional[str] = email,):
    return {"id": generate_uuid(), "email": email,
            "full_name": name, "is_active": 1}


def test_create_defined_user():
    app.dependency_overrides[
        auth.get_current_active_user] = override_dependency
    response = client.post(
        settings.API_PREFIX+local_prefix,
        json={"email": email,
              "password": password},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == email
    assert "id" in data


def test_login_with_wrong_user():
    email = "wrong.user@gmail.com"
    password = "mysecretpass"
    response = client.post(
        settings.API_PREFIX+local_prefix+"token",
        data={"username": email, "password": password},
    )
    assert response.status_code == 401, response.text
    # data = response.json()
    # assert data["email"] == email
    # assert "id" in data
    # user_id = data["id"]

    # response = client.get(f"{settings.API_PREFIX}{local_prefix}{user_id}")
    # assert response.status_code == 200, response.text
    # data = response.json()
    # assert data["email"] == email
    # assert data["id"] == user_id
