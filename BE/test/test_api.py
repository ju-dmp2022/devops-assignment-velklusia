import requests

BASE_URL = "http://localhost:5001"

def test_addition():
    response = requests.post(f"{BASE_URL}/calculate", json={
        "operation": "add",
        "operand1": 3,
        "operand2": 4
    }, timeout=10)
    assert response.status_code == 200
    assert response.json()["result"] == 7

def test_subtraction():
    response = requests.post(f"{BASE_URL}/calculate", json={
        "operation": "subtract",
        "operand1": 10,
        "operand2": 4
    }, timeout=10)
    assert response.status_code == 200
    assert response.json()["result"] == 6

def test_multiplication():
    response = requests.post(f"{BASE_URL}/calculate", json={
        "operation": "multiply",
        "operand1": 3,
        "operand2": 4
    }, timeout=10)
    assert response.status_code == 200
    assert response.json()["result"] == 12

def test_division():
    response = requests.post(f"{BASE_URL}/calculate", json={
        "operation": "divide",
        "operand1": 8,
        "operand2": 2
    }, timeout=10)
    assert response.status_code == 200
    assert response.json()["result"] == 4
