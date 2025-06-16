from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage
from tests.web.pages.login_page import RegisterPage
from tests.web.pages.login_page import CalculatorPage


class TestWeb(WebBase):

    def test_login(self):
        LoginPage(self.driver).login('admin', 'test1234')
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'user-name'), 'admin')
        )
        assert CalculatorPage(self.driver).elements.user_name.text == 'admin'
        CalculatorPage(self.driver).logout()

    def test_register(self):
        login_page = LoginPage(self.driver)

        login_page.go_to_register()

        username = "newuser88888"
        register_page = RegisterPage(self.driver)
        register_page.register(username, "password123", "password123")

        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'user-name'), username)
        )

        assert CalculatorPage(self.driver).elements.user_name.text == username

        CalculatorPage(self.driver).logout()

    def test_calculation_methods(self):
        # Login first
        login_page = LoginPage(self.driver)
        login_page.login('admin', 'test1234')

        # Wait for the calculator screen to be ready
        calculator_page = CalculatorPage(self.driver)
        calculator_screen = calculator_page.elements.calculator_screen

        def perform_calculation_and_verify(expected_result):
            WebDriverWait(self.driver, 10).until(
                lambda driver: calculator_screen.value == expected_result
            )
            assert calculator_screen.value == expected_result, f"Expected {
                expected_result}, but got {calculator_screen.value}"

        calculator_page.elements.key_2.click()
        calculator_page.elements.key_add.click()
        calculator_page.elements.key_3.click()
        calculator_page.elements.key_equals.click()
        perform_calculation_and_verify('5')

        # Test 2: 7 - 4 = 3
        calculator_page.elements.key_7.click()
        calculator_page.elements.key_subtract.click()
        calculator_page.elements.key_4.click()
        calculator_page.elements.key_equals.click()
        perform_calculation_and_verify('3')

        # Test 3: 6 * 3 = 18
        calculator_page.elements.key_6.click()
        calculator_page.elements.key_multiply.click()
        calculator_page.elements.key_3.click()
        calculator_page.elements.key_equals.click()
        perform_calculation_and_verify('18')

        # Test 4: 8 / 2 = 4
        calculator_page.elements.key_8.click()
        calculator_page.elements.key_divide.click()
        calculator_page.elements.key_2.click()
        calculator_page.elements.key_equals.click()
        perform_calculation_and_verify('4')

        calculator_page.logout()

    def test_history_feature(self):
        # Step 1: Login
        login_page = LoginPage(self.driver)
        login_page.login('admin', 'test1234')

        # Step 2: Perform some calculations
        calculator_page = CalculatorPage(self.driver)

        # First calculation: 2 + 3 = 5
        calculator_page.elements.key_2.click()
        calculator_page.elements.key_add.click()
        calculator_page.elements.key_3.click()
        calculator_page.elements.key_equals.click()

        # Second calculation: 7 - 4 = 3
        calculator_page.elements.key_7.click()
        calculator_page.elements.key_subtract.click()
        calculator_page.elements.key_4.click()
        calculator_page.elements.key_equals.click()

        # Step 3: Open history by clicking the '>>'-button
        calculator_page.elements.toggle_history_button.click()

        # Step 4: Verify that previous calculations are shown in the history textarea
        history_text = calculator_page.elements.history_textarea.value

        # Verify the history contains the results of previous calculations
        assert "2+3=5" in history_text, "First calculation is not present in history"
        assert "7-4=3" in history_text, "Second calculation is not present in history"

        calculator_page.logout()
