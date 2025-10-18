from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
from datetime import datetime

# Set up logging
log_file_path = './logs/test_log_' + datetime.now().strftime('%Y%m%d_%H%M%S') + '.log'
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
logging.basicConfig(filename=log_file_path, level=logging.INFO)

# Test name
logging.info("Test: User Login Test")

# Step 1: Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Step 2: Enter 'emilys' in the username field
    username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_field.send_keys("emilys")
except Exception as e:
    logging.error("Error entering username: " + str(e))
    raise

try:
    # Step 3: Enter 'emilyspass' in the password field
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("emilyspass")
except Exception as e:
    logging.error("Error entering password: " + str(e))
    raise

try:
    # Step 4: Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
except Exception as e:
    logging.error("Error clicking login button: " + str(e))
    raise

# Verification step
try:
    # Wait for the shop page to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    logging.info("User successfully redirected to the shop page.")
except Exception as e:
    logging.error("User was not redirected to the shop page: " + str(e))
    raise AssertionError("User was not redirected to the shop page.")

# End of test log
logging.info("End of Test")
logging.info("===================================")