import pytest
import logging
from config import USERNAME, PASSWORD
from booking.fixtures.api_fixtures import api_client
from utils.data_loader import booking_data
from utils.validate_response import validate_response_status
from modules.booking_api import BookingAPI

# Test authentication
@pytest.mark.sanity
def test_authenticate(api_client):
    response = api_client.authenticate(USERNAME, PASSWORD)
    validate_response_status(response, expected_status_code=200, content_type="application/json; charset=utf-8")
    assert "token" in response.json()

# Test booking operations
@pytest.mark.sanity
@pytest.mark.parametrize("test_data", booking_data())
def test_booking_operations(api_client, test_data):
    booking_api = BookingAPI(api_client)

    # Create Booking
    booking_id = booking_api.create_booking(test_data)
    assert booking_id is not None

    # Get Booking
    booking_api.retrieve_booking(test_data)

    # Update Booking
    booking_api.update_booking(test_data)

    # Partial Update
    booking_api.partial_update_booking(test_data)

    # Delete Booking
    booking_api.delete_booking()
