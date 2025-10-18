from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import datetime

# Set up logging
log_filename = f"./logs/test_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)

# Start of the test
logging.info("Test: Login and Select Category")

try:
    # Step 1: Navigate to the login page.
    driver.get("http://localhost:8000/")
    
    # Step 2: Enter 'emilys' in the username field (#username).
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
    
    # Step 3: Enter 'emilyspass' in the password field (#password).
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
    
    # Step 4: Click the login button (#login-submit-btn).
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-submit-btn"))).click()
    
    # Handle any alerts after login
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "Login successful", f"Expected alert text 'Login successful' but got '{alert_text}'"
    alert.accept()
    
    # Step 5: Select a category from the category filter (#categoryFilter).
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "categoryFilter"))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@id='categoryFilter']/option[1]"))).click()  # Selecting the first option as an example
    
    # Verification: Check if products in the selected category are displayed in the products list (#productsList).
    products_list = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    assert products_list.is_displayed(), "Expected products list is not displayed."
    
except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
    raise

finally:
    logging.info("End of test")
    logging.info("========================================")