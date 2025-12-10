from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.success_registration import SuccessRegistration
from utils.logger import get_logger


class RegisterPage(BasePage):

    FIRSTNAME = (By.ID, 'input-firstname')
    LASTNAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    PHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input-password')
    CONFIRM_PASSWORD = (By.XPATH, "//*[@name='confirm' and @id ='input-confirm']")
    SUBSCRIBE = (By.XPATH, "//*[@name='newsletter' and @value=0]")
    POLICY = (By.XPATH, "//*[@name='agree' and @value=1]")
    CONTINUE = (By.XPATH, "//*[@type='submit']")

    def __init__(self, page):
        super().__init__(page)
        # self.log = get_logger(__name__)


    def submit_register_form(self, form_dict):
        field_locators= {
            'first_name' : self.FIRSTNAME,
            'last_name': self.LASTNAME,
            'email': self.EMAIL,
            'phone': self.PHONE,
            'password': self.PASSWORD,
            'confirm_password': self.CONFIRM_PASSWORD,
            'subscribe': self.SUBSCRIBE,
            'policy':self.POLICY,
            'continue':self.CONTINUE
        }
        for field, value in field_locators.items():
            if field in form_dict:
                self.do_send_keys(field_locators[field], form_dict[field])
            else:
                if field in ['subscribe', 'policy','continue'] :
                    self.do_click(field_locators[field])
                if field == 'confirm_password':
                    self.do_send_keys(field_locators[field], form_dict['password'])
        self.log.info(f'user submitted registration info')
        return SuccessRegistration(self.driver)


