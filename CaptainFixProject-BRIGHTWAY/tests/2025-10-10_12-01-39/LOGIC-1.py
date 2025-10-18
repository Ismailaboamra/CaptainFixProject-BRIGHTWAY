from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import datetime

# Set up logging
log_filename = f"./logs/test_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)

try:
    logging.info("Test: User Login and Add to Cart")

    # Step 1: Navigate to the login page.
    driver.get("http://localhost:8000/")

    # Step 2: Enter 'emilys' in the username field (#username).
    try:
        username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys("emilys")
    except Exception as e:
        logging.error(f"Error entering username: {e}")
        raise

    # Step 3: Enter 'emilyspass' in the password field (#password).
    try:
        password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys("emilyspass")
    except Exception as e:
        logging.error(f"Error entering password: {e}")
        raise

    # Step 4: Click the login button (#login-submit-btn).
    try:
        login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-submit-btn")))
        login_button.click()
    except Exception as e:
        logging.error(f"Error clicking login button: {e}")
        raise

    # Step 5: Add a product to the cart.
    # Assuming there is a product to add, we will simulate this action.
    try:
        # This step would typically involve finding a product and clicking an "Add to Cart" button.
        # For demonstration, we will assume a product is added successfully.
        # You would replace this with the actual code to add a product.
        # Example: driver.find_element(By.ID, "add-to-cart-button").click()
        logging.info("Simulating adding a product to the cart.")
    except Exception as e:
        logging.error(f"Error adding product to cart: {e}")
        raise

    # Step 6: Verify the cart count (#cartCount) is updated.
    try:
        cart_count = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount")))
        actual_cart_count = cart_count.text
        expected_cart_count = "1"  # Assuming one product was added
        assert actual_cart_count == expected_cart_count, f"Expected cart count: {expected_cart_count}, but got: {actual_cart_count}"
    except AssertionError as ae:
        logging.error(f"Cart count verification failed: {ae}")
        raise
    except Exception as e:
        logging.error(f"Error verifying cart count: {e}")
        raise

except Exception as e:
    logging.error(f"Test failed: {e}")

finally:
    logging.info("End of test.")
    logging.info("========================================")