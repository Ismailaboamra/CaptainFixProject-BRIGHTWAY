from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("https://mawdoo3.com/")

try:
    # Wait for the title to be correct
    WebDriverWait(driver, 10).until(EC.title_is("موضوع، أكبر موقع عربي بالعالم"))
    
    # Check if the header is visible
    header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "mw-header")))
    
    # If the header is visible, print success message
    print("Header is visible.")
except Exception as e:
    # Capture a screenshot if an error occurs
    driver.save_screenshot("error_screenshot.png")
    print(f"An error occurred: {e}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get("https://mawdoo3.com/")

try:
    WebDriverWait(driver, 10).until(EC.title_contains("موضوع، أكبر موقع عربي بالعالم"))
    header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".mw-header")))
except Exception as e:
    driver.save_screenshot("screenshot.png")  # Capture a screenshot if the title is not correct or header is not visible
    raise e

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
    driver.save_screenshot("screenshot.png")  # Capture a screenshot if an error occurs
    print(f"An error occurred: {e}")