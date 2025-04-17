import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    web_driver= None
    if request.param== 'chrome':
        print('----------------------------Setting up----------------------------')
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # web_driver = webdriver.Chrome(options=chrome_options)
        web_driver = webdriver.Chrome()
    if request.param=='firefox':
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        web_driver = webdriver.Firefox(options=firefox_options)
        # web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    print(f'test name is : {request.node.name}')

    yield
    print('----------------------------tearing down----------------------------')
    web_driver.quit()
