import pytest
from BE.calculator_helper import CalculatorHelper
from tests.calculator_client.client import Client

from selenium import webdriver

class WebTestBase:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

BASE_URL = "http://localhost:5001"
