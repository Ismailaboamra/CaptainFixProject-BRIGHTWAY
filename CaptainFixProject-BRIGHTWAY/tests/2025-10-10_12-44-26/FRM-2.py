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
test_name = "Login Test - Empty Username"
logging.info(test_name)

# Step 1: Navigate to the login page.
driver.get("http://localhost:8000/")

try:
    # Step 2: Leave the username field empty.
    username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_field.clear()  # Ensure the field is empty
except Exception as e:
    logging.error(f"Error interacting with username field: {e}")
    raise

try:
    # Step 3: Enter 'emilyspass' in the password field.
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.clear()  # Clear any existing text
    password_field.send_keys("emilyspass")
except Exception as e:
    logging.error(f"Error interacting with password field: {e}")
    raise

try:
    # Step 4: Click the login button.
    login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "login-submit-btn")))
    login_button.click()
except Exception as e:
    logging.error(f"Error clicking login button: {e}")
    raise

# Verification step: Check for error message displayed for empty username.
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    if error_message.is_displayed():
        logging.info("Error message displayed for empty username as expected.")
    else:
        raise AssertionError("Error message for empty username not displayed.")
except Exception as e:
    logging.error(f"Error during verification of error message: {e}")
    raise

# End of test log separator
logging.info("End of test")