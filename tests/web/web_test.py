import pytest
from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage

class TestWeb(WebBase):

    def test_login(self):
        LoginPage(self.driver).login('admin', 'test1234')

        # LoginPage(self.driver).elements.username.set('admin')
        # LoginPage(self.driver).elements.password.set('test1234')
        # LoginPage(self.driver).elements.login.click()
        
        # a =  1  
                                 