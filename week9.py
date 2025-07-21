from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import time

# ✅ Set up path to chromedriver
current_dir = os.path.dirname(os.path.abspath(__file__))
chrome_driver_path = os.path.join(current_dir, "chromedriver.exe")
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the page
    driver.get("https://www.flipkart.com/")
    time.sleep(30)  # allow page to load

    # Get the page title
    actual_title = driver.title
    expected_title = "Google"

    # ✅ Use assertion to validate the title
    assert actual_title == expected_title, f"❌ Title mismatch! Expected: '{expected_title}', Got: '{actual_title}'"
    print("✅ Page title validated successfully.")

finally:
    driver.quit()
