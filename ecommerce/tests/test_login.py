from configs.config import TestData
from pages.home_page import HomePage
from tests.test_base import BaseTest
import allure


class TestLogin(BaseTest):

    @allure.description("Verify the title of the login page is as expected")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_page_title(self):
        self.homePage = HomePage(self.driver)
        login_page = self.homePage.click_to_login()
        title= login_page.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        print('under the login page')
        assert title == TestData.LOGIN_PAGE_TITLE
