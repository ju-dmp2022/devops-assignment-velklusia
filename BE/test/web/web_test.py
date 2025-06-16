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
        username_input.send_keys(username)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_input.clear()
        password_input.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login"))
        )
        login_button.click()

        wait = WebDriverWait(self.driver, 20)
        try:
            wait.until(lambda d: "login.html" not in d.current_url)
        except TimeoutException:
            print("Login failed or took too long")
            print("Current URL:", self.driver.current_url)
            print("Page source snippet:", self.driver.page_source[:1000])
            raise

        wait.until(EC.visibility_of_element_located((By.ID, "calculator-screen")))

        self.wait_and_click(By.ID, "key-2")
        self.wait_and_click(By.ID, "key-add")
        self.wait_and_click(By.ID, "key-3")
        self.wait_and_click(By.ID, "key-equals")
        assert CalculatorPage(self.driver).elements["calculator_screen"].value == "5", "Add calculation failed"

        self.wait_and_click(By.ID, "key-7")
        self.wait_and_click(By.ID, "key-subtract")
        self.wait_and_click(By.ID, "key-4")
        self.wait_and_click(By.ID, "key-equals")
        assert CalculatorPage(self.driver).elements["calculator_screen"].value == "3", "Subtract calculation failed"

        self.wait_and_click(By.ID, "key-2")
        self.wait_and_click(By.ID, "key-multiply")
        self.wait_and_click(By.ID, "key-3")
        self.wait_and_click(By.ID, "key-equals")
        assert CalculatorPage(self.driver).elements["calculator_screen"].value == "6", "Multiply calculation failed"

        self.wait_and_click(By.ID, "key-6")
        self.wait_and_click(By.ID, "key-divide")
        self.wait_and_click(By.ID, "key-3")
        self.wait_and_click(By.ID, "key-equals")
        assert CalculatorPage(self.driver).elements["calculator_screen"].value == "2", "Divide calculation failed"

    def test_history_feature(self, username, password):
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

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login"))
        )
        login_button.click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(lambda d: "login.html" not in d.current_url)

        wait.until(EC.visibility_of_element_located((By.ID, "calculator-screen")))

        # Perform calculations
        self.wait_and_click(By.ID, "key-2")
        self.wait_and_click(By.ID, "key-add")
        self.wait_and_click(By.ID, "key-3")
        self.wait_and_click(By.ID, "key-equals")

        self.wait_and_click(By.ID, "key-7")
        self.wait_and_click(By.ID, "key-subtract")
        self.wait_and_click(By.ID, "key-4")
        self.wait_and_click(By.ID, "key-equals")

        # Open history by clicking '>>' button (toggle_history_button)
        self.wait_and_click(By.ID, "toggle-button")

        history_text = CalculatorPage(self.driver).elements.history_textarea.value

        assert "2+3=5" in history_text, f"Expected '2+3=5' in history but got:\n{history_text}"
        assert "7-4=3" in history_text, f"Expected '7-4=3' in history but got:\n{history_text}"