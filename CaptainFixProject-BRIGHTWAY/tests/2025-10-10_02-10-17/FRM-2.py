from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
from datetime import datetime

# Set up logging
log_file_path = './logs/test_log_' + datetime.now().strftime('%Y%m%d_%H%M%S') + '.log'
if not os.path.exists('./logs'):
    os.makedirs('./logs')
logging.basicConfig(filename=log_file_path, level=logging.INFO)

# Test name
test_name = "Login Test - Empty Username"
logging.info(test_name)

# Step 1: Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Step 2: Leave the username field empty
    username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_field.clear()  # Ensure the field is empty

    # Step 3: Enter 'emilyspass' in the password field
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.clear()
    password_field.send_keys('emilyspass')

    # Step 4: Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()

    # Verification: Check for error message displayed for empty username
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    if error_message.is_displayed():
        logging.info("Error message displayed for empty username as expected.")
    else:
        raise AssertionError("Expected error message for empty username was not displayed.")

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")

finally:
    logging.info("End of test.")
    logging.info("===================================")