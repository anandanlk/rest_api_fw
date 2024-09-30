import os

BASE_URL_TEST_ENV = "https://restful-booker.herokuapp.com"
USERNAME = os.getenv("BOOKER_USER", "")
PASSWORD = os.getenv("BOOKER_PASS", "")
TIMEOUT = 30