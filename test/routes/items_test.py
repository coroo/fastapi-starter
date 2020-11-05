from fastapi.testclient import TestClient
from env import settings
from faker import Faker
import pytest

from main import app

client = TestClient(app)
# DEFINE MOCK DATA
fake = Faker()
fake_name = fake.name()
fake_name_2 = fake.name()
fake_description = fake.address()

local_prefix = "/items/"


class TestItems():
    @pytest.fixture(autouse=True)
    def _setup(self):
        # REQUEST AND TOKEN SETUP
        response = client.post(
            settings.API_PREFIX+"/users/token",
            data={"username": "coroo.wicaksono@gmail.com",
                  "password": "mysecretpass"},
        )

        assert response.status_code == 200, response.text
        session_data = response.json()
        assert session_data['token_type'] is not None
        assert session_data['access_token'] is not None

        # TOKEN HEADERS
        headers = {
            "Authorization":
            f"{session_data['token_type']} {session_data['access_token']}"}
        self.headers = headers

        # NEGATIVE TEST
        self.wrong_id = 912093018209302910

    def test_create(self):
        response = client.post(
            settings.API_PREFIX+"/users/1/items/",
            headers=self.headers,
            json={"title": fake_name, "description": fake_description},
        )
        assert response.status_code == 200, response.text

    @pytest.fixture(autouse=True)
    def test_get(self):
        # READ ITEMS
        response = client.post(
            settings.API_PREFIX+"/users/1/items/",
            headers=self.headers,
            json={"title": fake_name, "description": fake_description},
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data['id'] is not None
        assert "id" in data
        self.id_test = data['id']

        response = client.get(settings.API_PREFIX+"/items/",
                              headers=self.headers,)
        assert response.status_code == 200

        # READ ITEM
        response = client.get(settings.API_PREFIX+"/items/"+str(data['id']),
                              headers=self.headers,)
        assert response.status_code == 200

    def test_update(self):
        response = client.put(
            f"{settings.API_PREFIX}{local_prefix}{self.id_test}",
            json={"title": fake_name_2, "description": fake_description},
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["title"] != fake_name
        assert data["title"] == fake_name_2

    def test_delete(self):
        response = client.delete(
            f"{settings.API_PREFIX}{local_prefix}",
            json={"id": self.id_test},
        )
        assert response.status_code == 200

    # ============ NEGATIVE TEST ============
    def test_negative_get(self):
        response = client.get(f"{settings.API_PREFIX}{local_prefix}" +
                              f"{self.wrong_id}",
                              headers=self.headers,)
        assert response.status_code == 404

    def test_negative_update(self):
        response = client.put(
            f"{settings.API_PREFIX}{local_prefix}{self.wrong_id}",
            json={"title": fake_name_2, "description": fake_description},
        )
        assert response.status_code == 404, response.text

    def test_negative_delete(self):
        response = client.delete(
            f"{settings.API_PREFIX}{local_prefix}",
            json={"id": self.wrong_id},
        )
        assert response.status_code == 404
