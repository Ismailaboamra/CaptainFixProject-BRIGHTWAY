from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the login form to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm")))
    
    # Attempt to submit invalid credentials
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")

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
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D9%8A%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input field to be present and enter the invalid username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("invalidUser")
except Exception as e:
    print("Error entering username:", e)

try:
    # Submit the login form
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
except Exception as e:
    print("Error clicking login button:", e)

# Check for error message
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    expected_error_message = "Error message displayed for invalid credentials."
    if error_message != expected_error_message:
        raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{error_message}'")
except Exception as e:
    print("Error checking for error message:", e)

# Handle any alerts or popups
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Expected alert message if any."
    if alert_text != expected_alert_text:
        raise AssertionError(f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'")
    alert.accept()
except Exception as e:
    print("No alert present or error handling alert:", e)

# Detect and verify any inline errors or notifications
try:
    inline_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if inline_error:
        print("Detected inline error message:", inline_error)
except Exception as e:
    print("Error checking for inline errors:", e)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input field to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("wrongPass")
except Exception as e:
    print("Error entering password:", e)

try:
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    print("Error clicking login button:", e)

# Check for error message after attempting to log in
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    error_message = driver.find_element(By.ID, "passwordError").text
    expected_error_message = "Invalid credentials"  # Assuming this is the expected error message
    if error_message != expected_error_message:
        raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{error_message}'")
except Exception as e:
    print("Error checking for error message:", e)
    # Take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Error message not displayed as expected.")

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
    expected_alert_text = "Invalid credentials"  # Assuming this is the expected alert text
    if alert_text != expected_alert_text:
        driver.save_screenshot('alert_error.png')
        raise AssertionError(f"Expected alert text '{expected_alert_text}' but got '{alert_text}'")
    alert.accept()

except Exception as e:
    # Handle any errors that may occur
    print(f"An error occurred: {str(e)}")
    driver.save_screenshot('error.png')
    raise

# Verify if the error message is displayed for invalid credentials
try:
    error_message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "usernameError")))
    if error_message.text == "":
        raise AssertionError("Expected error message for invalid credentials is not displayed.")
except Exception as e:
    print(f"An error occurred while verifying the error message: {str(e)}")
    driver.save_screenshot('verification_error.png')
    raise