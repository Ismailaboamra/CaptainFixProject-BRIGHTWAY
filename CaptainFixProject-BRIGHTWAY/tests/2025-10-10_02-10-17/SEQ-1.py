from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import datetime

# Set up logging
log_filename = f"./logs/test_log_{datetime.datetime.now().strftime('%Y%m%d')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)

# Start of the test
logging.info("Test: User Login and Checkout Process")

try:
    # Step 1: Open the login page.
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Step 2: Enter 'emilys' in the username field.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
    
    # Step 3: Enter 'emilyspass' in the password field.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
    
    # Step 4: Click the Login button.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
    
    # Step 5: Click the Cart button.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "cartBtn"))).click()
    
    # Step 6: Click the Proceed to Checkout button.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary.btn-checkout"))).click()
    
    # Verification: Check if user is redirected to the checkout page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    assert "Your Cart" in driver.page_source, "User is not redirected to the checkout page."

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
    raise

finally:
    logging.info("End of test.")
    logging.info("===================================")