import pytest
from calculator_client.client import Client
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.api.actions import calculate


@pytest.fixture
def client():
    return Client(base_url="http://localhost:5001")


def test_calculate_addition(client):
    # Arrange
    calculation = Calculation(operand1=5, operand2=3,
                              operation=Opertions.ADD)

    # Act
    result = calculate.sync(client=client, body=calculation)

    # Assert
    assert result is not None, "API call returned None"
    assert result.result == 8


def test_calculate_subtraction(client):
    # Arrange
    calculation = Calculation(
        operand1=5, operand2=3, operation=Opertions.SUBTRACT)

    # Act
    result = calculate.sync(client=client, body=calculation)

    # Assert
    assert result is not None, "API call returned None"
    assert result.result == 2
