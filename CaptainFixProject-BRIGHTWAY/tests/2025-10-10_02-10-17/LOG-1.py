from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import datetime

# Set up logging
log_file = f"./logs/test_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(filename=log_file, level=logging.INFO)

# Test name
logging.info("Test: Add Product to Cart")

# Step 1: Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Step 2: Enter 'emilys' in the username field
    username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_field.send_keys("emilys")
except Exception as e:
    logging.error(f"Error entering username: {str(e)}")
    raise

try:
    # Step 3: Enter 'emilyspass' in the password field
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("emilyspass")
except Exception as e:
    logging.error(f"Error entering password: {str(e)}")
    raise

try:
    # Step 4: Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
except Exception as e:
    logging.error(f"Error clicking login button: {str(e)}")
    raise

# Check for alerts after login
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "Expected alert text"  # Replace with actual expected alert text
    alert.accept()
except Exception as e:
    logging.error(f"Error handling alert: {str(e)}")

# Step 5: Add a product to the cart
try:
    # Assuming there is a product to add, you would need to locate the product and add it
    # This is a placeholder for the actual product adding logic
    add_product_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart")))
    add_product_button.click()
except Exception as e:
    logging.error(f"Error adding product to cart: {str(e)}")
    raise

# Step 6: Check the total items in the cart
try:
    total_items = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount")))
    actual_total_items = total_items.text
    expected_total_items = "1"  # Assuming one product was added
    assert actual_total_items == expected_total_items, f"Expected {expected_total_items} but got {actual_total_items}"
except Exception as e:
    logging.error(f"Error checking total items in cart: {str(e)}")
    raise

# End of test log
logging.info("Test completed successfully.")
logging.info("========================================")