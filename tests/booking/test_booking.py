import pytest
import logging
from config import USERNAME, PASSWORD
from models.model import Booking, PartialUpdate
from pydantic import ValidationError
from booking.fixtures.api_fixtures import api_client, test_data, booking_id

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
        logging.error(f'Data validation failed for the payload: {payload}')
        pytest.fail(f"Booking validation failed: {e}")
    response = api_client.put(f"booking/{booking_id}", booking.model_dump())
    assert response.status_code == 200
    assert response.json()["firstname"] == test_data["updated_booking"]["firstname"]
    assert response.json()["lastname"] == test_data["updated_booking"]["lastname"]

# Test partial update
def test_partial_update_booking(api_client, booking_id, test_data):
    payload = test_data["partial_update"]
    try:
        booking = PartialUpdate(**payload)
    except ValidationError as e:
        logging.error(f'Data validation failed for the payload: {payload}')
        pytest.fail(f"Booking validation failed: {e}")
    response = api_client.patch(f"booking/{booking_id}", booking.model_dump())
    assert response.status_code == 200
    assert response.json()["additionalneeds"] == test_data["partial_update"]["additionalneeds"]

# Test delete booking
def test_delete_booking(api_client, booking_id):
    response = api_client.delete(f"booking/{booking_id}")
    assert response.status_code == 201
