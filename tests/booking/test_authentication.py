import pytest
import logging
from schema.user import User
from pydantic import ValidationError
from booking.fixtures.api_fixtures import api_client
from utils.data_loader import user_data, invalid_user_data

# Test authentication with valid data
@pytest.mark.parametrize("user", user_data())
def test_authenticate(api_client, user):
    logging.info(f"Testing authentication with user: {user}")

    # Validate user data
    try:
        validated_user = User(**user)
    except ValidationError as e:
        logging.error(f'Invalid user data for the user {user}: {e}')
        pytest.fail(f"Invalid user data for the user {user}: {e}")

    # authenticate
    response = api_client.authenticate(validated_user.username, validated_user.password)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert "token" in response.json()

# Test authentication with invalid data
@pytest.mark.parametrize("invalid_user", invalid_user_data())
def test_authenticate_invalid(api_client, invalid_user):
    logging.info(f"Testing authentication with invalid user: {invalid_user}")

    # Validate user data
    try:
        validated_user = User(**invalid_user)
    except ValidationError as e:
        logging.error(f'Invalid user data for the user {invalid_user}: {e}')
        pytest.fail(f"Invalid user data for the user {invalid_user}: {e}")

    # Authenticate
    response = api_client.authenticate(invalid_user.get("username", ""), invalid_user.get("password", ""))
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert "token" not in response.json()