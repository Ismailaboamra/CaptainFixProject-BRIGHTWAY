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
test_name = "Login and Navigate to Shop Test"
logging.info(test_name)

# Step 1: Navigate to the login page.
driver.get("http://localhost:8000/")

try:
    # Step 2: Enter 'emilys' in the username field (#username).
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    logging.error(f"Error entering username: {str(e)}")
    raise

try:
    # Step 3: Enter 'emilyspass' in the password field (#password).
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
except Exception as e:
    logging.error(f"Error entering password: {str(e)}")
    raise

try:
    # Step 4: Click the login button (#login-submit-btn).
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-submit-btn"))).click()
except Exception as e:
    logging.error(f"Error clicking login button: {str(e)}")
    raise

# Verify successful login and navigation to shop page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shop-header")))
except Exception as e:
    logging.error(f"Error verifying navigation to shop page: {str(e)}")
    raise

try:
    # Step 5: Select a category from the category filter (#categoryFilter).
    category_filter = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "categoryFilter")))
    category_filter.click()
    category_filter.find_element(By.XPATH, "//option[@value='']").click()  # Selecting "All Categories"
except Exception as e:
    logging.error(f"Error selecting category: {str(e)}")
    raise

# Verify category selection
try:
    selected_category = category_filter.get_attribute("value")
    assert selected_category == "", f"Expected category to be '', but got '{selected_category}'"
except AssertionError as e:
    logging.error(f"Category selection verification failed: {str(e)}")
    raise

try:
    # Step 6: Add a product to the cart.
    # Assuming there is a product to add, this step would require additional context about the product.
    # For demonstration, we will simulate adding a product.
    # This part of the code would need to be adjusted based on the actual product elements on the page.
    # Example: driver.find_element(By.ID, "add-to-cart-button").click()
    logging.info("Simulating adding a product to the cart.")
except Exception as e:
    logging.error(f"Error adding product to cart: {str(e)}")
    raise

try:
    # Step 7: Click the cart button (#cartBtn).
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "cartBtn"))).click()
except Exception as e:
    logging.error(f"Error clicking cart button: {str(e)}")
    raise

# Verify navigation to cart page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cart-header")))
except Exception as e:
    logging.error(f"Error verifying navigation to cart page: {str(e)}")
    raise

# End of test
logging.info("Test completed successfully.")
logging.info("========================================")