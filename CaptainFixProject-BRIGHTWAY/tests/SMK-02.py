from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Assuming driver is already defined and passed in
driver.get("https://mawdoo3.com/")

try:
    # Scroll down the homepage
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait for the footer to be visible
    footer = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "footer"))
    )
    
    # Optionally, you can take a screenshot if needed
    driver.save_screenshot("footer_visible.png")

except Exception as e:
    # Capture a screenshot if an error occurs
    driver.save_screenshot("error_screenshot.png")
    print(f"An error occurred: {e}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the website
driver.get("https://mawdoo3.com/")

try:
    # Wait for the footer to be visible
    footer = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer"))
    )
    print("Footer is visible.")
except Exception as e:
    driver.save_screenshot("footer_visibility_error.png")
    print("Footer is not visible.")
    print(e)