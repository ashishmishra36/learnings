from pages.account_page import AccountPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from utils.logger import get_logger


class LoginPage(BasePage):
    EMAIL = (By.ID, 'input-email')
    PASSWORD = (By.ID, 'input-password')
    BTN_LOGIN = (By.XPATH, "//input[@type='submit']")

    def __init__(self, page):
        super().__init__(page)
        # self.log = get_logger(__name__)


    def enter_login_details(self, email, password):
        self.do_send_keys(self.EMAIL,email)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.BTN_LOGIN)
        return AccountPage(self.driver)




