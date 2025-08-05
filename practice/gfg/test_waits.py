import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

"""write a fixture which launch the browser"""
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


"""test : go to the page -> search for veg name -> select all veges -> go to cart match the amount with total 
then apply a discount code -> verify discount is applied 
Why explicit wait : An explicit wait tells Selenium to:
"Wait for a specific condition to occur before proceeding further.
It checks for the condition repeatedly until it's true or the timeout expires. """

def test_cart_test(driver):
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.find_element(By.XPATH, "//input[@type='search']").send_keys('ber')
    # global timeout - implicit wait it will wait max if any web element is found before given wait then driver will move ahead
    driver.implicitly_wait(2)
    # it will blindly wait for 2 sec no matter what is time taken by the element
    time.sleep(2)
    # select all items available after this search with the class
    # still we need to put time.sleep because selenium will move forward even if the list is empty 
    products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
    assert len(products)>0
    # chaining of parent web element
    total_price = 0
    product_added={}
    for product in products:
        product_name = str(product.find_element(By.XPATH, "h4").text)
        product_price =  int(product.find_element(By.XPATH, "p").text)
        product_added[product_name]=product_price
        total_price= total_price + product_price
        print(product.find_element(By.XPATH, "h4").text)
        # print(product.find_element(By.XPATH, "p").text)
        product.find_element(By.XPATH,"div/button").click()
    try:
        # click on the cart
        driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
        # click on the checkout button
        driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
        # Click on the promo code field and enter the promo code
        print("Click on the promo code field and enter the promo code")
        driver.find_element(By.CLASS_NAME,'promoCode').send_keys('rahulshettyacademy')
        # click the promo code apply button
        print("click the promo code apply button")
        driver.find_element(By.CLASS_NAME,"promoBtn").click()
        # verify that "Code applied ..!" text appears when promo code is applied
        """explicit wait will not override the implicit wait """
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
        assert driver.find_element(By.CLASS_NAME, "promoInfo").text == "Code applied ..!", "Error ! text is not found "
        # this code example is to how - how to read table
        # amounts = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
        amounts = driver.find_elements(By.XPATH, "//td[5]/p")
        for amount in amounts:
            print(f'amount of the the item is : {amount.text}')

        # assignment : get the total amount and the discounted amount assert that discounted amount < total amount

        total_amount = driver.find_element(By.XPATH, '//div[@style]/span[1]').text
        discounted_amount = driver.find_element(By.XPATH, '//div[@style]/span[3]').text
        assert discounted_amount<total_amount, f'Error ! discount amount {discounted_amount} can be greater then total amount {total_amount}'


    except Exception as n:
        pytest.fail(f'Error: {str(n)}')

    finally:
        driver.quit()
    print(product_added)