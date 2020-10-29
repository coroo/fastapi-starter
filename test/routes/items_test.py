from fastapi.testclient import TestClient
from env import settings
from faker import Faker

from main import app

client = TestClient(app)
fake = Faker()
local_prefix = "/items/"

fake_name = fake.name()
fake_name_2 = fake.name()
fake_description = fake.address()


def test_func_items():
    response = client.post(
        settings.API_PREFIX+"/users/token",
        data={"username": "coroo.wicaksono@gmail.com",
              "password": "mysecretpass"},
    )

    assert response.status_code == 200, response.text
    session_data = response.json()
    assert session_data['token_type'] is not None
    assert session_data['access_token'] is not None

    # POST ITEM
    headers = {"Authorization":
               f"{session_data['token_type']} {session_data['access_token']}"}
    response = client.post(
        settings.API_PREFIX+"/users/1/items/",
        headers=headers,
        json={"title": fake_name, "description": fake_description},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['id'] is not None
    assert "id" in data
    item_id = data["id"]

    # READ ITEMS
    response = client.get(settings.API_PREFIX+"/items/",
                          headers=headers,)
    assert response.status_code == 200

    # READ ITEM
    response = client.get(settings.API_PREFIX+"/items/"+str(data['id']),
                          headers=headers,)
    assert response.status_code == 200

    # UPDATE ITEM
    response = client.put(
        f"{settings.API_PREFIX}{local_prefix}{item_id}",
        json={"title": fake_name_2, "description": fake_description},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] != fake_name
    assert data["title"] == fake_name_2

    # DELETE ITEM
    response = client.delete(
        f"{settings.API_PREFIX}{local_prefix}",
        json={"id": item_id},
    )
    assert response.status_code == 200

    # NEGATIVE TEST
    wrong_id = 90123801902930923  # just random id

    # UPDATE ITEM
    response = client.put(
        f"{settings.API_PREFIX}{local_prefix}{wrong_id}",
        json={"title": fake_name_2, "description": fake_description},
    )
    assert response.status_code == 404, response.text

    # DELETE ITEM
    response = client.delete(
        f"{settings.API_PREFIX}{local_prefix}",
        json={"id": wrong_id},
    )
    assert response.status_code == 404

    # READ NOT EXIST ITEM
    response = client.get(f"{settings.API_PREFIX}{local_prefix}{item_id}",
                          headers=headers,)
    assert response.status_code == 404
