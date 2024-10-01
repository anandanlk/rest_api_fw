import pytest
import json
import os
import logging
from lib.api_client import APIClient
from config import BASE_URL, TIMEOUT
from models.model import User, Booking
from pydantic import ValidationError
from utils.data_loader import booking_data

# Instance of APIClient
@pytest.fixture(scope='module')
def api_client():
    client = APIClient(BASE_URL, TIMEOUT)
    yield client

# # Create booking and return booking ID
# @pytest.fixture(scope='function')
# @pytest.mark.parametrize("test_data", booking_data())
# def booking_id(api_client, test_data, request):
#     payload = test_data["booking"]
#     # Validating payload using the Booking model
#     try:
#         booking = Booking(**payload)
#     except ValidationError as e:
#         logging.error(f'Data validation failed for the payload: {payload}')
#         pytest.fail(f"Booking validation failed: {e}")

#     # Create booking    
#     response = api_client.post("booking", booking.model_dump())
#     assert response.status_code == 200
#     booking_id = response.json()["bookingid"]
    
#     # Finalizer
#     def delete_booking():
#         check_response = api_client.get(f"booking/{booking_id}")
#         if check_response.status_code == 200:
#             del_response = api_client.delete(f"booking/{booking_id}")
#             assert del_response.status_code in [200, 201]
#         elif check_response.status_code == 404:
#             logging.info(f"Booking ID {booking_id} does not exist, skipping deletion.")

#     request.addfinalizer(delete_booking)
#     return booking_id