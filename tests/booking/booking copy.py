import pytest
import logging
from config import USERNAME, PASSWORD
from schema.booking import Booking, PartialUpdate
from pydantic import ValidationError
from booking.fixtures.api_fixtures import api_client
from utils.data_loader import booking_data

# Test authentication
@pytest.mark.sanity
def test_authenticate(api_client):
    response = api_client.authenticate(USERNAME, PASSWORD)
    assert response.status_code == 200
    assert "token" in response.json()

# Test booking
@pytest.mark.sanity
@pytest.mark.parametrize("test_data", booking_data())
def test_booking_operations(api_client, test_data):
    # Create Booking
    booking_id = create_booking(api_client, test_data)
    assert booking_id is not None

    # Get Booking
    retrieve_booking(api_client, booking_id, test_data)

    # Update Booking
    update_booking(api_client, booking_id, test_data)

    # Partial Update
    partial_update_booking(api_client, booking_id, test_data)

    # Delete Booking
    delete_booking(api_client, booking_id)

def create_booking(api_client, test_data):
    logging.info(f"Creating booking with data: {test_data['booking']}")
    payload = test_data["booking"]
    try:
        booking = Booking(**payload)
    except ValidationError as e:
        logging.error(f'Data validation failed for the payload: {payload}')
        pytest.fail(f"Booking validation failed: {e}")
    response = api_client.post("booking", booking.model_dump())
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    logging.info(f"Creating booking with data: {test_data['booking']} is successful")
    return response.json()["bookingid"]

def retrieve_booking(api_client, booking_id, test_data):
    logging.info(f"Retrieving created booking using booking_id: {booking_id}")
    response = api_client.get(f"booking/{booking_id}") 
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    booking_data = response.json()
    for field in test_data['booking']:
        assert booking_data[field] == test_data['booking'][field]
    logging.info(f"Retrieving created booking using booking_id: {booking_id} is successful")

def update_booking(api_client, booking_id, test_data):
    logging.info(f"Updating booking with data: {test_data['updated_booking']}")
    payload = test_data["updated_booking"]
    try:
        booking = Booking(**payload)
    except ValidationError as e:
        logging.error(f'Data validation failed for the payload: {payload}')
        pytest.fail(f"Booking validation failed: {e}")
    response = api_client.put(f"booking/{booking_id}", booking.model_dump())
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    booking_data = response.json()
    for field in test_data['updated_booking']:
        assert booking_data[field] == test_data['updated_booking'][field]
    logging.info(f"Updating booking with data: {test_data['updated_booking']} is successful")

def partial_update_booking(api_client, booking_id, test_data):
    logging.info(f"Partial update booking with data: {test_data['partial_update']}")
    payload = test_data["partial_update"]
    try:
        booking = PartialUpdate(**payload)
    except ValidationError as e:
        logging.error(f'Data validation failed for the payload: {payload}')
        pytest.fail(f"Booking validation failed: {e}")
    response = api_client.patch(f"booking/{booking_id}", booking.model_dump())
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    booking_data = response.json()
    for field in test_data['partial_update']:
        if field in ["checkin", "checkout"]:
            assert booking_data["bookingdates"][field] == test_data['partial_update'][field]
        else:
            assert booking_data[field] == test_data['partial_update'][field]
    logging.info(f"Partial update booking with data: {test_data['partial_update']} is successful")

def delete_booking(api_client, booking_id):
    logging.info(f"Deleting booking using booking_id: {booking_id}")
    response = api_client.delete(f"booking/{booking_id}")
    assert response.status_code == 201
    logging.info(f"Deleting booking using booking_id: {booking_id} is successful")
