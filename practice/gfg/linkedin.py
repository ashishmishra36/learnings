from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_driver(headless=False):
    """Create and configure a Chrome WebDriver instance."""
    options = Options()
    options.add_argument("--start-maximized")
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)  # Default wait for all elements
    return driver


def login(driver, username, password):
    """Generic login function for testing."""
    driver.get("https://www.linkedin.com/login")

    # Wait until fields are visible instead of fixed sleeps
    wait = WebDriverWait(driver, 10)
    email_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    email_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()


def edit_about_section(driver, profile_url):
    """Generic profile edit function for testing demo purposes."""
    driver.get(profile_url)
    wait = WebDriverWait(driver, 10)

    about_section = wait.until(
        EC.element_to_be_clickable((By.ID, "profile-card-name text-heading-large"))
    )
    about_section.click()
    # driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", about_section)
    field = wait.until(EC.element_to_be_clickable((By.ID, "navigation-add-edit-deeplink-edit-about")))
    field.click()

    textarea = wait.until(
        EC.presence_of_element_located((By.XPATH, "//textarea[contains(@id, 'summary')]"))
    )

    current_text = textarea.get_attribute("value") or ""
    textarea.clear()
    textarea.send_keys(current_text.strip() + " ")

    save_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Save')]"))
    )
    save_button.click()


def main():
    # Do not include credentials in code — load from env or config in real use
    USERNAME = "ashish.mishra36@gmail.com"
    PASSWORD = "Ashish@2015"
    PROFILE_URL = "https://www.linkedin.com/in/mishra36/"

    driver = create_driver()
    try:
        login(driver, USERNAME, PASSWORD)
        edit_about_section(driver, PROFILE_URL)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
