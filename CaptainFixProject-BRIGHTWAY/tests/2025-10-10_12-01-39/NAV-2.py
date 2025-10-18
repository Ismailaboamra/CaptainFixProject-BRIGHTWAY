from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import datetime

# Set up logging
log_filename = f"./logs/test_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)

try:
    logging.info("Test: User Login and Logout")

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

    # Step 5: Click the logout button (#logoutBtn).
    try:
        logout_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "logoutBtn")))
        logout_button.click()
    except Exception as e:
        logging.error(f"Error clicking logout button: {e}")
        raise

    # Verification: User is redirected back to the login page.
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm")))
        logging.info("User is successfully redirected back to the login page.")
    except Exception as e:
        logging.error(f"User is not redirected back to the login page: {e}")
        raise AssertionError("User is not redirected back to the login page.")

except Exception as e:
    logging.error(f"Test failed: {e}")

finally:
    logging.info("End of test.")
    logging.info("========================================")