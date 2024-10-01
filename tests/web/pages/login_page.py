from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class LoginPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        self.page_elements = {
            'username': Element('//input[@id="username"]', self),
        }

        self.elements = munchify(self.page_elements)

def login (self, username, password):
    self.elements.username.set(username)
    self.elements.password.set(password)
    self.elements.login.click()