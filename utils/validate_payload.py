import logging
from pydantic import ValidationError
import pytest

def validate_payload(schema, payload):
    try:
        validated_data = schema(**payload)
        return validated_data
    except ValidationError as e:
        logging.error(f'Data validation failed for the payload: {payload}')
        pytest.fail(f"Validation failed: {e}")
