# **REST API Test Automation Framework**

## **Project Overview**

This is a Python-based automation framework to test [restful-booker](https://restful-booker.herokuapp.com/apidoc/index.html) REST API. It uses _requests_, _pytest_, _python-dotenv_, _pydantic_ and _logger_ libraries and integrated with Docker for easy deployment and execution. It utilizes environment variables for configuration. The framework also generates allure reports.

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

   Create dotenv '.env' file with following variables (or) update os environment variable

```
   BASE_URL=https://restful-booker.herokuapp.com
   BOOKER_USER=your_username
   BOOKER_PASS=your_password
   TIMEOUT=30
```

2. **Update data:**

- Update `data\user_data.json' if needed
- Update `data\booking_data.json' if needed

3. **Run Tests Locally:**

   ```
   pytest tests/ -v
   ```

4. **Run Tests and Create html reports:**

   ```
   pip install pytest-html
   pytest tests/ -v --html=report.html
   ```

5. **To view Allure reports:**

   ```
   pip install allure-pytest
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

- _clients/api_client.py_: Contains libraries for CRUD operations.
- _data/user_data.json_: Contains user data to test.
- _data/invalid_user_data.json_: Contains invalid user data to test.
- _data/booking_data.json_: Contains booking data to test.
- _logs/_: To store session logs.
- _schema/schema.py_: Scehma validation.
- _tests/test_sample.py_: Contains test cases.
- _utils/data_loader.py_: Contains data loader library.
- _.env_: Environment variables.
- _config.py_: Imports configuration details from OS Environment or .env file.
- _Dockerfile'_: Contains the Docker image build process.
- _requirements.txt_: Contains list of required Python libraries.
- _pytest.ini_: Defines logfile and level.
