import requests
from config import BASE_URL

class APIClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def authenticate(self, username, password):
        auth_data = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/auth", json=auth_data)
        if response.status_code == 200:
            self.token = response.json()['token']
        return response

    def get(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}")
        return response

    def post(self, endpoint, data):
        response = requests.post(f"{self.base_url}/{endpoint}", json=data)
        return response

    def put(self, endpoint, data):
        response = requests.put(f"{self.base_url}/{endpoint}", json=data)
        return response

    def delete(self, endpoint):
        response = requests.delete(f"{self.base_url}/{endpoint}")
        return response
