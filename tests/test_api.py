import requests
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.api.actions import calculate, login
from calculator_client.models import ResultResponse, User, UserResponse, ErrorResponse
from calculator_client.client import Client

BASE_URL = "http://localhost:5000"

# ADD tests #
def test_addition():
    client = Client(base_url="http://localhost:5000")
    response = calculate.sync(client=client, body=Calculation(
        operation=Opertions.ADD, operand1=2, operand2=2))
    assert isinstance(response, ResultResponse)
    assert response.result == 4


def test_addition_negative():
    client = Client(base_url="http://localhost:5000")
    response = calculate.sync(client=client, body=Calculation(
        operation=Opertions.ADD, operand1=-2, operand2=-2))
    assert response.result == -4

# SUBSTRACT tests #
def test_subtraction():
    client = Client(base_url="http://localhost:5000")
    response = calculate.sync(client=client, body=Calculation(
        operation=Opertions.SUBTRACT, operand1=10, operand2=2))
    assert response.result == 8


def test_subtraction_negative():
    client = Client(base_url="http://localhost:5000")
    response = calculate.sync(client=client, body=Calculation(
        operation=Opertions.SUBTRACT, operand1=-10, operand2=-4))
    assert response.result == -6


### MULTIPLY tests ###
def test_multiplication():
    client = Client(base_url="http://localhost:5000")
    response = calculate.sync(client=client, body=Calculation(
        operation=Opertions.MULTIPLY, operand1=5, operand2=5))
    assert response.result == 25


def test_multiplication_negative():
    client = Client(base_url="http://localhost:5000")
    response = calculate.sync(client=client, body=Calculation(
        operation=Opertions.MULTIPLY, operand1=-3, operand2=-3))
    assert response.result == 9

### DIVIDE tests ###
def test_division():
    client = Client(base_url="http://localhost:5000")
    response = calculate.sync(client=client, body=Calculation(
        operation=Opertions.DIVIDE, operand1=6, operand2=2))
    assert response.result == 3

def test_division_negative():
    client = Client(base_url="http://localhost:5000")
    response = calculate.sync(client=client, body=Calculation(
        operation=Opertions.DIVIDE, operand1=-8, operand2=-2))
    assert response.result == 4