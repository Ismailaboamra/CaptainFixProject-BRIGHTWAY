from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("https://mawdoo3.com/")

try:
    about_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "عن موضوع"))
    )
    about_link.click()

    # Wait for the About page to load and check if it's visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'أهلاً بك في موضوع')]"))
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

# Click on the "عن موضوع" link to navigate to the about page
try:
    about_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "عن موضوع"))
    )
    about_link.click()
    
    # Wait for the about page to load and verify it's displayed
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'عن موضوع')]"))
    )
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")  # Capture a screenshot if an error occurs
    print(f"An error occurred: {e}")