from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("https://mawdoo3.com/")

try:
    # Wait for the page to load and check for the presence of the latest articles section
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'متداول')]")))
    print("Successfully navigated to the latest articles page.")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    print("Failed to navigate to the latest articles page:", str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get("https://mawdoo3.com/")
try:
    latest_articles_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "أجدد المقالات"))
    )
    latest_articles_link.click()
except Exception as e:
    driver.save_screenshot("screenshot.png")  # Capture a screenshot if the element is not found or action fails
    print(f"An error occurred: {e}")