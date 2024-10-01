import logging
from utils.validate_payload import validate_payload
from utils.validate_response import validate_response_status, validate_response_data
from schema.booking import Booking, PartialUpdate

class BookingAPI:
    def __init__(self, api_client):
        self.api_client = api_client
        self.booking_id = None

    def create_booking(self, test_data):
        logging.info(f"Creating booking with data: {test_data['booking']}")
        payload = test_data["booking"]

        # Validate payload
        booking = validate_payload(Booking, payload)

        # Make API request
        response = self.api_client.post("booking", booking.model_dump())

        # Validate response
        validate_response_status(response, expected_status_code=200, content_type="application/json; charset=utf-8")

        logging.info(f"Creating booking with data: {test_data['booking']} is successful")
        self.booking_id = response.json()["bookingid"]  # Store booking_id
        return self.booking_id

    def retrieve_booking(self, test_data):
        if self.booking_id is None:
            raise ValueError("No booking ID available. Please create a booking first.")
            
        logging.info(f"Retrieving created booking using booking_id: {self.booking_id}")
        response = self.api_client.get(f"booking/{self.booking_id}")

        # Validate response
        validate_response_status(response, expected_status_code=200, content_type="application/json; charset=utf-8")

        # Compare booking data
        booking_data = response.json()
        validate_response_data(test_data['booking'], booking_data)

        logging.info(f"Retrieving created booking using booking_id: {self.booking_id} is successful")

    def update_booking(self, test_data):
        if self.booking_id is None:
            raise ValueError("No booking ID available. Please create a booking first.")

        logging.info(f"Updating booking with data: {test_data['updated_booking']}")
        payload = test_data["updated_booking"]

        # Validate payload
        booking = validate_payload(Booking, payload)

        # Make API request
        response = self.api_client.put(f"booking/{self.booking_id}", booking.model_dump())

        # Validate response
        validate_response_status(response, expected_status_code=200, content_type="application/json; charset=utf-8")

        # Compare updated booking data
        booking_data = response.json()
        validate_response_data(test_data['updated_booking'], booking_data)

        logging.info(f"Updating booking with data: {test_data['updated_booking']} is successful")

    def partial_update_booking(self, test_data):
        if self.booking_id is None:
            raise ValueError("No booking ID available. Please create a booking first.")

        logging.info(f"Partial update booking with data: {test_data['partial_update']}")
        payload = test_data["partial_update"]

        # Validate payload
        booking = validate_payload(PartialUpdate, payload)

        # Make API request
        response = self.api_client.patch(f"booking/{self.booking_id}", booking.model_dump())

        # Validate response
        validate_response_status(response, expected_status_code=200, content_type="application/json; charset=utf-8")

        # Compare partial updated booking data
        booking_data = response.json()
        validate_response_data(test_data['partial_update'], booking_data)

        logging.info(f"Partial update booking with data: {test_data['partial_update']} is successful")

    def delete_booking(self):
        if self.booking_id is None:
            raise ValueError("No booking ID available. Please create a booking first.")

        logging.info(f"Deleting booking using booking_id: {self.booking_id}")
        response = self.api_client.delete(f"booking/{self.booking_id}")

        # Validate response
        validate_response_status(response, expected_status_code=201)

        logging.info(f"Deleting booking using booking_id: {self.booking_id} is successful")
        self.booking_id = None
