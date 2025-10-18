from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import datetime

# Set up logging
log_file = f"./logs/test_log_{datetime.datetime.now().strftime('%Y%m%d')}.log"
logging.basicConfig(filename=log_file, level=logging.INFO)

# Start of the test
logging.info("Test: Login and Search Functionality")

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
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
except Exception as e:
    logging.error(f"Error clicking login button: {e}")
    raise

# Handle any alerts after login
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "Expected alert text"  # Replace with actual expected alert text
    alert.accept()
except Exception as e:
    logging.error(f"Error handling alert: {e}")

try:
    # Step 5: Enter 'laptop' in the search input
    search_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchInput")))
    search_input.send_keys("laptop")
except Exception as e:
    logging.error(f"Error entering search term: {e}")
    raise

try:
    # Step 6: Click the Search button
    search_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchBtn")))
    search_button.click()
except Exception as e:
    logging.error(f"Error clicking search button: {e}")
    raise

# Verification step
try:
    search_results_info = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchResultsInfo")))
    assert "Search results for 'laptop'" in search_results_info.text  # Adjust based on actual expected text
except Exception as e:
    logging.error(f"Error verifying search results: {e}")
    raise

# End of the test
logging.info("Test completed successfully.")
logging.info("========================================")