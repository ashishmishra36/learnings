from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configs.config import TestData

"""
This class is parent class of the page classes
This will have common operations , which belong to all pages
"""

class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def get_page_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_page_image(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)


