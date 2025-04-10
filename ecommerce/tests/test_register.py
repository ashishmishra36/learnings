from configs.config import TestData
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from tests.test_base import BaseTest


class TestRegister(BaseTest):

    def test_page_title(self):
        self.homePage = HomePage(self.driver)
        register_page = self.homePage.click_my_account()
        title= register_page.get_register_page_title(TestData.REGISTER_PAGE_TITLE)
        print('under the register page')
        assert title == TestData.REGISTER_PAGE_TITLE
