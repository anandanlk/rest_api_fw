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

4. **To view Allure reports:**

   ```
   allure serve allure_results
   ```

5. **Run Tests in Docker Container:**

```
   docker build -t api-tests .
   docker run --env-file .env api-tests
```

6. **Run Tests in Docker Container and copy logs to local folder:**

```
   docker run --env-file .env --rm -v $(pwd)/logs:/api-tests/logs api-tests
```

### **Project Structure**

- _clients_: Contains libraries for CRUD operations.
- _data_: Contains user and booking data to test.
- _logs_: To store session logs.
- _modules_: Contains module libraries
- _schema_: Scehma validation.
- _tests_: Contains test cases.
- _utils_: Contains common utilities.
- _.env_: Environment variables.
- _config.py_: Imports configuration details from OS Environment or .env file.
- _Dockerfile'_: Contains the Docker image build process.
- _requirements.txt_: Contains list of required Python libraries.
- _pytest.ini_: Defines logfile and level.
