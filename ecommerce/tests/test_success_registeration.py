import pytest

from configs.config import TestData
from pages.home_page import HomePage
from tests.test_base import BaseTest
from utils.util_excel import get_registration_data



class TestSuccessRegistration(BaseTest):

    def test_page_title(self):
        self.homePage = HomePage(self.driver)
        register_page = self.homePage.click_to_register()
        registration_data = get_registration_data("C:/Users/AshishMishra/my_data/my_learning/codebase/learnings/ecommerce/configs/data.xlsx", "registration")
        register = register_page.submit_register_form(registration_data)
        print(f'registration page submitted successfully ')
        if register:
            print('under the SUCCESS_REGISTRATION register page')
            title= register.get_success_register_page_title(TestData.SUCCESS_REGISTRATION)
            assert title == TestData.SUCCESS_REGISTRATION
        else:
            assert False, 'title does not match '
