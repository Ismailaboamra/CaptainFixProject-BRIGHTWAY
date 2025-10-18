from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open the login page.
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Attempt to find the username input field and leave it empty to trigger the error message
    username_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "username")))
    username_input.clear()  # Ensure the field is empty

    # Submit the form to trigger validation
    login_form = driver.find_element(By.ID, "loginForm")
    login_form.submit()

    # Verify if the error message is displayed
    error_message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "usernameError")))
    actual_error_text = error_message.text

    # Check if the expected error message is displayed
    expected_error_text = "This field is required."  # Assuming this is the expected error message
    assert actual_error_text == expected_error_text, f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'"

except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Step 1: Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Leave the username field empty
try:
    username_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "username")))
    username_input.clear()  # Ensure the field is empty
    password_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.send_keys("validPassword")  # Assuming a valid password is needed to trigger the error
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
except Exception as e:
    driver.save_screenshot("error_step2.png")
    raise AssertionError(f"Failed to leave the username field empty: {str(e)}")

# Step 3: Verify the error message for empty username
try:
    error_message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "usernameError")))
    actual_error_text = error_message.text
    expected_error_text = "This field is required."  # Assuming this is the expected error message
    assert actual_error_text == expected_error_text, f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'"
except TimeoutException:
    driver.save_screenshot("error_message_not_displayed.png")
    raise AssertionError("Error message for empty username was not displayed.")
except AssertionError as e:
    driver.save_screenshot("error_message_mismatch.png")
    raise e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter password
try:
    password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.send_keys("emilyspass")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter password: " + str(e))

# Step 3: Verify error message for empty username
try:
    username_error = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    actual_error_message = username_error.text
    expected_error_message = "Error message displayed for empty username."
    assert actual_error_message != "", "Expected error message not displayed for empty username."
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Error message verification failed: " + str(e))

# Step 4: Check for any errors on the page
try:
    # Check for JavaScript alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()  # Accept the alert after verification
except Exception:
    alert_text = None

# Check for inline form errors
try:
    username_error = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    inline_error_message = username_error.text
except Exception:
    inline_error_message = ""

# Check for toast/banner notifications (if any)
# Assuming there's a toast/banner element with a specific class or ID
# This part may need to be adjusted based on actual implementation
try:
    toast_notification = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "toast-notification"))
    )
    toast_message = toast_notification.text
except Exception:
    toast_message = ""

# Log any detected errors for debugging
if alert_text or inline_error_message or toast_message:
    error_messages = []
    if alert_text:
        error_messages.append(f"Alert: {alert_text}")
    if inline_error_message:
        error_messages.append(f"Inline Error: {inline_error_message}")
    if toast_message:
        error_messages.append(f"Toast Notification: {toast_message}")
    raise AssertionError("Detected errors on the page: " + ", ".join(error_messages))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Click the Login button
try:
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    login_button.click()
    
    # Verification: Check for error message for empty username
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    actual_error_text = error_message.text
    expected_error_text = "This field is required."  # Assuming this is the expected error message
    assert actual_error_text == expected_error_text, f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'"

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")