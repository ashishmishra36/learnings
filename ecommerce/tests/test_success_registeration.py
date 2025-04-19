from configs.config import TestData
from pages.home_page import HomePage
from tests.test_base import BaseTest
from utils.util_excel import fetch_registration_data, update_row_in_sheet


class TestSuccessRegistration(BaseTest):

    def test_success_registration_title(self):
        self.homePage = HomePage(self.driver)
        register_page = self.homePage.click_to_register()
        registration_data = fetch_registration_data(TestData.EXCEL_SHEET_PATH, TestData.SHEET_NAME)
        register = register_page.submit_register_form(registration_data)
        print(f'registration page submitted successfully ')
        if register:
            print('under the SUCCESS_REGISTRATION register page')
            title= register.get_success_register_page_title(TestData.SUCCESS_REGISTRATION)
            assert title == TestData.SUCCESS_REGISTRATION
            update_row_in_sheet(TestData.EXCEL_SHEET_PATH, TestData.SHEET_NAME, registration_data)
        else:
            assert False, 'Failed to fill registration form! '
