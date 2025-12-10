import pytest

from configs.config import TestData
from pages.home_page import HomePage
from tests.base_test import BaseTest
import allure

from utils.logger import get_logger


class TestRegister(BaseTest):
    log = get_logger(__name__)

    @allure.description("Verify the title of the register page is as expected")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_register_page_title(self):
        self.log.info('Test: Verify the title of the register page is as expected')
        self.homePage = HomePage(self.driver)
        register_page = self.homePage.click_to_register()
        title= register_page.get_page_title(TestData.REGISTER_PAGE_TITLE)
        self.log.info('under the register page')
        assert title == TestData.REGISTER_PAGE_TITLE


