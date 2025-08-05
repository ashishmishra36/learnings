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
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_mouse(driver):
    driver.maximize_window()
    driver.get('https://rahulshettyacademy.com/AutomationPractice')
    driver.implicitly_wait(5)
    """Action class is used for mouse operations, create object of Action chains """
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.CSS_SELECTOR, "button[id='mousehover']")).perform()
    action.click(driver.find_element(By.LINK_TEXT,"Top")).perform()


def test_child_window(driver):
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/windows')
    driver.find_element(By.LINK_TEXT,'Click Here').click()
    # get all open tabs/windows
    windows = driver.window_handles
    print(windows)
    driver.switch_to.window(windows[1])
    print(driver.find_element(By.TAG_NAME,'h3').text)


def test_assignment(driver):
    driver.maximize_window()
    driver.get('https://rahulshettyacademy.com/loginpagePractise/')
    driver.implicitly_wait(5)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Free Access').click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    para = driver.find_elements(By.XPATH,"//div[@class='col-md-8']/p")
    t = para[1].text
    p = '[\w\.-]+@[\w\.-]+\.\w+'
    match = re.search(p,t)
    email = match.group()
    driver.switch_to.window(windows[0])
    # now enter the credentials in login page
    driver.find_element(By.XPATH,"//input[@id='username']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys('testingPassword')
    driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()
    alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger"))
    )
    print(alert.text)
