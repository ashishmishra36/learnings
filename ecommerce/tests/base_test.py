import pytest
from configs.config import TestData
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures('init_driver')
class BaseTest:
    driver: WebDriver
    pass

    # use pytest.fal only under the tests, for any other unexpected error use raiseError
    @pytest.fixture(autouse=True)
    def launch_application(self, request):
        env = request.config.getoption('--env').upper()
        print(f'0-----------0-0-0- {env}')
        if env:
            url = getattr(TestData, f'BASE_URL_{env}', None)
            self.driver.get(str(url))
        else:
            raise ValueError(f'Error !! environment argument is not valid')
