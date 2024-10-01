import pytest
import logging
from schema.user import User
from pydantic import ValidationError
from booking.fixtures.api_fixtures import api_client
from utils.data_loader import user_data

# Test authentication
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
    assert "token" in response.json()
