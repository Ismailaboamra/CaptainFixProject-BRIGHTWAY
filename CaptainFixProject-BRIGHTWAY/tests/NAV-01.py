from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Assuming driver is already created and passed in
driver.get("https://mawdoo3.com/")

try:
    # Wait for the categories section to be visible
    categories_section = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'all-categories')]"))
    )
    print("Categories section is visible.")
except Exception as e:
    driver.save_screenshot("screenshot.png")
    print("Categories section is not visible.")
    print(e)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Navigate to the website
driver.get("https://mawdoo3.com/")

try:
    # Wait for the categories section to be visible
    categories_section = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".all-categories"))
    )
    print("Categories section is displayed.")
except Exception as e:
    driver.save_screenshot("categories_section_not_found.png")
    print("Categories section is not displayed.")
    print(e)