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
test_name = "Login Test for Empty Password"
logging.info(test_name)

# Step 1: Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Step 2: Enter 'emilys' in the username field
    username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_field.send_keys("emilys")
except Exception as e:
    logging.error("Failed to enter username: " + str(e))

try:
    # Step 3: Leave the password field empty
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    # Intentionally not filling the password field
except Exception as e:
    logging.error("Failed to locate password field: " + str(e))

try:
    # Step 4: Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
except Exception as e:
    logging.error("Failed to click login button: " + str(e))

try:
    # Verification: Check for error message displayed for empty password
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    if error_message.is_displayed():
        logging.info("Error message displayed for empty password as expected.")
    else:
        raise AssertionError("Error message not displayed for empty password.")
except Exception as e:
    logging.error("Error message verification failed: " + str(e))

# End of test log
logging.info("End of test")
logging.info("========================================")