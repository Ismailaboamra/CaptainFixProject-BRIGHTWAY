from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Attempt to submit the login form without entering a password
try:
    login_form = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm")))
    login_form.submit()
except Exception as e:
    raise AssertionError(f"Failed to submit the login form: {str(e)}")

# Step 3: Verify that the error message for empty password is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "passwordError")))
    actual_error_text = error_message.text
    expected_error_text = "This field is required."  # Assuming this is the expected error message
    assert actual_error_text == expected_error_text, f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'"
except Exception as e:
    raise AssertionError(f"Error message verification failed: {str(e)}")

# Step 4: Check for any other errors on the page
try:
    # Check for JavaScript alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()  # Accept the alert after verification if needed
except Exception:
    pass  # No alert present, continue checking for other errors

# Check for inline form errors
try:
    inline_errors = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in inline_errors:
        if error.is_displayed():
            print(f"Inline error detected: {error.text}")
except Exception as e:
    raise AssertionError(f"Error checking inline errors: {str(e)}")

# Check for toast/banner notifications (if any)
try:
    # Assuming there's a class for toast notifications
    toast_notifications = driver.find_elements(By.CLASS_NAME, "toast")
    for toast in toast_notifications:
        if toast.is_displayed():
            print(f"Toast notification detected: {toast.text}")
except Exception as e:
    raise AssertionError(f"Error checking toast notifications: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Step 1: Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter username
try:
    username_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_input.send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter username: " + str(e))

# Step 3: Check for error message for empty password
try:
    password_error = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "passwordError"))
    )
    actual_error_message = password_error.text
    expected_error_message = "This field is required."  # Assuming this is the expected error message
    assert actual_error_message == expected_error_message, f"Expected error message: '{expected_error_message}', but got: '{actual_error_message}'"
except TimeoutException:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Error message for empty password not displayed.")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Error checking for password error message: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Leave the password field empty
try:
    password_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "password")))
    password_field.clear()  # Ensure the password field is empty
    password_field.send_keys("")  # Leave it empty
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to leave the password field empty: {str(e)}")

# Step 3: Submit the form
try:
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to click the login button: {str(e)}")

# Step 4: Verify the error message for empty password
try:
    error_message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "passwordError")))
    actual_error_text = error_message.text
    expected_error_text = "This field is required."  # Assuming this is the expected error message
    assert actual_error_text == expected_error_text, f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'"
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Error message verification failed: {str(e)}")

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
    
    # Verification: Check for error message for empty password
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "passwordError"))
    )
    actual_error_text = error_message.text
    expected_error_text = "This field is required."  # Assuming this is the expected error message
    assert actual_error_text == expected_error_text, f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'"

except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")