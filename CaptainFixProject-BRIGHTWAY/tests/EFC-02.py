from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Check for any error messages on the page
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartItems")))
    if error_message.text == "":
        raise AssertionError("Expected error message for empty cart is not displayed.")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("An error occurred while checking for error messages: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input field to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_username_input.png")
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Check for any JavaScript alerts after entering the username
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    # Verify the alert text if needed
except Exception as e:
    pass  # No alert present, continue

try:
    # Check for error messages on the page
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message != "Error message displayed for empty cart.":
        raise AssertionError(f"Expected error message not found. Actual: {error_message}")
except Exception as e:
    driver.save_screenshot("error_message_check.png")
    raise AssertionError("Failed to check for error message: " + str(e))

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
    alert.accept()  # Accept the alert after verification
except Exception as e:
    alert_text = None  # No alert present

# Check for errors on the page
error_messages = []
try:
    username_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if username_error:
        error_messages.append(username_error)
except Exception:
    pass

try:
    password_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError"))).text
    if password_error:
        error_messages.append(password_error)
except Exception:
    pass

# Verify the expected result
expected_error_message = "Error message displayed for empty cart."
if alert_text and alert_text != expected_error_message:
    error_messages.append(f"Alert text mismatch: expected '{expected_error_message}', got '{alert_text}'")

if error_messages:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Detected errors: " + ", ".join(error_messages))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for any potential alert and verify its presence
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Error message displayed for empty cart."
    
    if alert_text != expected_alert_text:
        driver.save_screenshot('alert_error.png')
        raise AssertionError(f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'")
    
    alert.accept()

except Exception as e:
    # Handle any errors that may occur
    driver.save_screenshot('error.png')
    raise AssertionError(f"An error occurred: {str(e)}")

# Verify if the error message is displayed on the page
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartError")))
    if error_message.is_displayed():
        print("Error message is displayed as expected.")
    else:
        raise AssertionError("Error message is not displayed.")
except Exception as e:
    driver.save_screenshot('error_message_check.png')
    raise AssertionError(f"Failed to verify error message: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Cart button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "cartBtn"))).click()
except Exception as e:
    driver.save_screenshot('error_click_cart_button.png')
    raise AssertionError("Failed to click the Cart button") from e

# Check for any alerts or error messages
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
except Exception as e:
    alert_text = None

# Verify if the error message for empty cart is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartItems")))
    if error_message.text == "":
        raise AssertionError("Expected error message for empty cart is not displayed.")
except Exception as e:
    driver.save_screenshot('error_empty_cart_message.png')
    raise AssertionError("Failed to verify error message for empty cart") from e

# Log detected messages for debugging
if alert_text:
    print(f"Alert detected: {alert_text}")

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
    alert_text = None

# Verify if the error message for empty cart is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cartItems .error-message")))
    actual_error_text = error_message.text
    expected_error_text = "Your cart is empty. Please add items to proceed."
    
    if actual_error_text != expected_error_text:
        raise AssertionError(f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'")
except Exception as e:
    print("Error checking for error message:", e)
    raise AssertionError("Error message for empty cart not displayed.")