import pytest

from configs.config import TestData
from pages.home_page import HomePage
from tests.base_test import BaseTest
import allure


class TestLogin(BaseTest):

    # add custom markers in the pytest.ini file
    @allure.description("Verify the title of the login page is as expected")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_login_page_title(self):
        self.homePage = HomePage(self.driver)
        login_page = self.homePage.click_to_login()
        # title = login_page.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        title = login_page.get_page_title(TestData.LOGIN_PAGE_TITLE)

        print('under the login page')
        assert title == TestData.LOGIN_PAGE_TITLE , 'Error! Login page title is not matching'
