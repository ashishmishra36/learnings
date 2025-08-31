import pytest
from configs.config import TestData
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures('init_driver')
class BaseTest:
    driver: WebDriver
    pass

    @pytest.fixture(autouse=True)
    def launch_application(self, request):
        self.driver.get(TestData.BASE_URL)
