from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# ✅ Set up path to chromedriver in the same folder
current_dir = os.path.dirname(os.path.abspath(__file__))
chrome_driver_path = os.path.join(current_dir, "chromedriver.exe")

# ✅ Launch browser
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open Walmart website
    driver.get("https://www.costco.com/")

    # Wait until the search box becomes visible
    wait = WebDriverWait(driver, 30)
    search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-automation-id='search-input']")))

    # Type a search term
    search_box.send_keys("laptop")

    print("✅ Typed 'laptop' into the Walmart search box.")

finally:
    driver.quit()
