import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=['chrome', 'firefox'], scope='class')
def init_driver(request):
    web_driver= None
    if request.param== 'chrome':
        print('----------------------------Setting up----------------------------')
        service = ChromeService(executable_path=ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=service)
    if request.param=='firefox':
        # Instantiate GeckoDriverManager first, then call install()
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        web_driver = webdriver.Firefox(service=service)
    request.cls.driver = web_driver
    print(f'test name is : {request.node.name}')

    yield web_driver
    print('----------------------------tearing down----------------------------')
    web_driver.quit()