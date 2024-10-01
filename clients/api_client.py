import requests
import logging

class APIClient:
    def __init__(self, base_url, timeout):
        self.base_url = base_url
        self.timeout = timeout
        self.log = logging.getLogger(__name__)

    def authenticate(self, username, password):
        auth_data = {"username": username, "password": password}
        self.log.info(f"Authenticating user {username}")
        response = requests.post(f"{self.base_url}/auth", json=auth_data, timeout=self.timeout)
        self.log.info(f"Response: {response.status_code} - {response.text}")
        if response.status_code == 200 and 'token' in response.json():
            self.token = response.json()['token']
        return response
    
    def get_headers(self, token_required=False):
        if token_required: # Token required for put, patch and delete
            headers = { "Content-Type": "application/json", "Accept": "application/json", "Cookie":f"token={self.token}"}
        else:
            headers = { "Content-Type": "application/json", "Accept": "application/json"}
        return headers

    def get(self, endpoint):
        self.log.info(f"GET {self.base_url}/{endpoint}")
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.get_headers(), timeout=self.timeout)
        self.log.info(f"Response: {response.status_code} - {response.text}")
        return response

    def post(self, endpoint, data):
        self.log.info(f"POST {self.base_url}/{endpoint} with payload {data}")
        response = requests.post(f"{self.base_url}/{endpoint}", json=data, headers=self.get_headers(), timeout=self.timeout)
        self.log.info(f"Response: {response.status_code} - {response.text}")
        return response

    def put(self, endpoint, data):
        self.log.info(f"PUT {self.base_url}/{endpoint} with payload {data}")
        response = requests.put(f"{self.base_url}/{endpoint}", json=data, headers=self.get_headers(token_required=True), timeout=self.timeout)
        self.log.info(f"Response: {response.status_code} - {response.text}")
        return response
    
    def patch(self, endpoint, data):
        self.log.info(f"PATCH {self.base_url}/{endpoint} with payload {data}")
        response = requests.patch(f"{self.base_url}/{endpoint}", json=data, headers=self.get_headers(token_required=True), timeout=self.timeout)
        self.log.info(f"Response: {response.status_code} - {response.text}")
        return response

    def delete(self, endpoint):
        self.log.info(f"DELETE {self.base_url}/{endpoint}")
        response = requests.delete(f"{self.base_url}/{endpoint}", headers=self.get_headers(token_required=True), timeout=self.timeout)
        self.log.info(f"Response: {response.status_code} - {response.text}")
        return response
