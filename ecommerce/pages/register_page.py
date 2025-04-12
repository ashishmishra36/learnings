from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):

    FIRSTNAME = (By.ID, 'input-firstname')
    LASTNAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    PHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input-password')
    CONFIRM_PASSWORD = (By.ID, 'input-confirm')
    SUBSCRIBE = (By.XPATH, "//*[@name='newsletter' and @value=0]")
    POLICY = (By.XPATH, "//*[@name='agree' and @value=1]")
    CONTINUE = (By.CLASS_NAME, 'btn btn-primary')


    def get_register_page_title(self, title):
        return self.get_page_title(title)

    def fill_register_form(self, form_dict):
        field_locators= {
            'first_name' : self.FIRSTNAME,
            'last_name': self.LASTNAME,
            'email': self.EMAIL,
            'phone': self.PHONE,
            'password': self.PASSWORD,
            'confirm_password': self.CONFIRM_PASSWORD,'subscribe': self.SUBSCRIBE, 'policy':self.POLICY,
            'continue':self.CONTINUE
        }
        for field, value in form_dict:
            if field in field_locators:
                if field == 'subscribe':
                    self.do_click(field_locators[field])
                if field == 'policy':
                    self.do_click(field_locators[field])
                if field == 'continue':
                    self.do_click(field_locators[field])
                else:
                    self.do_send_keys(field_locators,value)


