import pytest
from lib.crud import APIClient
from config import BASE_URL_TEST_ENV, USERNAME, PASSWORD, TIMEOUT

api_client = APIClient(BASE_URL_TEST_ENV, TIMEOUT)

# Testing authentication/credentials
def test_authenticate():
    response = api_client.authenticate(USERNAME, PASSWORD)
    assert response.status_code == 200
    assert "token" in response.json()
