from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from BE.test.calculator_client.api.actions import logout
from BE.test.calculator_client.client import Client


class WebBase:

    @classmethod
    def setup_class(cls):
        cls.app_url = 'http://host.docker.internal:8080' 

    def setup_method(self):
        logout.sync(client=Client(base_url="http://localhost:5001"))

        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=chrome_options
        )
        self.driver.set_window_size(1920, 1080)
        self.driver.get(self.app_url)

    def teardown_method(self):
        self.driver.quit()
