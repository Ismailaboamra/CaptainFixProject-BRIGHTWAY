from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Verify that the login page is displayed
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginForm")))
    print("Login page is displayed.")
except Exception as e:
    driver.save_screenshot("login_page_error.png")
    raise AssertionError("Login page did not display as expected.") from e

# Step 2: Attempt to submit invalid credentials to trigger error message
try:
    username_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "username")))
    username_input.send_keys("invalidUser")
    
    password_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password")))
    password_input.send_keys("invalidPass")
    
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
except Exception as e:
    driver.save_screenshot("login_interaction_error.png")
    raise AssertionError("Failed to interact with login form.") from e

# Step 3: Verify that the error message is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "usernameError")))
    assert error_message.is_displayed(), "Error message for username is not displayed."
    print("Error message for invalid credentials is displayed.")
except Exception as e:
    driver.save_screenshot("error_message_verification_error.png")
    raise AssertionError("Error message for invalid credentials was not displayed as expected.") from e

# Step 4: Check for any additional errors on the page
try:
    # Check for JavaScript alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()  # Accept the alert after verification
except Exception as e:
    print("No alert was present.")

# Check for inline form errors
try:
    username_error = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "usernameError")))
    password_error = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "passwordError")))
    assert username_error.is_displayed() or password_error.is_displayed(), "No inline error messages are displayed."
except Exception as e:
    driver.save_screenshot("inline_error_verification_error.png")
    raise AssertionError("Inline error messages were not displayed as expected.") from e

# Check for toast/banner notifications
# Assuming there are no toast notifications in the provided HTML, this step can be skipped or customized based on actual implementation.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Step 1: Navigate to the login page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter username
try:
    username_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_input.send_keys("emilys")
    
    # Verification: Check for error message
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    actual_error_text = error_message.text
    expected_error_text = "Error message displayed for invalid credentials."
    
    if actual_error_text != expected_error_text:
        raise AssertionError(f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'")
    
except TimeoutException:
    raise AssertionError("Element not found or not visible within the timeout period.")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter password
try:
    password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.send_keys("wrongpassword")
    
    # Verification: Check if the error message is displayed
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "passwordError"))
    )
    actual_error_text = error_message.text
    expected_error_text = "Invalid credentials"  # Adjust this based on the actual expected error message
    assert actual_error_text == expected_error_text, f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'"

except (TimeoutException, NoSuchElementException) as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("An error occurred while entering the password or verifying the error message.") from e

# Step 3: Error Detection
try:
    # Check for any JavaScript alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Expected alert message"  # Adjust this based on the actual expected alert message
    assert alert_text == expected_alert_text, f"Expected alert message: '{expected_alert_text}', but got: '{alert_text}'"
    alert.accept()

except TimeoutException:
    pass  # No alert present

# Check for inline form errors
try:
    inline_error = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "passwordError"))
    )
    if inline_error.is_displayed():
        actual_inline_error_text = inline_error.text
        assert actual_inline_error_text == expected_error_text, f"Expected inline error message: '{expected_error_text}', but got: '{actual_inline_error_text}'"
except (TimeoutException, NoSuchElementException):
    pass  # No inline error present

# Check for toast/banner notifications
try:
    toast_notification = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "toast-notification"))  # Adjust class name based on actual implementation
    )
    actual_toast_text = toast_notification.text
    expected_toast_text = "Expected toast message"  # Adjust this based on the actual expected toast message
    assert actual_toast_text == expected_toast_text, f"Expected toast message: '{expected_toast_text}', but got: '{actual_toast_text}'"
except (TimeoutException, NoSuchElementException):
    pass  # No toast notification present

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Click the Login button
try:
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    login_button.click()
    
    # Verification: Check for error message
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    actual_error_text = error_message.text
    expected_error_text = "Invalid credentials"  # Adjust this based on the actual expected error message
    assert actual_error_text == expected_error_text, f"Expected error message '{expected_error_text}' but got '{actual_error_text}'"

except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")