from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("https://mawdoo3.com/")

try:
    # Wait for the categories section to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".all-categories")))
    print("Successfully navigated to the categories page.")
except Exception as e:
    driver.save_screenshot("screenshot.png")
    print("Failed to navigate to the categories page:", e)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Assuming driver is already defined and passed in
driver.get("https://mawdoo3.com/")

try:
    # Wait for the 'التصنيفات' link to be clickable and then click it
    categories_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "التصنيفات"))
    )
    categories_link.click()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")  # Capture a screenshot if an error occurs
    print(f"An error occurred: {e}")