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
test_name = "Login Test for Fix-Shop"
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

    # Step 3: Enter 'emilyspass' in the password field (#password).
    try:
        password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys("emilyspass")
    except Exception as e:
        logging.error(f"Error entering password: {e}")
        raise

    # Step 4: Click the login button (#login-submit-btn).
    try:
        login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-submit-btn")))
        login_button.click()
    except Exception as e:
        logging.error(f"Error clicking login button: {e}")
        raise

    # Step 5: Click the login button again rapidly (#login-submit-btn).
    try:
        login_button.click()
    except Exception as e:
        logging.error(f"Error clicking login button again: {e}")
        raise

    # Verification step: Check for duplicate login requests
    try:
        # Assuming that a successful login redirects to the shop page
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
        logging.info("Login successful, shop page loaded.")
    except Exception as e:
        logging.error(f"Login failed or shop page did not load: {e}")
        raise

    # Check for any alerts or errors
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        logging.info(f"Alert detected: {alert_text}")
    except Exception:
        logging.info("No alert detected.")

    # Check for inline errors
    try:
        username_error = driver.find_element(By.ID, "usernameError").text
        password_error = driver.find_element(By.ID, "passwordError").text
        if username_error or password_error:
            raise AssertionError(f"Inline errors detected: {username_error}, {password_error}")
    except Exception:
        logging.info("No inline errors detected.")

except Exception as e:
    logging.error(f"Test failed: {e}")

finally:
    logging.info("End of test.")
    logging.info("===================================")