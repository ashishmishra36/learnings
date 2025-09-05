import pytest
from configs.config import TestData
from pages.home_page import HomePage
from tests.base_test import BaseTest
from utils.util_excel import fetch_registration_data, update_row_in_sheet
import allure


class TestSuccessRegistration(BaseTest):

    @allure.description("Verify that user is able to register successfully and lands on success page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skip(reason="Test is under development")
    def test_success_registration_title(self):
        self.homePage = HomePage(self.driver)
        register_page = self.homePage.click_to_register()
        registration_data = fetch_registration_data(TestData.EXCEL_SHEET, TestData.SHEET_NAME)
        if registration_data:
            register = register_page.submit_register_form(registration_data)
            print(f'registration page submitted successfully ')
            if register:
                print('under the SUCCESS_REGISTRATION register page')
                title= register.get_page_title(TestData.SUCCESS_REGISTRATION)
                assert title == TestData.SUCCESS_REGISTRATION
                update_row_in_sheet(TestData.EXCEL_SHEET, TestData.SHEET_NAME, registration_data)
                print(registration_data)
            else:
                assert False, 'Failed to fill registration form! '
        else:
            assert False, 'Failed to get a valid registration data ! '
