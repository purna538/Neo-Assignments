from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import time
from selenium.webdriver.common.by import By

# ✅ Get full path to chromedriver.exe in the same folder as the script
current_dir = os.path.dirname(os.path.abspath(__file__))
chrome_driver_path = os.path.join(current_dir, "chromedriver.exe")

# ✅ Print path for debug
print("Using ChromeDriver path:", chrome_driver_path)

# ✅ Set up the service
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# ✅ Open Facebook
driver.get("https://www.facebook.com/")
time.sleep(10)

# ✅ Find the login button by name
try:
    login_button = driver.find_element(By.NAME, "login")
    print("Button by NAME:", login_button.text)
except:
    print("Button by NAME not found.")

# ✅ Find by XPath
try:
    login_xpath = driver.find_element(By.XPATH, "//button[text()='Log in']")
    print("Button by XPath:", login_xpath.text)
except:
    print("Button by XPath not found.")

# ✅ Optional ID (may fail if dynamic)
try:
    button_by_id = driver.find_element(By.ID, "u_0_5")
    print("Button by ID:", button_by_id.text)
except:
    print("Button by ID not found.")

# ✅ Close browser
driver.quit()