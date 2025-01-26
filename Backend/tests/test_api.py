from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_restaurant():
    response = client.post("/restaurants/", json={"name": "Test Place", "cuisine_type": "Italian"})
    assert response.status_code == 201
    assert response.json()["name"] == "Test Place"

def test_create_rating():
    response = client.post("/ratings/", json={"restaurant_id": 1, "rating": 4.5, "calories": 500})
    assert response.status_code == 201
    assert response.json()["rating"] == 4.5
