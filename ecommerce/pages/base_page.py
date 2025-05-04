from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configs.config import TestData
from utils.logger import generate_logger

"""
This class is parent class of the page classes
This will have common operations , which belong to all pages
"""

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        # identify which class (page) a log came from.It will put class name in generating logs for each class
        self.logger = generate_logger(self.__class__.__name__)


    def get_page_title(self, title):
        WebDriverWait(self.driver, 20).until(EC.title_is(title))
        self.logger.info(f'title of the pages is fetched : {title}')
        return self.driver.title

    def get_page_image(self, by_locator):
        self.logger.info(f'fetching image from {by_locator}')
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()

    def do_click(self, by_locator):
        self.logger.info(f'user clicked on {by_locator}')
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        self.logger.info(f'locator is : {by_locator}  and value to be enter is :{text}')
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text_of_element(self, by_locator):
        self.logger.info(f'fetching text of the element locator is : {by_locator}')
        element =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        self.logger.info(f'text of the element is : {element.text}')
        return element.text

    def get_list_of_elements(self, by_locator):
        self.logger.info(f'fetching list of the element for locator : {by_locator}')
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))



