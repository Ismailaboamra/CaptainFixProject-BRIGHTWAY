from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%A7%D8%AA%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

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
    # Wait for the username input to be present and enter the invalid username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("invalidUser")
except Exception as e:
    print("Error entering username:", e)

try:
    # Wait for the login button to be present and click it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    print("Error clicking login button:", e)

try:
    # Wait for the error message to be present
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    expected_error_message = "Error message is displayed for invalid credentials."
    
    # Verify the error message
    if error_message != expected_error_message:
        raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{error_message}'")
except Exception as e:
    print("Error verifying error message:", e)

try:
    # Check for any JavaScript alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Error message is displayed for invalid credentials."
    
    if alert_text != expected_alert_text:
        driver.save_screenshot("alert_error.png")
        raise AssertionError(f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'")
    
    alert.accept()
except Exception as e:
    print("No alert present or error verifying alert:", e)

# Detect and log any inline errors or notifications
try:
    inline_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if inline_error:
        print("Detected inline error message:", inline_error)
except Exception as e:
    print("Error detecting inline error message:", e)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input field to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("wrongPass")
    
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
    
    # Wait for the error message to be present
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError"))).text
    
    # Verify the expected result
    if "invalid credentials" not in error_message.lower():
        raise AssertionError(f"Expected error message for invalid credentials not displayed. Actual message: {error_message}")

except Exception as e:
    # Handle any alerts or popups
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Unexpected alert displayed: {alert_text}")
    except:
        # Take a screenshot for debugging
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError("An error occurred during the test execution.") from e

# Check for any inline errors or notifications
inline_error = driver.find_element(By.ID, "passwordError").text
if inline_error:
    raise AssertionError(f"Inline error message detected: {inline_error}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
    
    # Wait for any potential error message to be displayed
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    
    # Verify that the error message is displayed
    if error_message.is_displayed():
        actual_error_text = error_message.text
        expected_error_text = "Invalid credentials"  # Assuming this is the expected error message
        if actual_error_text != expected_error_text:
            driver.save_screenshot("error_screenshot.png")
            raise AssertionError(f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'")
    else:
        raise AssertionError("Error message is not displayed when it was expected to be.")
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")