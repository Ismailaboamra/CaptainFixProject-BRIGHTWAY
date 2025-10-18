from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Check for any error messages related to the cart
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartErrorMessage")))
    actual_error_text = error_message.text
    
    # Expected error message
    expected_error_text = "Error message displayed for empty cart."
    
    # Verification step
    if actual_error_text != expected_error_text:
        # Save a screenshot for debugging
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError(f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'")
    
except Exception as e:
    # Handle any alerts or popups
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
    except:
        pass
    
    # Log the exception for debugging
    print(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_username_input.png")
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Check for any error messages after entering the username
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message != "Error message displayed for empty cart.":
        driver.save_screenshot("error_message_verification.png")
        raise AssertionError(f"Expected error message not found. Actual: {error_message}")
except Exception as e:
    driver.save_screenshot("error_message_check.png")
    raise AssertionError("Failed to check error message: " + str(e))

try:
    # Check for any JavaScript alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    if alert_text != "Expected alert message":
        driver.save_screenshot("alert_verification.png")
        raise AssertionError(f"Unexpected alert message: {alert_text}")
    alert.accept()
except Exception as e:
    driver.save_screenshot("alert_check.png")
    raise AssertionError("No alert appeared or failed to handle alert: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input field to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter password: " + str(e))

try:
    # Check for any JavaScript alerts after entering the password
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
except Exception as e:
    alert_text = None

# Check for errors on the page
error_message = None
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartItems"))).text
except Exception as e:
    error_message = None

# Verify the expected result
if error_message != "Error message displayed for empty cart.":
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Expected error message not displayed. Found: " + str(error_message))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
except Exception as e:
    driver.save_screenshot('error_click_login_button.png')
    raise AssertionError(f"Failed to click the Login button: {str(e)}")

# Check for any alerts after clicking the button
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Error message displayed for empty cart."
    if alert_text != expected_alert_text:
        driver.save_screenshot('error_alert_text.png')
        raise AssertionError(f"Unexpected alert text: {alert_text}")
    alert.accept()
except Exception as e:
    driver.save_screenshot('error_no_alert.png')
    raise AssertionError(f"No alert appeared or failed to handle alert: {str(e)}")

# Verify if the error message for empty cart is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "cartItems")))
    if error_message.text != "Error message displayed for empty cart.":
        driver.save_screenshot('error_message_not_displayed.png')
        raise AssertionError("Expected error message for empty cart is not displayed.")
except Exception as e:
    driver.save_screenshot('error_checking_message.png')
    raise AssertionError(f"Failed to verify error message: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Cart button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "cartBtn"))).click()
except Exception as e:
    driver.save_screenshot('error_click_cart_button.png')
    raise AssertionError("Failed to click the Cart button") from e

# Verify if the error message for empty cart is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartItems")))
    if error_message.text == "":
        raise AssertionError("Expected error message for empty cart is not displayed.")
except Exception as e:
    driver.save_screenshot('error_empty_cart_message.png')
    raise AssertionError("Failed to verify the error message for empty cart") from e

# Check for any alerts or popups
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    if alert_text != "Your cart is empty.":
        raise AssertionError("Unexpected alert message: " + alert_text)
except Exception as e:
    # No alert was present, continue
    pass

# Check for inline errors or notifications
try:
    inline_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartItems")))
    if inline_error.text == "":
        raise AssertionError("Expected inline error message for empty cart is not displayed.")
except Exception as e:
    driver.save_screenshot('error_inline_message.png')
    raise AssertionError("Failed to verify inline error message for empty cart") from e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Proceed to Checkout button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.btn-checkout"))).click()
except Exception as e:
    print("Error clicking the Proceed to Checkout button:", e)

# Check for any alerts or error messages
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
except Exception as e:
    print("No alert present or error occurred:", e)

# Verify if the error message for empty cart is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cartItems .error-message")))
    actual_error_text = error_message.text
    expected_error_text = "Your cart is empty."  # Assuming this is the expected error message
    assert actual_error_text == expected_error_text, f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'"
except Exception as e:
    print("Error verifying the error message:", e)
    raise AssertionError("Error message verification failed.")