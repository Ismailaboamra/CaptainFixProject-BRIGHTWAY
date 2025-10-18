from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Wait for the login form to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm")))
    
    # Attempt to submit the form without entering a password
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("testuser")  # Enter a username for testing
    login_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    login_button.click()
    
    # Wait for the error message to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    
    # Verify the error message for empty password
    error_message = driver.find_element(By.ID, "passwordError").text
    expected_error_message = "This field is required."  # Assuming this is the expected error message
    if error_message != expected_error_message:
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{error_message}'")
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Enter username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_username_entry.png")
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot("error_login_button_click.png")
    raise AssertionError("Failed to click login button: " + str(e))

# Verify if the error message for empty password is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError"))).text
    expected_error_message = "Password is required"  # Assuming this is the expected error message
    if error_message != expected_error_message:
        driver.save_screenshot("error_message_verification_failed.png")
        raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{error_message}'")
except Exception as e:
    driver.save_screenshot("error_password_error_message.png")
    raise AssertionError("Failed to verify error message: " + str(e))

# Check for any JavaScript alerts
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Please fill in all required fields."  # Assuming this is the expected alert text
    if alert_text != expected_alert_text:
        driver.save_screenshot("error_alert_verification_failed.png")
        raise AssertionError(f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'")
    alert.accept()
except Exception as e:
    driver.save_screenshot("error_alert_not_present.png")
    raise AssertionError("No alert was present or failed to verify alert: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input field to be present
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    
    # Leave the password field empty (do not send any keys)
    password_field.clear()  # Ensure it's empty

    # Submit the form
    login_form = driver.find_element(By.ID, "loginForm")
    login_form.submit()

    # Wait for the error message to be present
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    
    # Verify the error message is displayed
    if error_message.is_displayed():
        actual_error_text = error_message.text
        expected_error_text = "This field is required."  # Assuming this is the expected error message
        if actual_error_text != expected_error_text:
            # If the error message does not match, take a screenshot and raise an error
            driver.save_screenshot('error_screenshot.png')
            raise AssertionError(f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'")
    else:
        raise AssertionError("Error message for empty password is not displayed.")

except Exception as e:
    # Handle any unexpected errors
    driver.save_screenshot('unexpected_error_screenshot.png')
    raise e

# Check for any JavaScript alerts
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()  # Accept the alert after verification
except:
    pass  # No alert present, continue with the test

# Check for inline errors or notifications
inline_errors = driver.find_elements(By.CLASS_NAME, "error-message")
for error in inline_errors:
    if error.is_displayed():
        print(f"Detected inline error: {error.text}")  # Log detected errors
        if error.text != "This field is required.":  # Assuming this is the expected error message
            raise AssertionError(f"Unexpected inline error message: {error.text}")

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

# Verify if the error message for empty password is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    actual_error_text = error_message.text
    expected_error_text = "This field is required."  # Assuming this is the expected error message for empty password
    if actual_error_text != expected_error_text:
        driver.save_screenshot('error_message_verification_failed.png')
        raise AssertionError(f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'")
except Exception as e:
    driver.save_screenshot('error_checking_error_message.png')
    raise AssertionError(f"Failed to verify error message: {str(e)}")