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
logging.info("Test: Login and Search Products")

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

# Step 5: Select a category from the category filter
try:
    category_filter = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "categoryFilter")))
    category_filter.click()
    # Assuming there's a category to select, you may need to add logic to select an option
    # For example, if there's an option with value "category1":
    category_filter.find_element(By.XPATH, "//option[@value='category1']").click()  # Replace 'category1' with actual value
except Exception as e:
    logging.error(f"Error selecting category: {e}")
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
    # Check if products from the selected category are displayed
    products_displayed = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    assert products_displayed.is_displayed(), "Products from the selected category are not displayed."
except Exception as e:
    logging.error(f"Verification failed: {e}")
    raise

# End of test log
logging.info("Test completed successfully.")
logging.info("========================================")