import pytest
import json
import os
import logging
from lib.api_client import APIClient
from config import BASE_URL, USERNAME, PASSWORD, TIMEOUT
from models.model import Booking, PartialUpdate
from pydantic import ValidationError

# Load test data
@pytest.fixture(scope='module')
def test_data():
    current_dir = os.path.dirname(__file__)
    test_data_path = os.path.join(current_dir, '..', 'data', 'user_data.json')
    with open(test_data_path) as f:
        return json.load(f)

# Define log file nmae and format
@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    current_dir = os.path.dirname(__file__)
    log_dir = os.path.join(current_dir, '..', 'logs')

    # Create log directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_path = os.path.join(log_dir, 'test_logs.log')

    logging.basicConfig(filename=log_path, filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         level=logging.INFO)
    logging.info("Starting test session")

# Instance of APIClient
@pytest.fixture(scope='module')
def api_client():
    client = APIClient(BASE_URL, TIMEOUT)
    yield client

# Create booking and return booking ID
# @pytest.fixture(scope='module')
# def booking_id(api_client, test_data):
#     payload = test_data["booking"]
#     response = api_client.post("booking", payload)
#     assert response.status_code == 200
#     return response.json()["bookingid"]

# Create booking and return booking ID
@pytest.fixture(scope='module')
def booking_id(api_client, test_data):
    payload = test_data["booking"]
    # Validating payload using the Booking model
    try:
        booking = Booking(**payload)
    except ValidationError as e:
        logging.error(f'Data validation failed foir the payload: {payload}')
        pytest.fail(f"Booking validation failed: {e}")
    response = api_client.post("booking", booking.model_dump())
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
def test_get_booking(api_client, booking_id, test_data):
    response = api_client.get(f"booking/{booking_id}")
    assert response.status_code == 200
    assert response.json()["firstname"] == test_data["booking"]["firstname"]
    assert response.json()["lastname"] == test_data["booking"]["lastname"]

# Test update booking
def test_update_booking(api_client, booking_id, test_data):
    payload = test_data["updated_booking"]
    # Validating payload using the Booking model
    try:
        booking = Booking(**payload)
    except ValidationError as e:
        logging.error(f'Data validation failed foir the payload: {payload}')
        pytest.fail(f"Booking validation failed: {e}")
    response = api_client.put(f"booking/{booking_id}", booking.model_dump())
    assert response.status_code == 200
    assert response.json()["firstname"] == test_data["updated_booking"]["firstname"]
    assert response.json()["lastname"] == test_data["updated_booking"]["lastname"]
    assert response.json()["lastname"] == test_data["updated_booking"]["lastname"]

# Test partial update
def test_partial_update_booking(api_client, booking_id, test_data):
    payload = test_data["partial_update"]
    try:
        booking = PartialUpdate(**payload)
    except ValidationError as e:
        logging.error(f'Data validation failed foir the payload: {payload}')
        pytest.fail(f"Booking validation failed: {e}")
    response = api_client.patch(f"booking/{booking_id}", booking.model_dump())
    assert response.status_code == 200
    assert response.json()["additionalneeds"] == test_data["partial_update"]["additionalneeds"]

# Test delete booking
def test_delete_booking(api_client, booking_id):
    response = api_client.delete(f"booking/{booking_id}")
    assert response.status_code == 201
