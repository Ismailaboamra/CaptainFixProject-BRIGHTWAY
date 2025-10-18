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
    logging.info("Test: Login and Add Items to Cart")

    # Step 1: Navigate to the login page.
    driver.get("http://localhost:8000/")

    # Step 2: Enter 'emilys' in the username field.
    try:
        username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys("emilys")
    except Exception as e:
        logging.error(f"Error entering username: {str(e)}")
        raise

    # Step 3: Enter 'emilyspass' in the password field.
    try:
        password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys("emilyspass")
    except Exception as e:
        logging.error(f"Error entering password: {str(e)}")
        raise

    # Step 4: Click the login button.
    try:
        login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-submit-btn")))
        login_button.click()
    except Exception as e:
        logging.error(f"Error clicking login button: {str(e)}")
        raise

    # Step 5: Add 2 items to the cart.
    try:
        # Assuming there are items to add, we will simulate adding items to the cart.
        # This part of the code would depend on the actual implementation of adding items.
        # For demonstration, we will just simulate the action.
        # You would replace this with actual code to add items to the cart.
        # Example: driver.find_element(...).click() for each item.
        for _ in range(2):
            # Simulate adding an item to the cart
            # This is a placeholder for the actual item adding logic
            pass
    except Exception as e:
        logging.error(f"Error adding items to cart: {str(e)}")
        raise

    # Step 6: Verify the total items count in the cart.
    try:
        cart_count = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount")))
        actual_count = int(cart_count.text)
        expected_count = 2
        assert actual_count == expected_count, f"Expected {expected_count} items in cart, but found {actual_count}."
    except AssertionError as ae:
        logging.error(f"Verification failed: {str(ae)}")
        raise
    except Exception as e:
        logging.error(f"Error verifying cart count: {str(e)}")
        raise

except Exception as e:
    logging.error(f"Test failed: {str(e)}")

finally:
    logging.info("End of test.")
    logging.info("========================================")