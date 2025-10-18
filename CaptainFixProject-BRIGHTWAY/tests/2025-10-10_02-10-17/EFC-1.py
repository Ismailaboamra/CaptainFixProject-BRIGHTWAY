from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import datetime

# Set up logging
log_file = f"./logs/test_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(filename=log_file, level=logging.INFO)

# Test name
test_name = "Login Test with Invalid Credentials"
logging.info(test_name)

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Enter 'invalidUser' in the username field
    username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_field.send_keys("invalidUser")
except Exception as e:
    logging.error(f"Error entering username: {str(e)}")
    raise

try:
    # Enter 'wrongPass' in the password field
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("wrongPass")
except Exception as e:
    logging.error(f"Error entering password: {str(e)}")
    raise

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
except Exception as e:
    logging.error(f"Error clicking login button: {str(e)}")
    raise

try:
    # Verify error message displayed for invalid credentials
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    assert error_message.is_displayed(), "Error message is not displayed."
    logging.info("Error message displayed for invalid credentials.")
except AssertionError as ae:
    logging.error(f"Assertion error: {str(ae)}")
    raise
except Exception as e:
    logging.error(f"Error verifying error message: {str(e)}")
    raise

# Separator for log
logging.info("========================================")