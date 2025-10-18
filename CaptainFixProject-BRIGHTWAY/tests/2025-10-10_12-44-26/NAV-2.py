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
logging.info("Test: User Login and Logout")

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
    
    # Detect any errors after login
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    
    # Step 5: Click the logout button.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "logoutBtn")))
    logout_button = driver.find_element(By.ID, "logoutBtn")
    logout_button.click()
    
    # Verify user is logged out and redirected to the login page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    assert "loginPage" in driver.page_source, "User is not redirected to the login page after logout."
    
except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
    raise AssertionError(f"Test failed due to an error: {str(e)}")

finally:
    logging.info("End of Test")
    logging.info("========================================")