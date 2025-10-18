from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import datetime

# Set up logging
log_filename = f"./logs/test_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)

# Test name
logging.info("Test: User Login Test")

try:
    # Step 1: Navigate to the login page.
    driver.get("http://localhost:8000/")
    
    # Step 2: Enter 'emilys' in the username field.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("emilys")
    
    # Step 3: Enter 'emilyspass' in the password field.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("emilyspass")
    
    # Step 4: Click the login button.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-submit-btn")))
    login_button = driver.find_element(By.ID, "login-submit-btn")
    login_button.click()
    
    # Verification: User is logged in and redirected to the shop page.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    assert "shopPage" in driver.page_source, "User is not redirected to the shop page."
    
except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
    raise

finally:
    logging.info("End of Test")
    logging.info("===================================")