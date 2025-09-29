from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("https://mawdoo3.com/")

try:
    facebook_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.facebook.com/mawdoo3']"))
    )
    facebook_link.click()
    
    # Wait for the Facebook page to load
    WebDriverWait(driver, 10).until(
        EC.title_contains("Mawdoo3")
    )
except Exception as e:
    driver.save_screenshot("error_screenshot.png")  # Capture a screenshot if an error occurs
    print(f"An error occurred: {e}")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("https://mawdoo3.com/")

try:
    facebook_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@itemprop='sameAs' and @href='https://www.facebook.com/mawdoo3']"))
    )
    facebook_link.click()

    # Wait for the Facebook page to load
    WebDriverWait(driver, 10).until(
        EC.title_contains("Facebook")
    )
except Exception as e:
    driver.save_screenshot("error_screenshot.png")  # Capture a screenshot if an error occurs
    print(f"An error occurred: {e}")