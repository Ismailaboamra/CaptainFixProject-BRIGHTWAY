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
test_name = "Login Test for Empty Password"
logging.info(test_name)

# Step 1: Navigate to the login page.
driver.get("http://localhost:8000/")

try:
    # Step 2: Enter 'emilys' in the username field.
    username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_field.send_keys("emilys")
except Exception as e:
    logging.error(f"Error entering username: {e}")
    raise

try:
    # Step 3: Leave the password field empty.
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    # Intentionally not filling the password field
except Exception as e:
    logging.error(f"Error locating password field: {e}")
    raise

try:
    # Step 4: Click the login button.
    login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "login-submit-btn")))
    login_button.click()
except Exception as e:
    logging.error(f"Error clicking login button: {e}")
    raise

try:
    # Verification: Check for error message displayed for empty password.
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    if error_message.is_displayed():
        logging.info("Error message displayed for empty password as expected.")
    else:
        raise AssertionError("Error message for empty password not displayed.")
except Exception as e:
    logging.error(f"Error during verification of error message: {e}")
    raise

# End of test log
logging.info("End of test")
logging.info("=" * 50)