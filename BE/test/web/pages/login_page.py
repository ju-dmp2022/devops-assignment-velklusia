from .page_base import PageBase
from web.helpers.element import Element
from munch import munchify


class LoginPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver=driver)

        page_elements = {
            "username": Element('//input[@id="username"]', self),
            "password": Element('//input[@id="password"]', self),
            "login": Element('//button[@id="login"]', self),
        }

        self.elements = munchify(page_elements)
