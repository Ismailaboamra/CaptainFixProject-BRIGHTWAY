from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Assuming driver is already defined and passed in
driver.get("https://mawdoo3.com/")

try:
    # Scroll down the homepage
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait for the footer to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
except TimeoutException:
    driver.save_screenshot("footer_not_visible.png")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Navigate to the website
driver.get("https://mawdoo3.com/")

try:
    # Wait for the footer to be visible
    footer = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "footer"))
    )
    print("Footer is visible.")
except Exception as e:
    driver.save_screenshot("footer_not_visible.png")
    print("Footer is not visible.")
    print(e)