import pytest
import retry
from .test_base import WebBase
from .pages.login_page import LoginPage
from .pages.register_page import RegisterPage
from .pages.calculator_page import CalculatorPage


@pytest.fixture
def username():
    return "user"


@pytest.fixture
def password():
    return "test1234"


class TestWeb(WebBase):

    # tests registering a new user
    def test_register(self, username, password):
        RegisterPage(self.driver).elements.register.click()
        RegisterPage(self.driver).elements["username"].set(username)
        RegisterPage(self.driver).elements["password1"].set(password)
        RegisterPage(self.driver).elements["password2"].set(password)
        RegisterPage(self.driver).elements.register.click()

    # tests logging in
    def test_login(self, username, password):
        LoginPage(self.driver).elements["username"].set(username)
        LoginPage(self.driver).elements["password"].set(password)
        LoginPage(self.driver).elements.login.click()

    def test_calculator(self):

        # login
        LoginPage(self.driver).elements['username'].set('admin')
        LoginPage(self.driver).elements['password'].set('test1234')
        LoginPage(self.driver).elements.login.click()

        # add
        CalculatorPage(self.driver).elements["key_2"].click()
        CalculatorPage(self.driver).elements["key_add"].click()
        CalculatorPage(self.driver).elements["key_3"].click()
        CalculatorPage(self.driver).elements["key_equals"].click()
        assert CalculatorPage(self.driver).elements["calculator_screen"].value == "5"

        # subtract
        CalculatorPage(self.driver).elements["key_7"].click()
        CalculatorPage(self.driver).elements["key_subtract"].click()
        CalculatorPage(self.driver).elements["key_4"].click()
        CalculatorPage(self.driver).elements["key_equals"].click()
        assert CalculatorPage(self.driver).elements["calculator_screen"].value == "3"

        # multiply
        CalculatorPage(self.driver).elements["key_2"].click()
        CalculatorPage(self.driver).elements["key_multiply"].click()
        CalculatorPage(self.driver).elements["key_3"].click()
        CalculatorPage(self.driver).elements["key_equals"].click()
        assert CalculatorPage(self.driver).elements["calculator_screen"].value == "6"

        # divide
        CalculatorPage(self.driver).elements["key_6"].click()
        CalculatorPage(self.driver).elements["key_divide"].click()
        CalculatorPage(self.driver).elements["key_3"].click()
        CalculatorPage(self.driver).elements["key_equals"].click()
        # timer to sleep for 1 second
        
        assert CalculatorPage(self.driver).elements["calculator_screen"].value == "2"

    def test_history(self):

        # # logout
        # CalculatorPage(self.driver).elements["logout_button"].click()

        # # login
        # LoginPage(self.driver).elements["username"].set("admin")
        # LoginPage(self.driver).elements["password"].set("test1234")
        # LoginPage(self.driver).elements["login"].click()

        calculator_page = CalculatorPage(self.driver) 

        calculator_page.elements["key_2"].click()
        calculator_page.elements["key_add"].click()
        calculator_page.elements["key_3"].click()
        calculator_page.elements["key_equals"].click()

        calculator_page.elements["key_7"].click()
        calculator_page.elements["key_subtract"].click()
        calculator_page.elements["key_4"].click()
        calculator_page.elements["key_equals"].click()

        calculator_page.elements["toggle_history_button"].click()

        history_text = calculator_page.elements.history_textarea.value

        assert "2+3=5" in history_text, f"Expected '2+3=5' in history, but got {history_text}"
        assert "7-4=3" in history_text, f"Expected '7-4=3' in history, but got {history_text}"
