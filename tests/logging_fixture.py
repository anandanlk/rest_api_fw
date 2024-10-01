import pytest
import os
import logging

# Configure logging
@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    current_dir = os.path.dirname(__file__)
    log_dir = os.path.join(current_dir, '..', '..', '..', 'logs')

    # Create log directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_path = os.path.join(log_dir, 'test_logs.log')

    logging.basicConfig(filename=log_path, filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logging.info("Starting test session")
