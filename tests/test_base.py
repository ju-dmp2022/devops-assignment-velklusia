import pytest

from BE.calculator_helper import CalculatorHelper

class BaseTestCalculator:
    def setup_method(self, method):
        self.calculator = CalculatorHelper()

    def teardown_method(self, method):
        del self.calculator