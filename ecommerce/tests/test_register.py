from configs.config import TestData
from pages.home_page import HomePage
from tests.test_base import BaseTest
import allure



class TestRegister(BaseTest):

    @allure.description("This test verifies the title of the register page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_page_title(self):
        self.homePage = HomePage(self.driver)
        register_page = self.homePage.click_to_register()
        title= register_page.get_register_page_title(TestData.REGISTER_PAGE_TITLE)
        print('under the register page')
        assert title == TestData.REGISTER_PAGE_TITLE


