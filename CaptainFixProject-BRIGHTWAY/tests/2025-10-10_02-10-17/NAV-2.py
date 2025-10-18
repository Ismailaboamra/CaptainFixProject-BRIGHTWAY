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
logging.info("Test: User Login and Navigation to Shop Page")

try:
    # Step 1: Open the login page.
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

    # Step 2: Enter 'emilys' in the username field.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")

    # Step 3: Enter 'emilyspass' in the password field.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")

    # Step 4: Click the Login button.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()

    # Handle potential alert after login
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        assert alert_text == "Login successful"  # Assuming this is the expected alert text
        alert.accept()
    except Exception as e:
        logging.error("No alert appeared after login or alert text was incorrect.")
        raise AssertionError("Alert did not appear or text was incorrect.")

    # Step 5: Click the Back to Shop button.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "backToShopBtn"))).click()

    # Verification: Check if user is redirected back to the shop page.
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html", "User is not redirected to the shop page."

except Exception as e:
    logging.error(f"Test failed: {str(e)}")
    raise

finally:
    logging.info("End of test.")
    logging.info("===================================")