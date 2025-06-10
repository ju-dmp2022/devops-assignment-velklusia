import pytest
import random
from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage
from tests.web.pages.register_page import RegisterPage
from tests.web.pages.calculator_page import CalculatorPage
from assertpy import assert_that

class TestWeb(WebBase):
    admin_user = 'admin'
    admin_password = 'test1234'
    
    def test_login(self):
        LoginPage(self.driver).login(self.admin_user, self.admin_password)
        assert_that(CalculatorPage(self.driver).elements.username.text).is_equal_to(self.admin_user)
        CalculatorPage(self.driver).logout()
        
    def test_register_user(self):
        username = f"test{random.randint(1,99999)}"
        password = "password"
        LoginPage(self.driver).elements.register.click()
        RegisterPage(self.driver).register_user(username, password)
        assert_that(CalculatorPage(self.driver).get_username()).is_equal_to(username)
        CalculatorPage(self.driver).logout()