from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import datetime

# Set up logging
log_file = f"./logs/test_log_{datetime.datetime.now().strftime('%Y%m%d')}.log"
logging.basicConfig(filename=log_file, level=logging.INFO)

# Test name
test_name = "Login Test"
logging.info(test_name)

# Step 1: Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Step 2: Enter 'emilys' in the username field
    username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_field.send_keys("emilys")
except Exception as e:
    logging.error(f"Error entering username: {e}")
    raise

try:
    # Step 3: Enter 'emilyspass' in the password field
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("emilyspass")
except Exception as e:
    logging.error(f"Error entering password: {e}")
    raise

try:
    # Step 4: Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
except Exception as e:
    logging.error(f"Error clicking login button: {e}")
    raise

try:
    # Step 5: Check the user name displayed in the navbar
    user_name_displayed = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName")))
    actual_user_name = user_name_displayed.text
    expected_user_name = "emilys"
    assert actual_user_name == expected_user_name, f"Expected user name '{expected_user_name}', but got '{actual_user_name}'"
except Exception as e:
    logging.error(f"Error verifying user name: {e}")
    raise

# End of test log
logging.info("Test completed successfully.")
logging.info("========================================")