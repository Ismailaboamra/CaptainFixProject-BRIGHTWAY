from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%A7%D8%AA%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that the user is on the login page
    assert driver.find_element(By.ID, "loginPage").is_displayed(), "Login page is not displayed"
    
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Submit the login form
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to click login button: " + str(e))

# Verify successful login
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName")))
    actual_user_name = driver.find_element(By.ID, "userName").text
    expected_user_name = "emilys"  # Assuming the username is displayed after login
    if actual_user_name != expected_user_name:
        raise AssertionError(f"Expected user name '{expected_user_name}' but got '{actual_user_name}'")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Login verification failed: " + str(e))

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Error message displayed: {error.text}")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Error checking failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter password: " + str(e))

try:
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to click login button: " + str(e))

# Verify successful login
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName")))
    actual_user_name = driver.find_element(By.ID, "userName").text
    expected_user_name = "Welcome"  # Assuming the user name or welcome message is displayed
    if actual_user_name != expected_user_name:
        raise AssertionError(f"Expected user name to be '{expected_user_name}', but got '{actual_user_name}'")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Login verification failed: " + str(e))

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Error message displayed: {error.text}")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Error checking failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for potential alert and verify its presence
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "User is logged in successfully."  # Adjust this based on actual expected alert text
    if alert_text == expected_alert_text:
        alert.accept()
    else:
        driver.save_screenshot("alert_error.png")
        raise AssertionError(f"Unexpected alert text: {alert_text}")

except Exception as e:
    # Check for inline errors or notifications
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            driver.save_screenshot("inline_error.png")
            raise AssertionError(f"Inline error detected: {error.text}")

    # Check for any other notifications or modals
    # (Add additional checks as necessary based on the application behavior)

    raise e  # Re-raise the original exception if no specific error was found

# Verification step: Check if the user is logged in successfully
try:
    user_name_displayed = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName")))
    if not user_name_displayed.is_displayed():
        raise AssertionError("User is not logged in successfully.")
except Exception as e:
    driver.save_screenshot("login_verification_error.png")
    raise AssertionError("Failed to verify user login status.") from e