FROM python:3.12-slim

# working directory inside the container
WORKDIR /app

#COPY . /app/ samma sak men enklare

COPY . .

RUN pip install --no-cache-dir -r /app/requirements.txt

# Set the entry point to run your Python script
ENTRYPOINT ["python", "calculator.py"]


