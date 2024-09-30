import pytest
from lib.crud import APIClient

api_client = APIClient()

def test_authenticate():
    response = api_client.authenticate(username="admin", password="password123")
    assert response.status_code == 200
    assert "token" in response.json()
