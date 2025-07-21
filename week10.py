from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

# ✅ Page Object class for the Login Page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.facebook.com/"
        self.username_input = (By.ID, "email")
        self.password_input = (By.ID, "pass")
        self.login_button = (By.NAME, "login")

    def load(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

# ✅ Main test script using the Page Object
if __name__ == "__main__":
    # Set path to chromedriver
    current_dir = os.path.dirname(os.path.abspath(__file__))
    chrome_driver_path = os.path.join(current_dir, "chromedriver.exe")

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)

    try:
        # Use the Page Object
        login_page = LoginPage(driver)
        login_page.load()

        time.sleep(1)  # wait for page to load

        # Fill the form (use dummy credentials for testing)
        login_page.enter_username("testuser@example.com")
        login_page.enter_password("fakepassword")
        login_page.click_login()

        time.sleep(30)  # wait to observe

        print("✅ Login flow executed using Page Object.")

    finally:
        driver.quit()
