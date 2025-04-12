from configs.config import TestData
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class HomePage(BasePage):


    IMAGE = (By.XPATH, '//*[@id="slideshow0"]/div/div[4]/a/img')
    MY_ACCOUNT = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a')
    REGISTER = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a')

# super keyword : it will call the parent class constructor, with help of this driver we can invoke generic method
# created in the BasePage
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    def get_home_page_title(self, title):
        return self.get_page_title(title)


    def get_home_page_image(self):
        return self.get_page_image(self.IMAGE)


    def click_to_register(self):
        self.do_click(self.MY_ACCOUNT)
        self.do_click(self.REGISTER)
        return RegisterPage(self.driver)

    def click_to_login(self):
        self.do_click(self.MY_ACCOUNT)
        self.do_click(self.REGISTER)
        return LoginPage(self.driver)



