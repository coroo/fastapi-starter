from fastapi.testclient import TestClient
from env import settings
from faker import Faker

from main import app

client = TestClient(app)
fake = Faker()

fake_name = fake.name()
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

    # READ ITEMS
    response = client.get(settings.API_PREFIX+"/items/",
                          headers=headers,)
    assert response.status_code == 200

    # READ ITEM
    response = client.get(settings.API_PREFIX+"/items/"+str(data['id']),
                          headers=headers,)
    assert response.status_code == 200

    # READ NOT EXIST ITEM
    response = client.get(settings.API_PREFIX+"/items/987654321",
                          headers=headers,)
    assert response.status_code == 404
