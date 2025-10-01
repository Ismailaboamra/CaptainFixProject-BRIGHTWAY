from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("https://mawdoo3.com/")

try:
    # Wait for the title to be correct
    WebDriverWait(driver, 10).until(EC.title_is("موضوع، أكبر موقع عربي بالعالم"))
    
    # Check if the header is displayed
    header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "mw-header")))
    
    # If the header is displayed, print success message
    print("Header is displayed.")
except Exception as e:
    # Capture a screenshot if an error occurs
    driver.save_screenshot("error_screenshot.png")
    print(f"An error occurred: {e}")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Assuming driver is already created and passed in
driver.get("https://mawdoo3.com/")

try:
    # Wait for the title to be present and verify it
    WebDriverWait(driver, 10).until(EC.title_is("موضوع، أكبر موقع عربي بالعالم"))
    print("Title is correct.")
except Exception as e:
    driver.save_screenshot("screenshot.png")
    print("Title is incorrect or not found.")
    print(e)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Navigate to the website
driver.get("https://mawdoo3.com/")

try:
    # Wait for the header to be visible
    header = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "mw-header"))
    )
    
    # Check the title
    assert "موضوع، أكبر موقع عربي بالعالم" in driver.title

except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    print(f"An error occurred: {e}")