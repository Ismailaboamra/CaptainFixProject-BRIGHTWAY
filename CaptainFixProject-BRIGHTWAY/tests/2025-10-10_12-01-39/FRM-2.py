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
test_name = "Login Test with Empty Username"
logging.info(test_name)

# Step 1: Navigate to the login page
driver.get("http://localhost:8000/")

try:
    # Step 2: Leave the username field empty (#username)
    username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_field.clear()  # Ensure the field is empty

    # Step 3: Enter 'emilyspass' in the password field (#password)
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("emilyspass")

    # Step 4: Click the login button (#login-submit-btn)
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-submit-btn")))
    login_button.click()

    # Verification: Check for error message for empty username (#usernameError)
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    if error_message.is_displayed():
        logging.info("Error message displayed for empty username.")
    else:
        raise AssertionError("Expected error message for empty username not displayed.")

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")

# End of test log separator
logging.info("End of test")