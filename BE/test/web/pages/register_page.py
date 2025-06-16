from .page_base import PageBase
from web.helpers.element import Element
from munch import munchify


class RegisterPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver=driver)

        page_elements = {
            "username": Element('//input[@id="username"]', self),
            "password1": Element('//input[@id="password1"]', self),
            "password2": Element('//input[@id="password2"]', self),
            "register": Element('//button[@id="register"]', self),
        }

        self.elements = munchify(page_elements)
