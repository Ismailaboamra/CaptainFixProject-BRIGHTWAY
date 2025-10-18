from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%A7%D8%AA%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Check if the user is logged in successfully
    user_name_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName")))
    actual_user_name = user_name_element.text
    
    # Verify the expected result
    expected_user_name = "Expected User Name"  # Replace with the actual expected user name after login
    if actual_user_name != expected_user_name:
        raise AssertionError(f"Expected user name '{expected_user_name}' but got '{actual_user_name}'")

except Exception as e:
    # Handle any alerts or errors
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert appeared with text: {alert_text}")
    except:
        pass  # No alert present

    # Check for inline errors or notifications
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Error message displayed: {error.text}")

    # Take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")
    raise e  # Re-raise the original exception

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input field to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Submit the login form
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginForm button[type='submit']"))).click()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to click login button: " + str(e))

# Verify successful login
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    actual_result = driver.find_element(By.ID, "shopPage").is_displayed()
    expected_result = True
    assert actual_result == expected_result, "User is not logged in successfully."
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Login verification failed: " + str(e))

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        if error_texts:
            raise AssertionError("Detected error messages: " + ", ".join(error_texts))
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Error checking failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input field to be present and enter the password
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

# Check for any alerts after clicking the login button
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "User is logged in successfully."
    if alert_text != expected_alert_text:
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError(f"Unexpected alert text: {alert_text}")
    alert.accept()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("No alert appeared or failed to handle alert: " + str(e))

# Verify successful login by checking the presence of the user's name or any other indicator
try:
    user_name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName")))
    if user_name.text == "":
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError("User is not logged in successfully.")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to verify user login: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the Login button to be clickable and then click it
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for any potential alert to appear
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    
    # Verify the alert text if needed (this is an example, adjust as necessary)
    expected_alert_text = "User logged in successfully."  # Adjust this based on actual expected alert text
    if alert_text != expected_alert_text:
        driver.save_screenshot('alert_error.png')
        raise AssertionError(f"Expected alert text '{expected_alert_text}' but got '{alert_text}'")
    
    # Accept the alert
    alert.accept()

except Exception as e:
    driver.save_screenshot('error.png')
    raise AssertionError(f"An error occurred: {str(e)}")

# Verification step: Check if the user is logged in successfully
try:
    # Wait for the user name element to be visible, indicating a successful login
    user_name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "userName")))
    actual_user_name = user_name.text
    
    # Assuming the expected user name is known (replace with actual expected value)
    expected_user_name = "Welcome, User!"  # Adjust this based on actual expected user name
    if actual_user_name != expected_user_name:
        raise AssertionError(f"Expected user name '{expected_user_name}' but got '{actual_user_name}'")

except Exception as e:
    driver.save_screenshot('verification_error.png')
    raise AssertionError(f"Verification failed: {str(e)}")