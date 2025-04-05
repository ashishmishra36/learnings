import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# important : test should be starting with test or ending with test
@pytest.mark.skip
def test_method_one():
    a, b = 4, 5
    assert a==b, 'test failed: a and b are not equal'

@pytest.mark.skip
def test_method_two():
    s = 'Ashish'
    assert len(s)==6, 'test failed: length is not as per expectation'


@pytest.mark.parametrize('first, second', [(1,2),(4,2), (23,3)])
def test_login(first,second):
    assert first>second, 'Error ! 3 is not equal to 4 !!'

@pytest.mark.skip
def test_method_three():
    s = 'Ashish'
    assert len(s) == 6, 'test failed: length is not as per expectation'

@pytest.mark.parametrize('word', ['ashish', 'mishra', 'qwedfg', 'pixel'])
def test_method_four(word):
    assert len(word)==6, 'test failed: length is not as per expectation'

@pytest.mark.skip
def test_google():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get('https://www.google.com/')
    assert driver.title =='Google'
    driver.quit()

@pytest.mark.skip
def test_facebook():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get('https://www.facebook.com/')
    assert driver.title =='Facebook - log in or sign up'
    driver.quit()

@pytest.mark.skip
def test_linkedin():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get('https://www.linkedin.com/feed/')
    assert driver.title =='LinkedIn'
    driver.quit()

@pytest.mark.skip
def test_perm_time_line():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get('https://permtimeline.com/')
    assert driver.title =='PERM Processing Time'
    driver.quit()

