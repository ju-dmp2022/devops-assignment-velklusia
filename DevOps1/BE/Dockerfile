FROM python:3.12-slim

# working directory inside the container
WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application into the container
COPY . /app/

# Set the entry point to run your Python script
ENTRYPOINT ["python", "calculator.py"]


