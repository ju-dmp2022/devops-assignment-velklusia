from tests.calculator_client.api.actions import logout
from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from assertpy import assert_that
from munch import munchify
import time

class CalculatorPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver=driver)

        self.page_elements = {
            # Add more elements here as needed....
            
            'logout': Element('//button[@id="logout-button"]', self),
            'username': Element('//label[@id="user-name"]', self),
        }

        self.elements = munchify(self.page_elements)

    ###
    ### Actions
    ###

    def get_username(self):
        retries = 0
        while self.elements.username.text == "" and retries < 15:
            time.sleep(1)
            retries += 1

        assert_that(self.elements.username.text).is_not_empty()
        return self.elements.username.text
    
    def logout(self):
        self.elements.logout.click()