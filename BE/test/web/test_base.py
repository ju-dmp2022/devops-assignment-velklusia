from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from BE.test.calculator_client.api.actions import logout
from BE.test.calculator_client.client import Client


class WebBase:

    @classmethod
    def setup_class(cls):
        """Setup to run once: initiate some common parameters"""
        cls.app_url = 'http://localhost:8080'

    def setup_method(self):
        """Setup to run before every test: initiate a new browser driver"""
        logout.sync(client=Client(base_url="http://localhost:5001"))
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
        self.driver.set_window_size(1920, 1080)
        self.driver.get(self.app_url)

    def teardown_method(self):
        """Teardown to run after every test: stop the browser driver"""
        self.driver.quit()
