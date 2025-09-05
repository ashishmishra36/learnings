from pages.account_page import AccountPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    EMAIL = (By.ID, 'input-email')
    PASSWORD = (By.ID, 'input-password')
    BTN_LOGIN = (By.XPATH, "//input[@type='submit']")


    def enter_login_details(self, email, password):
        self.do_send_keys(self.EMAIL,email)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.BTN_LOGIN)
        return AccountPage(self.driver)




