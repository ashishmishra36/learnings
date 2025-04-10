import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    web_driver= None
    if request.param== 'chrome':
        print('----------------------------Setting up----------------------------')
        web_driver = webdriver.Chrome()
    if request.param=='firefox':
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    print(f'test name is : {request.node.name}')

    yield
    print('----------------------------tearing down----------------------------')
    web_driver.quit()
