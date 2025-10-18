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
logging.info("Test: User Login Test")

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Enter 'emilys' in the username field
    username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_field.send_keys("emilys")
except Exception as e:
    logging.error("Error entering username: " + str(e))
    raise

try:
    # Enter 'emilyspass' in the password field
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("emilyspass")
except Exception as e:
    logging.error("Error entering password: " + str(e))
    raise

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
except Exception as e:
    logging.error("Error clicking login button: " + str(e))
    raise

# Verification step
try:
    # Check for successful login (you can adjust this based on your application's behavior)
    user_name_display = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName")))
    actual_user_name = user_name_display.text
    expected_user_name = "emilys"  # Assuming the username is displayed after login
    assert actual_user_name == expected_user_name, f"Expected username '{expected_user_name}', but got '{actual_user_name}'"
except AssertionError as ae:
    logging.error("Login verification failed: " + str(ae))
    raise
except Exception as e:
    logging.error("Error during verification: " + str(e))
    raise

# End of test log
logging.info("Test completed successfully.")
logging.info("========================================")