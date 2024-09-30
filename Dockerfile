FROM python:3.9-slim

WORKDIR /api-tests

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY config.py ./
COPY lib/ ./lib
COPY tests/ ./tests
COPY data/ ./data
COPY pytest.ini ./

ENV PYTHONPATH=/api-tests

CMD ["pytest", "tests/", "-v"]
