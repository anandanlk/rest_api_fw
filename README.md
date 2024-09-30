# **REST API Test Automation Framework**

## **Project Overview**

This project is a Python-based automation framework to test REST APIs. It uses _requests_, _pytest_, _python-dotenv_, _pydantic_ and _logger_ libraries and integrated with Docker for easy deployment and execution. It utilizes environment variables for configuration.

### **Prerequisites**

- Python 3.9 or higher
- Docker Desktop

### **Installation**

1. Clone the repository:

```
   git clone https://github.com/anandanlk/rest_api_fw.git
```

2. Install dependencies:

```
   pip install -r requirements.txt
```

### **Usage**

1. **Configure API Details:**

   Create dotenv '.env' file with following variables (or) update os environment

```
   BASE_URL=https://restful-booker.herokuapp.com
   BOOKER_USER=your_username
   BOOKER_PASS=your_password
   TIMEOUT=30
```

2. **Update data:**

- Update `data\user_data.json' as needed

3. **Run Tests Locally:**

   ```
   pytest tests/ -v
   ```

4. **Run Tests and Create html reports:**

   ```
   pip install pytest-html
   pytest tests/ -v --html=report.html
   ```

5. **Run Tests and create Allure reports:**

   ```
   pip install allure-pytest
   pytest tests/ -v --alluredir=allure_results
   allure serve allure_results
   ```

6. **Run Tests in Docker Container:**

```
   docker build -t api-tests .
   docker run --env-file .env api-tests
```

6. **Run Tests in Docker Container and copy logs to local folder:**

```
   docker run --env-file .env --rm -v $(pwd)/logs:/api-tests/logs api-tests
```

### **Project Structure**

- _config.py_: Imports configuration details from OS Environment.
- _lib/api_client.py_: Contains libraries for CRUD operations.
- _models/model.py_: Data Object model.
- _tests/test_sample.py_: Contains test cases.
- _requirements.txt_: Contains list of required Python libraries.
- _Dockerfile'_: Contains the Docker image build process.
- _logs/test_logs.log_: Captures session logs.
- _pytest.ini_: Defines logfile and level.
