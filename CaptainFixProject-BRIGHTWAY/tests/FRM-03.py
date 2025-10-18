from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    
    # Attempt to submit the form without entering a username
    login_form = driver.find_element(By.ID, "loginForm")
    login_form.submit()
    
    # Wait for the error message to be displayed
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "usernameError")))
    
    # Verify the error message
    error_message = driver.find_element(By.ID, "usernameError").text
    expected_error_message = "This field is required."  # Assuming this is the expected error message
    if error_message != expected_error_message:
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{error_message}'")
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input field to be present
    username_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    
    # Enter an empty username (simulating the action)
    username_input.send_keys("")  # Leaving it empty to trigger the error

    # Submit the form
    login_form = driver.find_element(By.ID, "loginForm")
    login_form.submit()

    # Wait for the error message to be present
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    
    # Verify the error message is displayed
    if error_message.is_displayed():
        actual_error_text = error_message.text
        expected_error_text = "This field is required."  # Assuming this is the expected error message
        if actual_error_text != expected_error_text:
            # If the error message does not match, take a screenshot and raise an error
            driver.save_screenshot('error_screenshot.png')
            raise AssertionError(f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'")
    else:
        raise AssertionError("Error message is not displayed when it should be.")

except Exception as e:
    # Handle any unexpected errors
    driver.save_screenshot('unexpected_error_screenshot.png')
    raise e

# Check for any JavaScript alerts
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = ""  # Define expected alert text if any
    if alert_text != expected_alert_text:
        driver.save_screenshot('alert_error_screenshot.png')
        raise AssertionError(f"Unexpected alert text: '{alert_text}'")
    alert.accept()
except:
    pass  # No alert present, continue with the test

# Check for inline errors or notifications
# This part can be expanded based on the specific error messages expected on the page.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
except Exception as e:
    print("Error entering password:", e)

# Check for any JavaScript alerts or errors after entering the password
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
except Exception as e:
    print("No alert present or error occurred:", e)

# Verify if the error message for empty username is displayed
try:
    username_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    if username_error.is_displayed() and username_error.text != "":
        print("Error message displayed for empty username as expected.")
    else:
        raise AssertionError("Expected error message for empty username not displayed.")
except Exception as e:
    print("Error checking for username error message:", e)
    raise AssertionError("Error message for empty username not found.")

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
    raise AssertionError("Failed to click the Login button") from e

# Verify if the error message for empty username is displayed
try:
    username_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    actual_error_message = username_error.text
    expected_error_message = "This field is required."  # Assuming this is the expected error message for empty username
    assert actual_error_message == expected_error_message, f"Expected error message: '{expected_error_message}', but got: '{actual_error_message}'"
except Exception as e:
    driver.save_screenshot('error_verifying_username_error.png')
    raise AssertionError("Error message for empty username not displayed or verification failed") from e

# Detect any errors on the page
try:
    # Check for JavaScript alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Please fill out this field."  # Assuming this is the expected alert text
    assert alert_text == expected_alert_text, f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'"
    alert.accept()
except Exception as e:
    driver.save_screenshot('error_alert_not_present.png')
    raise AssertionError("No alert was present or alert verification failed") from e

# Check for inline form errors
try:
    inline_errors = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in inline_errors:
        if error.is_displayed():
            print(f"Inline error detected: {error.text}")
except Exception as e:
    driver.save_screenshot('error_inline_errors.png')
    raise AssertionError("Failed to detect inline errors") from e