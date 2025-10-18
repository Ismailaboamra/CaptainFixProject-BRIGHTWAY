from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Attempt to submit the login form without entering a password
    username_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_input.send_keys("testuser")  # Enter a username for testing

    login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()

    # Wait for the error message to be displayed
    password_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    actual_error_message = password_error.text

    # Verify the expected error message
    expected_error_message = "This field is required."  # Assuming this is the expected error message
    if actual_error_message != expected_error_message:
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{actual_error_message}'")

except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Enter username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_username_entry.png")
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot("error_login_button_click.png")
    raise AssertionError("Failed to click login button: " + str(e))

# Check for error message for empty password
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    error_message = driver.find_element(By.ID, "passwordError").text
    expected_error_message = "Password is required"  # Assuming this is the expected error message
    if error_message != expected_error_message:
        driver.save_screenshot("error_message_verification_failed.png")
        raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{error_message}'")
except Exception as e:
    driver.save_screenshot("error_checking_error_message.png")
    raise AssertionError("Failed to check for error message: " + str(e))

# Detect any JavaScript alerts
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Please fill in all required fields."  # Assuming this is the expected alert text
    if alert_text != expected_alert_text:
        driver.save_screenshot("alert_verification_failed.png")
        raise AssertionError(f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'")
    alert.accept()
except Exception as e:
    driver.save_screenshot("error_checking_alert.png")
    raise AssertionError("No alert appeared or alert verification failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Locate the password input field and enter an empty string
    password_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys("")  # Entering empty password

    # Locate and click the login button
    login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()

    # Wait for the error message to be displayed
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    
    # Verify the error message is displayed
    if error_message.is_displayed():
        actual_error_text = error_message.text
        expected_error_text = "This field is required."  # Assuming this is the expected error message
        if actual_error_text != expected_error_text:
            driver.save_screenshot("error_screenshot.png")
            raise AssertionError(f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'")
    else:
        raise AssertionError("Error message not displayed for empty password.")

except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
except Exception as e:
    driver.save_screenshot('error_click_login_button.png')
    raise AssertionError(f"Failed to click the login button: {str(e)}")

# Verify if the error message for empty password is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "passwordError")))
    actual_error_text = error_message.text
    expected_error_text = "This field is required."  # Assuming this is the expected error message for empty password
    if actual_error_text != expected_error_text:
        driver.save_screenshot('error_message_mismatch.png')
        raise AssertionError(f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'")
except Exception as e:
    driver.save_screenshot('error_checking_password_error.png')
    raise AssertionError(f"Failed to verify the error message: {str(e)}")

# Detect any JavaScript alerts or inline errors
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Please fill out this field."  # Assuming this is the expected alert message
    if alert_text != expected_alert_text:
        driver.save_screenshot('alert_text_mismatch.png')
        raise AssertionError(f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'")
    alert.accept()
except Exception as e:
    # No alert was present, continue checking for inline errors
    pass

# Check for any inline form errors or notifications
try:
    inline_error = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "passwordError")))
    if inline_error.is_displayed():
        actual_inline_error_text = inline_error.text
        if actual_inline_error_text != expected_error_text:
            driver.save_screenshot('inline_error_mismatch.png')
            raise AssertionError(f"Expected inline error message: '{expected_error_text}', but got: '{actual_inline_error_text}'")
except Exception as e:
    driver.save_screenshot('error_checking_inline_errors.png')
    raise AssertionError(f"Failed to check for inline errors: {str(e)}")