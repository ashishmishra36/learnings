import os
import time
from pathlib import Path
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

""" 
This file has basic methods of launching browsers, using different kind of locators 
"""

@pytest.mark.skip
def test_first_way():
    """ Basic launch: first way to launch a browser: use the automatic downloaded chromedriver at runtime"""
    driver = webdriver.Chrome()
    time.sleep(2)
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    assert driver.title=='ProtoCommerce', 'Correct page is not loaded !'
    # enter the name, password and click on submit
    driver.find_element(By.NAME,'email').send_keys('test@test.com')
    # hint xpath: //tagname[@attribute='value']
    # hint css selector- its almost same as xpath : tagname[attribute='value']
    # hint css selector: <#id> , <.className>
    # driver.find_element(By.XPATH,'//input[@type="password"]').send_keys('2345678')
    driver.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys('2345678')
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    message = driver.find_element(By.CLASS_NAME,'alert-success').text
    print(f'Form Submitted: {message}')
    assert message.replace("×", "").strip() == 'Success! The Form has been submitted successfully!.' , 'Error text is not matching !'

    driver.quit()
    print('Basic launch: first way  is finished')

@pytest.mark.skip
def test_second_way():
    # second way to launch a browser: use the explicit manually downloaded chrome driver
    # Why ? sometimes chromedriver could not be downloaded at runtime
    print('second way: to launch a browser use the explicit manually downloaded chrome driver')
    chromedriver_path = Path("resources/chromedriver.exe").resolve()
    print(os.path.isfile(chromedriver_path))
    service_obj= Service(str(chromedriver_path))
    driver1 = webdriver.Chrome(service=service_obj)
    driver1.get('https://www.google.com')
    assert driver1.title == 'Google', 'Test2: Title is not correct ! '
    driver1.quit()
    print('Basic launch: second way is finished')

@pytest.mark.skip
def test_third_way():
    #third way: using webdriver manager which automatically download the chrome driver for the version present in system
    # recommended for CI/CD
    print('third way: using webdriver manager which automatically download the chrome driver for the version present in system')
    obj_service = Service(ChromeDriverManager().install())
    driver2=webdriver.Chrome(service=obj_service)
    driver2.get('https:www.google.com')
    assert driver2.title =='Google', 'Error2: Title is not valid'
    driver2.quit()
    print('third way: using webdriver manager is finished')


#forth way: Remote launch for docker and Selenium GRID


def test_links():
    print('launch webdriver -> find a element "forget password" using linked text -> click on it -> go to new page')
    driver = webdriver.Chrome()
    driver.get('https://rahulshettyacademy.com/client/')
    assert driver.title=="Let's Shop", 'Correct page is not loaded !'
    # find the link , check if it returns 200 when making API call to the URL
    link = driver.find_element(By.LINK_TEXT,'Forgot password?')
    response = requests.get(link.get_attribute('href'))
    assert response.status_code == 200 , 'link is broken !'
    link.click()
    # to find a xpath from a form 
    driver.find_element(By.XPATH,'//form/div[1]/input').send_keys('test@test.com')
    driver.find_element(By.XPATH, "//input[@id='userPassword']").send_keys("Test@1234")
    driver.find_element(By.XPATH, "//input[@id='confirmPassword']").send_keys("Test@1234")
    driver.find_element(By.XPATH,"//button[contains(text(),'Save New')]").click()
    assert driver.current_url == "https://rahulshettyacademy.com/client/#/auth/password-new", 'Correct page is not loaded !'
    driver.quit()
    print('Basic launch: first way  is finished')

@pytest.mark.skip
def test_find_all_links():
    driver = webdriver.Chrome()
    driver.get('https://naveenautomationlabs.com/opencart/index.php')
    driver.maximize_window()
    list_link = driver.find_elements(By.TAG_NAME,'a')
    print(f'total links available on the page is: {len(list_link)}')
    # check if all links are valid , if there is an invalid link then store it in a list
    valid_links=0
    broken_links=[]
    for link in list_link:
        url= link.get_attribute('href')
        if url.startswith('https'):
            if requests.get(url,timeout=5).status_code==200:
                valid_links = valid_links+1
            else:
                broken_links.append(url)
    print(f'total {valid_links} links are up and running ')


