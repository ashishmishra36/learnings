import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(scope='module')
def init_driver():
    print('----------------------------Setting up----------------------------')
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://www.google.com/')

    yield driver
    print('----------------------------tearing down----------------------------')
    driver.quit()


#The purpose of a fixture is to automatically provide the resource (in this case, the driver) to your test functions.
# By simply including the fixture name (init_driver) as a parameter in your test function, pytest will inject the
# fixture's output (the WebDriver instance) into your test.

def test_google(init_driver):
    assert 'Google' in init_driver.title

def test_url(init_driver):
    assert 'https://www.google.com/' == init_driver.current_url
