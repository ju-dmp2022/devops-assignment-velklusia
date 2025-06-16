import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator_helper import CalculatorHelper

from calculator_helper import CalculatorHelper


class BaseTestCalculator:
    def setup_method(self, method):
        self.calculator = CalculatorHelper()

    def teardown_method(self, method):
        del self.calculator
