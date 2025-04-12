from configs.config import TestData
from pages.home_page import HomePage
from tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_page_title(self):
        self.homePage = HomePage(self.driver)
        login_page = self.homePage.click_to_login()
        title= login_page.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        print('under the login page')
        assert title == TestData.LOGIN_PAGE_TITLE
