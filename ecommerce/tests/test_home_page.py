import pytest
from configs.config import TestData
from pages.home_page import HomePage
from tests.test_base import BaseTest
import allure


class TestHomePage(BaseTest):



    @allure.description("Verify title of the home page is as expected")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.order(1)
    def test_home_page_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE


    @allure.description("Verify the image appearing on the home page, to make sure home page is loaded")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.order(2)
    def test_image(self):
        self.homePage = HomePage(self.driver)
        assert self.homePage.get_home_page_image() , 'Image is not displayed! '


    @allure.description("Verify user successfully add macbook on home screen")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.order(4)
    def test_add_macbook(self):
        self.homePage = HomePage(self.driver)
        assert self.homePage.add_item_without_login() == TestData.CART_TOTAL_1_ITEM

    @allure.description("Verify cart is empty")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.order(3)
    def test_empty_cart(self):
        self.homePage = HomePage(self.driver)
        assert self.homePage.check_cart() == TestData.TEXT_EMPTY_CART, 'Error ! cart is not empty'

    @allure.description("Verify carousel has correct items")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.car
    def test_carousel_horizontal(self):
        self.homePage = HomePage(self.driver)
        items = self.homePage.get_items_in_carousel()
        print(items)
        assert len(items) == 11, 'Error ! Item count is not matching'
        # get the difference between the items list fetched and items in carousel
        assert len(list(set(items)-set(TestData.ITEMS_CAROUSEL))) == 0 , 'Error there is mismatch in the carousel items'



