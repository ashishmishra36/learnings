from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):



    def get_login_page_title(self, title):
        return self.get_page_title(title)


    def fill_the_


