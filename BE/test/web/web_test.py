from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import pytest
from .test_base import WebBase
from .pages.login_page import LoginPage
from .pages.register_page import RegisterPage
from .pages.calculator_page import CalculatorPage
import time


@pytest.fixture
def username():
    return "admin"

@pytest.fixture
def password():
    return "test1234"


class TestWeb(WebBase):

    def wait_and_click(self, locator_type, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        print(f"Waiting up to {timeout} seconds for element {locator} by {locator_type} to be clickable...")
        try:
            element = wait.until(EC.presence_of_element_located((locator_type, locator)))
            print(f"Element {locator} found in DOM. Waiting to be clickable...")
            element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
            element.click()
            print(f"Clicked element {locator} successfully.")
        except TimeoutException:
            print(f"Timeout: Element {locator} by {locator_type} not clickable after {timeout} seconds.")
            raise
        except Exception as e:
            print(f"Error clicking element {locator}: {e}")
            raise

    def test_register(self, username, password):
        self.wait_and_click(By.ID, "register") 
        RegisterPage(self.driver).elements["username"].set(username)
        RegisterPage(self.driver).elements["password1"].set(password)
        RegisterPage(self.driver).elements["password2"].set(password)
        self.wait_and_click(By.ID, "register") 

    def test_login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_input.clear()
        username_input.send_keys(username)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_input.clear()
        password_input.send_keys(password)

        self.wait_and_click(By.ID, "login")

    def test_calculation_methods(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_input.clear()
        print(f"Typing username: {username}")
        username_input.send_keys(username)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_input.clear()
        print(f"Typing password: {password}")
        password_input.send_keys(password)

        self.wait_and_click(By.ID, "login")
        print("Clicked login button, waiting for calculator screen...")

        time.sleep(2)

        wait = WebDriverWait(self.driver, 20)
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "calculator_screen")))
        except TimeoutException:
            print("Calculator screen not visible after login. Login probably failed.")
            print("Current URL:", self.driver.current_url)
            print("Page source snippet:", self.driver.page_source[:1000])

            try:
                err = self.driver.find_element(By.ID, "errormsg")
                print("Error message on page:", err.text)
            except:
                print("No error message element found.")
            raise

        # Calculator operations
        self.wait_and_click(By.ID, "key_2")
        self.wait_and_click(By.ID, "key_add")
        self.wait_and_click(By.ID, "key_3")
        self.wait_and_click(By.ID, "key_equals")
        assert CalculatorPage(self.driver).elements["calculator_screen"].value == "5", "Add calculation failed"

        self.wait_and_click(By.ID, "key_7")
        self.wait_and_click(By.ID, "key_subtract")
        self.wait_and_click(By.ID, "key_4")
        self.wait_and_click(By.ID, "key_equals")
        assert CalculatorPage(self.driver).elements["calculator_screen"].value == "3", "Subtract calculation failed"

        self.wait_and_click(By.ID, "key_2")
        self.wait_and_click(By.ID, "key_multiply")
        self.wait_and_click(By.ID, "key_3")
        self.wait_and_click(By.ID, "key_equals")
        assert CalculatorPage(self.driver).elements["calculator_screen"].value == "6", "Multiply calculation failed"

        self.wait_and_click(By.ID, "key_6")
        self.wait_and_click(By.ID, "key_divide")
        self.wait_and_click(By.ID, "key_3")
        self.wait_and_click(By.ID, "key_equals")
        assert CalculatorPage(self.driver).elements["calculator_screen"].value == "2", "Divide calculation failed"
