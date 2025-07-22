import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from utils.logger import generate_logger

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# URL of your Selenium Grid hub
grid_url = "http://172.17.0.2:4444/wd/hub"


@pytest.fixture(params=['docker'], scope='class')
def init_driver(request):
    print(f'Test name is : {request.node.name}')
    web_driver= None
    if request.param== 'chrome':
        print('----------------------------Setting up----------------------------')
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        web_driver = webdriver.Chrome(options=chrome_options)
        # web_driver = webdriver.Chrome()
    if request.param== 'docker':
        print('----------------------------Setting up----------------------------')
        options = ChromeOptions()
        options.browser_name = 'chromium'  # Force Chromium
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        web_driver = webdriver.Remote(command_executor=grid_url,options=options)
    # if request.param=='firefox':
    #     # firefox_options = Options()
    #     # firefox_options.add_argument("--headless")
    #     # web_driver = webdriver.Firefox(options=firefox_options)
    #     web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    print('----------------------------tearing down----------------------------')
    web_driver.quit()



