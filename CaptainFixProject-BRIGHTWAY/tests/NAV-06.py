from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Assuming driver is already created and passed in
driver.get("https://mawdoo3.com/")

try:
    # Wait for the page to load and the element to be clickable
    contact_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "اتصل بنا"))
    )
    contact_link.click()

    # Wait for the contact page to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'اتصل بنا')]"))
    )
except Exception as e:
    driver.save_screenshot("error_screenshot.png")  # Capture a screenshot if an error occurs
    print(f"An error occurred: {e}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Navigate to the website
driver.get("https://mawdoo3.com/")

try:
    # Wait for the contact link to be visible and click it
    contact_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "اتصل بنا"))
    )
    contact_link.click()

    # Wait for the contact page to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'اتصل بنا')]"))
    )
    
    print("Contact page is displayed.")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    print("An error occurred:", e)