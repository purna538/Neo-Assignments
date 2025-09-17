import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
    elif request.param == "firefox":
        firefox_options = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(), options=firefox_options)
    else:
        raise ValueError("Unsupported browser!")

    yield driver
    driver.quit()

def test_google_title(browser):
    browser.get("https://www.google.com")
    time.sleep(5)  # Just to visually see it's working
    assert "Google" in browser.title
