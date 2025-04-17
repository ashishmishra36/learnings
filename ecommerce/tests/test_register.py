from configs.config import TestData
from pages.home_page import HomePage
from tests.test_base import BaseTest



class TestRegister(BaseTest):

    def test_page_title(self):
        self.homePage = HomePage(self.driver)
        register_page = self.homePage.click_to_register()
        title= register_page.get_register_page_title(TestData.REGISTER_PAGE_TITLE)
        print('under the register page')
        assert title == TestData.REGISTER_PAGE_TITLE

    # def test_submit_register_page(self):
    #     self.homePage = HomePage(self.driver)
    #     register_page = self.homePage.click_to_register()
    #     register_page.submit_register_form()


