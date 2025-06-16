# Use the official image as a parent image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "calculator_rest_service.py", "--port=5001"] 