from fastapi.testclient import TestClient
from env import settings
from faker import Faker

from main import app

client = TestClient(app)
fake = Faker()

fake_name = fake.name()
fake_description = fake.address()


# def test_read_item():
#     response = client.get(settings.API_PREFIX+"/items/1", headers={"X-Token": "fake-super-secret-token"})
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": "foo",
#         "title": "Foo",
#         "description": "There goes my hero",
#     }

# def test_create_item():
#     response = client.post(
#         settings.API_PREFIX+"/users/1/items/",
#         headers={"X-Token": "fake-super-secret-token"},
#         json={"title": fake_name, "description": fake_description},
#     )
#     assert response.status_code == 200, response.text

#     # data = response.json()
#     # assert data["title"] == fake_name
#     # assert data["description"] == fake_description
#     # assert "id" in data
#     # item_id = data["id"]

#     # response = client.get(f"{settings.API_PREFIX}/items/{item_id}")
#     # assert response.status_code == 200, response.text
#     # data = response.json()
#     # assert data["title"] == fake_name
#     # assert data["description"] == fake_description
#     # assert data["id"] == item_id


# def test_read_items():
#     response = client.get(settings.API_PREFIX+"/items/", headers={"X-Token": "fake-super-secret-token"})
#     assert response.status_code == 200
#     # assert response.json() == {"detail": "Not Found"}


# def test_read_item():
#     response = client.get(settings.API_PREFIX+"/items/1", headers={"X-Token": "fake-super-secret-token"})
#     assert response.status_code == 200
#     # assert response.json() == {"detail": "Not Found"}


# def test_read_item_doesnt_exist():
#     response = client.get(settings.API_PREFIX+"/items/987654321", headers={"X-Token": "fake-super-secret-token"})
#     assert response.status_code == 404
#     # assert response.json() == {"detail": "Not Found"}
