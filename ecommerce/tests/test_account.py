import json
from configs.config import TestData
from pages.home_page import HomePage
from tests.base_test import BaseTest
import allure
import pytest


test_data_path = '../test_data/test_account_login.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data['data']



class TestAccount(BaseTest):

    @allure.description("Verify user lands on login page able to login successfully")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('test_data_list', test_list)
    @pytest.mark.skip
    def test_account_login(self, test_data_list):
        self.homePage = HomePage(self.driver)
        login_page = self.homePage.click_to_login()
        title= login_page.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        print('under the login page')
        if title == TestData.LOGIN_PAGE_TITLE:
            account_page =  login_page.enter_login_details(test_data_list['email'],test_data_list['password'])
            title_account = account_page.get_account_page_title(TestData.ACCOUNT_PAGE_TITLE)
            assert title_account == TestData.ACCOUNT_PAGE_TITLE
        else:
            assert False, 'Error ! unable to land on login page '



