import pytest
from BE.calculator_helper import CalculatorHelper
from tests.calculator_client.client import Client

import sys
import os

BASE_URL = "http://localhost:5001"

class BaseTestCalculator:
    def setup_method(self, method):
        """Setup method to run before every test."""
        self.calculator = CalculatorHelper()
        self.client = Client(base_url=BASE_URL)

    def teardown_method(self, method):
        """Teardown method to run after every test."""
        del self.calculator
        del self.client