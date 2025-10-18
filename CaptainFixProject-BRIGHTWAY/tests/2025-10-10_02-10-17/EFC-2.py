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
logging.info("Test: Login Functionality")

try:
    # Step 1: Open the login page.
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Step 2: Enter 'emilys' in the username field.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
    
    # Step 3: Enter 'emilyspass' in the password field.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
    
    # Step 4: Click the Login button.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
    
    # Step 5: Click the Login button again rapidly.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
    
    # Verification: Check for any error messages or alerts
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        assert alert_text == "Expected alert message", f"Unexpected alert message: {alert_text}"
        alert.accept()
    except:
        pass  # No alert present

    # Check for inline errors
    username_error = driver.find_element(By.ID, "usernameError").text
    password_error = driver.find_element(By.ID, "passwordError").text
    assert username_error == "", f"Username error displayed: {username_error}"
    assert password_error == "", f"Password error displayed: {password_error}"

    # Check for duplicate login attempts
    user_name_displayed = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName"))).text
    assert user_name_displayed == "emilys", "User should be logged in without duplicate attempts."

except Exception as e:
    logging.error(f"Test failed: {str(e)}")

finally:
    logging.info("End of Test")
    logging.info("===================================")