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
logging.info("Test: Search for a product after login")

try:
    # Step 1: Navigate to the login page.
    driver.get("http://localhost:8000/")

    # Step 2: Enter 'emilys' in the username field.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("emilys")

    # Step 3: Enter 'emilyspass' in the password field.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("emilyspass")

    # Step 4: Click the login button.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-submit-btn")))
    login_button = driver.find_element(By.ID, "login-submit-btn")
    login_button.click()

    # Step 5: Click the search button.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchBtn")))
    search_button = driver.find_element(By.ID, "searchBtn")
    search_button.click()

    # Step 6: Enter 'laptop' in the search input.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchInput")))
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.send_keys("laptop")

    # Step 7: Click the search button.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchBtn")))
    search_button = driver.find_element(By.ID, "searchBtn")
    search_button.click()

    # Verification: Check if search results for 'laptop' are displayed.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchResultsInfo")))
    search_results_info = driver.find_element(By.ID, "searchResultsInfo").text

    if "laptop" not in search_results_info.lower():
        raise AssertionError("Expected search results for 'laptop' are not displayed.")

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
finally:
    logging.info("End of test")
    logging.info("===================================")