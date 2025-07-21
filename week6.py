from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Get path to chromedriver in the same folder as this script
current_dir = os.path.dirname(os.path.abspath(__file__))
chrome_driver_path = os.path.join(current_dir, "chromedriver.exe")

# Start the driver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Open Facebook
    driver.get("https://www.facebook.com/")
    wait = WebDriverWait(driver, 10)

    print("\n--- Facebook Login Button Test ---")

    # ✅ Find the button by NAME
    try:
        btn_by_name = wait.until(EC.presence_of_element_located((By.NAME, "login")))
        print("Button by NAME:", btn_by_name.text)
    except:
        print("❌ Button by NAME not found.")

    # ✅ Find the same button by XPath using @name
    try:
        btn_by_xpath = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@name='login']")))
        print("Button by XPath (via name):", btn_by_xpath.text)
    except:
        print("❌ Button by XPath not found.")

    # ❌ Skipping ID-based location (Facebook uses dynamic IDs)
    print("ℹ️ Skipping button by ID because Facebook IDs are dynamic and unreliable.\n")

    time.sleep(2)

finally:
    driver.quit()
