from .page_base import PageBase
from web.helpers.element import Element
from munch import munchify


class CalculatorPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver=driver)

        page_elements = {
            "key_0": Element('//button[@id="key-0"]', self),
            "key_1": Element('//button[@id="key-1"]', self),
            "key_2": Element('//button[@id="key-2"]', self),
            "key_3": Element('//button[@id="key-3"]', self),
            "key_4": Element('//button[@id="key-4"]', self),
            "key_5": Element('//button[@id="key-5"]', self),
            "key_6": Element('//button[@id="key-6"]', self),
            "key_7": Element('//button[@id="key-7"]', self),
            "key_8": Element('//button[@id="key-8"]', self),
            "key_9": Element('//button[@id="key-9"]', self),
            "key_add": Element('//button[@id="key-add"]', self),
            "key_subtract": Element('//button[@id="key-subtract"]', self),
            "key_multiply": Element('//button[@id="key-multiply"]', self),
            "key_divide": Element('//button[@id="key-divide"]', self),
            "key_equals": Element('//button[@id="key-equals"]', self),
            "key_clear": Element('//button[@id="key-clear"]', self),
            "logout_button": Element('//button[@id="logout"]', self),
            "toggle_history_button": Element('//button[@id="toggle-button"]', self),
            "history_textarea": Element('//textarea[@id="history"]', self),
            "calculator_screen": Element('//input[@id="calculator-screen"]', self)
        }

        self.elements = munchify(page_elements)
