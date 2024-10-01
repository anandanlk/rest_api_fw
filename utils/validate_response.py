def validate_response_status(response, expected_status_code=None, content_type=None):
    if expected_status_code:
        assert response.status_code == expected_status_code
    if content_type:
        assert response.headers["Content-Type"] == content_type

def validate_response_data(expected_data, actual_data):
    for field in expected_data:
        if field in ["checkin", "checkout"]:
            assert actual_data["bookingdates"][field] == expected_data[field]
        else:
            assert actual_data[field] == expected_data[field]
