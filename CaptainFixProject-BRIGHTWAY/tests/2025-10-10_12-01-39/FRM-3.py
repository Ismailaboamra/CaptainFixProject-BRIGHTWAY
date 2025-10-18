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
test_name = "Login Test with Empty Password"
logging.info(test_name)

try:
    # Step 1: Navigate to the login page.
    driver.get("http://localhost:8000/")
    
    # Step 2: Enter 'emilys' in the username field (#username).
    try:
        username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys("emilys")
    except Exception as e:
        logging.error(f"Error entering username: {e}")
        raise

    # Step 3: Leave the password field empty (#password).
    try:
        password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
        # Intentionally leaving this field empty
    except Exception as e:
        logging.error(f"Error locating password field: {e}")
        raise

    # Step 4: Click the login button (#login-submit-btn).
    try:
        login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "login-submit-btn")))
        login_button.click()
    except Exception as e:
        logging.error(f"Error clicking login button: {e}")
        raise

    # Verification: Check for error message for empty password (#passwordError).
    try:
        error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
        if error_message.is_displayed():
            logging.info("Error message displayed as expected.")
        else:
            raise AssertionError("Error message not displayed.")
    except Exception as e:
        logging.error(f"Error verifying error message: {e}")
        raise

except Exception as e:
    logging.error(f"Test failed: {e}")

finally:
    logging.info("End of test.")
    logging.info("===================================")