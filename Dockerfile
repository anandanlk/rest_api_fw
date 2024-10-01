FROM python:3.9-slim

WORKDIR /api-tests

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY clients/ ./clients
COPY data/ ./data
COPY schema/ ./schema
COPY tests/ ./tests
COPY utils/ ./utils
COPY config.py ./
COPY pytest.ini ./

ENV PYTHONPATH=/api-tests

CMD ["pytest", "tests/", "-v"]
