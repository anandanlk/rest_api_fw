import pytest
from lib.crud import APIClient
from config import BASE_URL_TEST_ENV, USERNAME, PASSWORD, TIMEOUT

# Instance of APIClient
@pytest.fixture(scope='module')
def api_client():
    client = APIClient(BASE_URL_TEST_ENV, TIMEOUT)
    yield client

# Create booking and return booking ID
@pytest.fixture(scope='module')
def booking_id(api_client):
    payload = {
        "firstname": "Anand",
        "lastname": "Krishna",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-10-28",
            "checkout": "2024-10-30"
        },
        "additionalneeds": "Breakfast"
    }
    response = api_client.post("booking", payload)
    assert response.status_code == 200
    return response.json()["bookingid"]

# Test authentication
def test_authenticate(api_client):
    response = api_client.authenticate(USERNAME, PASSWORD)
    assert response.status_code == 200
    assert "token" in response.json()

# Test booking
def test_create_booking(booking_id):
    assert booking_id is not None

# Testing Retrieve Booking
def test_get_booking(api_client, booking_id):
    response = api_client.get(f"booking/{booking_id}")
    assert response.status_code == 200
    assert response.json()["firstname"] == "Anand"
    assert response.json()["lastname"] == "Krishna"

# Test update booking
def test_update_booking(api_client, booking_id):
    payload = {
        "firstname": "Anandan",
        "lastname": "Krishnasamy",
        "totalprice": 300,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-10-28",
            "checkout": "2024-10-30"
        },
        "additionalneeds": "Breakfast"
    }
    response = api_client.put(f"booking/{booking_id}", payload)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Anandan"
    assert response.json()["lastname"] == "Krishnasamy"
    assert response.json()["totalprice"] == 300

# Test delete booking
def test_delete_booking(api_client, booking_id):
    response = api_client.delete(f"booking/{booking_id}")
    assert response.status_code == 201
