from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(), options=options)


def login_linkedin(username, password):
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)  # Allow time for the page to load
    # sign_in_button = driver.find_element((By.XPATH, '//*[@id="main-content"]/section[1]/div/div/a'))
    # sign_in_button.click()
    time.sleep(2)  # Allow time for the page to load

    email_field = driver.find_element(By.XPATH, '//*[@id="username"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    email_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    time.sleep(5)  # Allow time for login to complete


def edit_about_section():
    driver.get("https://www.linkedin.com/in/ashishm-test-analyst/")
    time.sleep(5)  # Allow profile to load

    # Scroll down to the About section
    about_section = driver.find_element(By.XPATH,
                                        '//*[@id="navigation-add-edit-deeplink-edit-about"]')
    driver.execute_script("arguments[0].scrollIntoView();", about_section)
    time.sleep(2)
    about_section.click()
    time.sleep(3)  # Wait for the pop-up to appear

    # Find the text area in the About section
    about_textarea = driver.find_element(By.XPATH, '//*[@id="gai-text-form-component-profileEditFormElement-SUMMARY-profile-ACoAAARGzBcBDBkxiw97L1FZyomSt45la7ll5io-summary"]')
    current_text = about_textarea.get_attribute("value")

    # Add an extra space at the end
    about_textarea.clear()
    about_textarea.send_keys(current_text + " ")
    time.sleep(2)

    # Click on Save button
    save_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Save')]")
    save_button.click()
    time.sleep(5)


if __name__ == "__main__":
    USERNAME = "ashish.mishra36@gmail.com"  # Replace with your LinkedIn email
    PASSWORD = "Ashish@2015"  # Replace with your LinkedIn password

    login_linkedin(USERNAME, PASSWORD)
    edit_about_section()
    driver.quit()
