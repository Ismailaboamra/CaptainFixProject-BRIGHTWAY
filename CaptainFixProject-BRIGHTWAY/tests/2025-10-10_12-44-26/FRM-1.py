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
logging.info("Test: User Login Test")

try:
    # Step 1: Navigate to the login page.
    driver.get("http://localhost:8000/")
    
    # Step 2: Enter 'emilys' in the username field.
    try:
        username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys("emilys")
    except Exception as e:
        logging.error("Failed to enter username: " + str(e))
        raise

    # Step 3: Enter 'emilyspass' in the password field.
    try:
        password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys("emilyspass")
    except Exception as e:
        logging.error("Failed to enter password: " + str(e))
        raise

    # Step 4: Click the login button.
    try:
        login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-submit-btn")))
        login_button.click()
    except Exception as e:
        logging.error("Failed to click login button: " + str(e))
        raise

    # Verification: Check if user is logged in successfully.
    try:
        user_name_display = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName")))
        actual_user_name = user_name_display.text
        expected_user_name = "emilys"  # Assuming the username is displayed after login
        assert actual_user_name == expected_user_name, f"Expected username '{expected_user_name}', but got '{actual_user_name}'"
    except AssertionError as ae:
        logging.error("Login verification failed: " + str(ae))
        raise
    except Exception as e:
        logging.error("Failed to verify login: " + str(e))
        raise

except Exception as e:
    logging.error("An error occurred during the test: " + str(e))

# End of the test
logging.info("End of Test")
logging.info("========================================")