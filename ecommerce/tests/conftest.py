import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.firefox.options import Options as FirefoxOption


# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# URL of your Selenium Grid hub
grid_url = "http://172.17.0.2:4444/wd/hub"

# it will parse the value of browser given in command line
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser name given in command")
    parser.addoption("--headless", action="store_true", help="run browser in headless mode")


# parameterized with multiple data set
@pytest.fixture(scope='class')
def init_driver(request):
    """
    :param request:means pytest injects the default fixture request object into the fixture
    here getoption will retrieve the value given in the command line, and it will pass to the fixture
    But we need to register the command line option
    """
    browser = request.config.getoption('--browser').lower()
    headless = request.config.getoption('--headless')
    driver=None
    print(f'----------------------------Setting up: {browser}----------------------------')
    if browser== 'chrome':
        chrome_options = ChromeOption()
        if headless:
            chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
    elif browser== 'docker':
        options = ChromeOption()
        options.browser_name = 'chromium'  # Force Chromium
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Remote(command_executor=grid_url,options=options)
    elif browser=='firefox':
        firefox_options = FirefoxOption()
        if headless:
            firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        pytest.fail('Error! no browser provided !')

    request.cls.driver = driver
    yield
    print('----------------------------tearing down----------------------------')
    driver.quit()



