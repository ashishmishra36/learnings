from configs.config import TestData
from pages.home_page import HomePage
from tests.test_base import BaseTest
import allure


class TestHomePage(BaseTest):


    @allure.description("Verify title of the home page is as expected")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_home_page_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE


    @allure.description("Verify the image appearing on the home page, to make sure home page is loaded")
    @allure.severity(allure.severity_level.NORMAL)
    def test_image(self):
        self.homePage = HomePage(self.driver)
        assert self.homePage.get_home_page_image() , 'Image is not displayed! '



