import pytest

from BE.calculator_helper import CalculatorHelper
from calculator_client.client import Client

BASE_URL = "http://localhost:5000"

class BaseTestCalculator:
    def setup_method(self, method):
        self.calculator = CalculatorHelper()
        self.client = Client(base_url=BASE_URL)

    def teardown_method(self, method):
        del self.calculator