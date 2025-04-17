from configs.config import TestData
from pages.home_page import HomePage
from tests.test_base import BaseTest
from utils import logger


class TestHomePage(BaseTest):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)  # Important to call the parent's __init__
    #     self.homePage = HomePage(self.driver)  # Initialize here


    def test_home_page_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE
        # self.logger.info('title of home page is verified ')


    def test_image(self):
        self.homePage = HomePage(self.driver)
        assert self.homePage.get_home_page_image() , 'Image is not displayed! '

    # def test_register_account(self):
    #     self.homePage = HomePage(self.driver)
    #     self.homePage.click_my_account()


