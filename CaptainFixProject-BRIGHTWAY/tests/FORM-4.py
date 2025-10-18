from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the login form to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm")))
    
    # Attempt to submit the form with invalid credentials
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    
    username_input.send_keys("invalid_user")
    password_input.send_keys("invalid_pass")
    login_button.click()
    
    # Wait for the error message to be displayed
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "usernameError")))
    
    # Verify the error message
    error_message = driver.find_element(By.ID, "usernameError").text
    expected_error_message = "Invalid username or password."  # Assuming this is the expected error message
    if error_message != expected_error_message:
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{error_message}'")

except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input field to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    print("Error entering username:", e)

try:
    # Submit the login form
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm"))).submit()
except Exception as e:
    print("Error submitting the login form:", e)

# Wait for any error message to be displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    expected_error_message = "Invalid credentials."  # Assuming this is the expected error message
    if error_message != expected_error_message:
        raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{error_message}'")
except Exception as e:
    print("Error checking for error message:", e)
    # Take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input field to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("wrongpassword")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter password: " + str(e))

try:
    # Wait for the login button to be clickable and click it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click login button: " + str(e))

# Check for any alerts after clicking the login button
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Invalid credentials"  # Assuming this is the expected alert text
    if alert_text != expected_alert_text:
        driver.save_screenshot('error_screenshot.png')
        raise AssertionError(f"Unexpected alert text: {alert_text}")
    alert.accept()
except Exception as e:
    # If no alert is present, check for inline error messages
    try:
        error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError"))).text
        expected_error_message = "Invalid credentials"  # Assuming this is the expected error message
        if error_message != expected_error_message:
            driver.save_screenshot('error_screenshot.png')
            raise AssertionError(f"Expected error message not displayed: {error_message}")
    except Exception as e:
        driver.save_screenshot('error_screenshot.png')
        raise AssertionError("Failed to verify error message: " + str(e))

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

# Wait for the error message to be displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    actual_error_text = error_message.text
    expected_error_text = "Invalid credentials"  # Assuming this is the expected error message
    assert actual_error_text == expected_error_text, f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'"
except Exception as e:
    driver.save_screenshot('error_message_not_displayed.png')
    raise AssertionError("Error message not displayed as expected") from e

# Check for any JavaScript alerts
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Invalid credentials"  # Assuming this is the expected alert message
    assert alert_text == expected_alert_text, f"Expected alert message: '{expected_alert_text}', but got: '{alert_text}'"
    alert.accept()
except Exception as e:
    driver.save_screenshot('alert_not_displayed.png')
    raise AssertionError("Alert not displayed as expected") from e

# Check for inline form errors or notifications
try:
    inline_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    if inline_error.is_displayed():
        actual_inline_error_text = inline_error.text
        assert actual_inline_error_text == expected_error_text, f"Expected inline error message: '{expected_error_text}', but got: '{actual_inline_error_text}'"
except Exception as e:
    driver.save_screenshot('inline_error_not_displayed.png')
    raise AssertionError("Inline error message not displayed as expected") from e