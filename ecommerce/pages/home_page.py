from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class HomePage(BasePage):

    # assign locators as tuple so that we can use it as is at find element method
    IMAGE = (By.XPATH, '//*[@id="slideshow0"]/div/div[4]/a/img')
    MY_ACCOUNT = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a')
    REGISTER = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a')
    LOGIN = (By.XPATH, "//a[contains(@href, 'account/login')]")
    ADD_MACBOOK = (By.XPATH, '//button[contains(@onclick, "cart.add")]')
    BTN_CART = (By.XPATH, '//*[@id="cart"]/button[1]')
    CART_CHK_EMPTY = (By.XPATH, '//*[@id="cart"]/ul/li/p')
    CART_TOTAL = (By.XPATH,'//*[@id="cart-total"]')
    CAROUSEL = (By.XPATH, "//img[contains(@src,'130x100.png') and contains(@class,'img-responsive')]")
    # CAROUSEL = (By.CSS_SELECTOR, ".swiper-wrapper img")


    def get_home_page_title(self, title):
        return self.get_page_title(title)


    def get_home_page_image(self):
        return self.get_page_image(self.IMAGE)


    def click_to_register(self):
        self.do_click(self.MY_ACCOUNT)
        self.do_click(self.REGISTER)
        print('User clicked on Register button under Account dropdown')
        return RegisterPage(self.driver)

    def click_to_login(self):
        self.do_click(self.MY_ACCOUNT)
        self.do_click(self.LOGIN)
        print('User clicked on login button under Account dropdown')
        return LoginPage(self.driver)

    def check_cart(self):
        return self.get_text_of_element(self.CART_TOTAL)


    def add_item_without_login(self):
        self.do_click(self.ADD_MACBOOK)
        print('User added one item')
        return self.get_text_of_element(self.CART_TOTAL)

    def get_items_in_carousel(self):
        l= self.get_list_of_elements(self.CAROUSEL)
        return set([x.get_attribute('alt') for x in l])








