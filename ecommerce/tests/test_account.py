from configs.config import TestData
from pages.home_page import HomePage
from tests.test_base import BaseTest
import allure
import pytest


class TestAccount(BaseTest):

    @allure.description("Verify user lands on login page able to login successfully")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('email, password', [('test3457@test.com', 'Test@2029')])
    def test_account_login(self, email, password):
        self.homePage = HomePage(self.driver)
        login_page = self.homePage.click_to_login()
        title= login_page.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        print('under the login page')
        if title == TestData.LOGIN_PAGE_TITLE:
            account_page =  login_page.enter_login_details(email,password)
            title_account = account_page.get_account_page_title(TestData.ACCOUNT_PAGE_TITLE)
            assert title_account == TestData.ACCOUNT_PAGE_TITLE
        else:
            assert False, 'Error ! unable to land on login page '



