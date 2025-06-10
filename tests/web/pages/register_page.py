from tests.calculator_client.api.actions import logout
from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class RegisterPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver=driver)

        self.page_elements = {
            'username': Element('//input[@id="username"]', self),
            'password1': Element('//input[@id="password1"]', self),
            'password2': Element('//input[@id="password2"]', self),
            'register': Element('//button[@id="register"]', self)
        }

        self.elements = munchify(self.page_elements)

    ###
    ### Actions
    ###

    def register_user(self, username, password):
        self.elements.username.set(username)
        self.elements.password1.set(password)
        self.elements.password2.set(password)
        self.elements.register.click()
