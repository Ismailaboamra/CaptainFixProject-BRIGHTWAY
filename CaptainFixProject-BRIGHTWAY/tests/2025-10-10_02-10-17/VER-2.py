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
logging.info("Test: Login and Check Cart Total")

try:
    # Step 1: Open the login page.
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Step 2: Enter 'emilys' in the username field.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
    
    # Step 3: Enter 'emilyspass' in the password field.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
    
    # Step 4: Click the Login button.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
    
    # Handle any alerts after login
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "Login successful"  # Assuming this is the expected alert text
    alert.accept()
    
    # Step 5: Click the Cart button.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "cartBtn"))).click()
    
    # Step 6: Check the total price displayed in the cart.
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    total_price = total_price_element.text
    
    # Assuming we expect the total price to be greater than $0.00 if there are products in the cart
    assert total_price != "$0.00", "Total price should reflect the sum of products in the cart."
    
except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
finally:
    logging.info("End of Test")
    logging.info("===================================")