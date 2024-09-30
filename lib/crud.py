import requests

class APIClient:
    def __init__(self, base_url, timeout):
        self.base_url = base_url
        self.timeout = timeout

    def authenticate(self, username, password):
        auth_data = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/auth", json=auth_data, timeout=self.timeout)
        if response.status_code == 200:
            self.token = response.json()['token']
        return response
    
    def get_headers(self):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        if self.token:
            headers["Cookie"] = f"token={self.token}"
        return headers

    def get(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.get_headers(), timeout=self.timeout)
        return response

    def post(self, endpoint, data):
        response = requests.post(f"{self.base_url}/{endpoint}", json=data, headers=self.get_headers(), timeout=self.timeout)
        return response

    def put(self, endpoint, data):
        response = requests.put(f"{self.base_url}/{endpoint}", json=data, headers=self.get_headers(), timeout=self.timeout)
        return response

    def delete(self, endpoint):
        response = requests.delete(f"{self.base_url}/{endpoint}", headers=self.get_headers(), timeout=self.timeout)
        return response
