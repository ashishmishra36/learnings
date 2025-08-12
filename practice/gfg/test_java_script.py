import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


"""write a fixture which launch the browser"""
@pytest.fixture
def driver():
    # run chrome in headless mode create a object of ChromeOptions class and set the options as headless
    chrome_options= webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("--ignore-certificate-errors")
    # give this option to the driver object when we are launching the chrome
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    yield driver
    driver.quit()


#Tip : window.scrollBy(0,document.body.scrollHeight) - it will find the depth of the page dynamically and go to the bottom
def test_scripts(driver):
    driver.maximize_window()
    driver.get('https://rahulshettyacademy.com/AutomationPractice')
    driver.implicitly_wait(5)
    # now lets scroll to some point and take screenshot
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    # so even the browser is running in headless mode screenshot can be captured
    driver.get_screenshot_as_file("screenshot.png")


def test_table_sorting(driver):
    driver.maximize_window()
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
    we_items= driver.find_elements(By.XPATH,"//tr/td[1]")
    items= []
    for item in we_items:
        items.append(item.text)
    print(f'items: {items}')
    # copy method will just shallow copy(not the nested list,dict) best way if you want to play with original list
    orig_list = items.copy()
    print(f'orig_list: {orig_list}')
    items.sort()
    assert items == orig_list






