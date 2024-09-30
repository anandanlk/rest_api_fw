# **REST API Test Automation Framework**

## **Project Overview**

This project is a Python-based automation framework to test REST APIs. It uses _requests_, _pytest_ and _python-dotenv_ libraries and integrated with Docker for easy deployment and execution. It utilizes environment variables for configuration.

### **Prerequisites**

- Python 3.9 or higher
- Docker Desktop

### **Installation**

1. Clone the repository:
   git clone https://github.com/anandanlk/rest_api_fw.git

2. Install dependencies:
   pip install -r requirements.txt

### **Usage**

1. **Configure API Details:**

   Create dotenv '.env' file with following variables (or) update os environment

   - BASE_URL=https://restful-booker.herokuapp.com
   - BOOKER_USER=your_username
   - BOOKER_PASS=your_password
   - TIMEOUT=30

2. **Run Tests Locally:**
   pytest tests/ -v

3. **Run Tests in Docker Container:**
   docker build -t api-tests .
   docker run --env-file .env api-tests

### **Project Structure**

- _config.py_: Imports configuration details from OS Environment.
- _lib\crud.py_: Contains libraries for CRUD operations.
- _tests\test_sample.py_: Contains test cases.
- _requirements.txt_: Contains list of required Python libraries.
- _Dockerfile'_: Contains the Docker image build process.
