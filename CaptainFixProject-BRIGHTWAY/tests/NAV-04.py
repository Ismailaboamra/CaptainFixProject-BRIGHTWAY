from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Assuming 'driver' is already defined and passed in
driver.get("https://mawdoo3.com/")

try:
    # Wait for the page to load and the element to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'معاييرنا_للتدقيق')]")))
    # Click on the link to open the quality standards page
    driver.find_element(By.XPATH, "//a[contains(@href, 'معاييرنا_للتدقيق')]").click()
    
    # Wait for the quality standards page to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'معايير التدقيق')]")))
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")  # Capture a screenshot if an error occurs
    print(f"An error occurred: {e}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("https://mawdoo3.com/")

try:
    # Wait for the quality standards page link to be visible and click it
    quality_standards_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "معايير التدقيق"))
    )
    quality_standards_link.click()

    # Wait for the quality standards page to be displayed
    WebDriverWait(driver, 10).until(
        EC.title_contains("معايير التدقيق")
    )
except Exception as e:
    driver.save_screenshot("error_screenshot.png")  # Capture a screenshot if an error occurs
    print(f"An error occurred: {e}")