from assertpy import assert_that
from selenium.webdriver.common.by import By
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BE.calculator_helper import CalculatorHelper
from test_base import WebTestBase

class TestEndToEnd(WebTestBase):
    def test_full_flow(self):
        self.driver.get("http://localhost:8080")  # or host.docker.internal if you're in Docker

         # Register a new user

        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            ).send_keys("testuser123")

        self.driver.find_element(By.ID, "password1").send_keys("password123")
        self.driver.find_element(By.ID, "password2").send_keys("password123")
        self.driver.find_element(By.ID, "register").click()

        success = self.driver.find_element(By.ID, "errormsg").text
        assert_that(success.lower()).contains("success")


        # Login
        self.driver.find_element(By.ID, "username").send_keys("testuser123")
        self.driver.find_element(By.ID, "password").send_keys("password123")
        self.driver.find_element(By.ID, "login-button").click()

        # Perform calculation
        self.perform_calc_and_assert(3, 2, "add", "5")
        self.perform_calc_and_assert(10, 3, "subtract", "7")
        self.perform_calc_and_assert(4, 2, "multiply", "8")
        self.perform_calc_and_assert(8, 2, "divide", "4")

        # Open history
        self.driver.find_element(By.ID, "history-toggle").click()
        history = self.driver.find_element(By.ID, "history").text
        assert_that(history).contains("3 + 2")
        assert_that(history).contains("10 - 3")
        assert_that(history).contains("4 * 2")
        assert_that(history).contains("8 / 2")

    def perform_calc_and_assert(self, a, b, op_id, expected_result):
        self.driver.find_element(By.ID, "operand1").clear()
        self.driver.find_element(By.ID, "operand1").send_keys(str(a))

        self.driver.find_element(By.ID, "operand2").clear()
        self.driver.find_element(By.ID, "operand2").send_keys(str(b))

        self.driver.find_element(By.ID, op_id).click()

        result = self.driver.find_element(By.ID, "result").text
        assert_that(result).is_equal_to(expected_result)
