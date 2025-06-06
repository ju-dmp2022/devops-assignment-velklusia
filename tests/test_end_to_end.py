from assertpy import assert_that
from selenium.webdriver.common.by import By
from test_base import WebTestBase  # this works since it's in the same folder

class TestEndToEnd(WebTestBase):
    def test_full_flow(self):
        self.driver.get("http://localhost:8080")  # or host.docker.internal if you're in Docker

        # Register a new user
        self.driver.find_element(By.ID, "register").click()
        self.driver.find_element(By.ID, "username").send_keys("testuser123")
        self.driver.find_element(By.ID, "password").send_keys("password123")
        self.driver.find_element(By.ID, "confirm").send_keys("password123")
        self.driver.find_element(By.ID, "register-button").click()

        success = self.driver.find_element(By.ID, "register-success").text
        assert_that(success).contains("success")

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
