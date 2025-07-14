import os
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager




def test_first_way():
    # Basic launch: first way to launch a browser: use the automatic downloaded chromedriver
    print('Basic launch: first way to launch a browser: use the automatic downloaded chromedriver')
    driver = webdriver.Chrome()
    time.sleep(2)
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    assert driver.title=='ProtoCommerce', 'Correct page is not loaded !'
    # enter the name, password and click on submit
    driver.find_element(By.NAME,'email').send_keys('test@test.com')
    # hint xpath: //tagname[@attribute='value']
    # hint css selector: tagname[attribute='value']
    # driver.find_element(By.XPATH,'//input[@type="password"]').send_keys('2345678')
    driver.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys('2345678')
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    message = driver.find_element(By.CLASS_NAME,'alert-success').text
    assert message == 'Success! The Form has been submitted successfully!.' , 'Error text is not matching !'
    print('-----password entered !')
    driver.quit()
    print('Basic launch: first way  is finished')


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


