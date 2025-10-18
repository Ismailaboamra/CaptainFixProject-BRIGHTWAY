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
test_name = "Login Test with Invalid Credentials"
logging.info(test_name)

# Step 1: Navigate to the login page.
driver.get("http://localhost:8000/")

try:
    # Step 2: Enter 'wronguser' in the username field (#username).
    username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_field.send_keys("wronguser")
except Exception as e:
    logging.error(f"Error entering username: {e}")
    raise

try:
    # Step 3: Enter 'wrongpass' in the password field (#password).
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("wrongpass")
except Exception as e:
    logging.error(f"Error entering password: {e}")
    raise

try:
    # Step 4: Click the login button (#login-submit-btn).
    login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "login-submit-btn")))
    login_button.click()
except Exception as e:
    logging.error(f"Error clicking login button: {e}")
    raise

# Verification step: Check for error message
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    if error_message.is_displayed():
        logging.info("Error message displayed as expected for invalid credentials.")
    else:
        raise AssertionError("Error message not displayed.")
except Exception as e:
    logging.error(f"Error during verification of error message: {e}")
    raise

# End of test log separator
logging.info("End of test")