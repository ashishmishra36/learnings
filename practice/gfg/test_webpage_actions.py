import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

"""write a fixture which launch the browser"""
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

"""
this method to fetch static drop-down using select class
"""
def test_static_drop_down(driver):
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    try:
        drop_down_gender = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
        drop_down_gender.select_by_index(0)
        # drop_down_gender.select_by_value('Male')
        drop_down_gender.select_by_visible_text('Male')
        time.sleep(2)
    except NoSuchElementException as er:
        # its cleanest way to generate a failure
        pytest.fail(f'error is {str(er)}')
    finally:
        driver.quit()


"""to test dynamic typed drop down like when we type first 3 chars then drop down comes with a list"""

def test_dyn_drop_down(driver):
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    driver.find_element(By.XPATH, "//input[@id='autosuggest']").send_keys('ind')
    # to give some synchronization
    time.sleep(2)
    countries = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a")
    # find a value matching the given text then break the loop
    for country in countries:
        if country.text == "India":
            country.click()
            break
    # to verify if the value entered is correct or not #IQ
    assert driver.find_element(By.XPATH, "//input[@id='autosuggest']").get_attribute("value")=="India"


"""to select a radio button if it is not selected"""
def test_radio_button(driver):
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    # selecting a radio button: first make sure its not selected then click after the click
    # make sure its selected
    radio_button = driver.find_element(By.XPATH,"//input[@value='radio1']")
    if not radio_button.is_selected():
        radio_button.click()
    assert radio_button.is_selected(), "Error ! radio button is not selected"
    print("radio button is selected")
    # selecting a checkbox: first find if its is not selected then click and later verify if it was clicked
    check_box = driver.find_element(By.XPATH, "//input[@value='option1']")
    if not check_box.is_selected():
        check_box.click()
    assert check_box.is_selected(), "Error ! checkbox button is not selected"
    print("checkbox is selected")


@pytest.mark.skip
def test_show_hide_text(driver):
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    # find the text box check if its displayed - if Yes then click on hide button
    # Later make sure the text box is not displayed
    text_box = driver.find_element(By.XPATH,'//input[@id="displayed-text"]')
    if text_box.is_displayed():
        driver.find_element(By.XPATH, '//input[@id="hide-textbox"]').click()
    assert text_box.is_displayed() == False, "Error ! text_box is still visible ! "


"""to click on alert not a java script pop-up"""
def test_alert(driver):
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.find_element(By.XPATH,"//input[@name='enter-name']").send_keys("Ashish")
    driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
    # switchto method gives you lots of options to swicth
    alert = driver.switch_to.alert
    assert "Ashish" in alert.text
    alert.accept()



