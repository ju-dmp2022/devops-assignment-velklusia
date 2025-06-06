FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT ["python", "calculator_rest_service.py", "--port=5001"]


