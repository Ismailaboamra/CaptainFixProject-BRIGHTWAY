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
logging.info("Test: Search for a product after logging in")

try:
    # Step 1: Navigate to the login page.
    driver.get("http://localhost:8000/")
    
    # Step 2: Enter 'emilys' in the username field (#username).
    try:
        username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys("emilys")
    except Exception as e:
        logging.error("Failed to enter username: " + str(e))
        raise

    # Step 3: Enter 'emilyspass' in the password field (#password).
    try:
        password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys("emilyspass")
    except Exception as e:
        logging.error("Failed to enter password: " + str(e))
        raise

    # Step 4: Click the login button (#login-submit-btn).
    try:
        login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "login-submit-btn")))
        login_button.click()
    except Exception as e:
        logging.error("Failed to click login button: " + str(e))
        raise

    # Step 5: Enter 'laptop' in the search input (#searchInput).
    try:
        search_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchInput")))
        search_input.send_keys("laptop")
    except Exception as e:
        logging.error("Failed to enter search term: " + str(e))
        raise

    # Step 6: Click the search button (#searchBtn).
    try:
        search_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchBtn")))
        search_button.click()
    except Exception as e:
        logging.error("Failed to click search button: " + str(e))
        raise

    # Verification: Check if search results for 'laptop' are displayed in the products list (#productsList).
    try:
        products_list = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
        assert products_list.is_displayed(), "Search results are not displayed."
        logging.info("Search results for 'laptop' are displayed successfully.")
    except AssertionError as ae:
        logging.error("Verification failed: " + str(ae))
        raise
    except Exception as e:
        logging.error("Failed to verify search results: " + str(e))
        raise

except Exception as e:
    logging.error("Test failed: " + str(e))

logging.info("End of test")
logging.info("========================================")