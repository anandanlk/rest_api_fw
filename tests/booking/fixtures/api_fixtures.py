import pytest
from clients.api_client import APIClient
from config import BASE_URL, TIMEOUT
from pydantic import ValidationError
from utils.data_loader import booking_data

# Instance of APIClient
@pytest.fixture(scope='module')
def api_client():
    client = APIClient(BASE_URL, TIMEOUT)
    yield client
