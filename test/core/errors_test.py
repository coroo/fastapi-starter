from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_not_found():
    response = client.get("/read-not-found")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
