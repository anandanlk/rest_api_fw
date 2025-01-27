import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
USERNAME = os.getenv("BOOKER_USER", "")
PASSWORD = os.getenv("BOOKER_PASS", "")
TIMEOUT = int(os.getenv("TIMEOUT", 30))