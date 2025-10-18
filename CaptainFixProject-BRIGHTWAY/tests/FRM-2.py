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

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input field to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    
    # Leave the username field empty
    username_input = driver.find_element(By.ID, "username")
    username_input.clear()  # Ensure it's empty

    # Submit the form
    login_form = driver.find_element(By.ID, "loginForm")
    login_form.submit()

    # Wait for the error message to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    
    # Verify the error message
    error_message = driver.find_element(By.ID, "usernameError").text
    expected_error_message = "This field is required."  # Assuming this is the expected error message
    if error_message != expected_error_message:
        driver.save_screenshot('error_screenshot.png')
        raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{error_message}'")

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password field to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys('emilyspass')
except Exception as e:
    print("Error entering password:", e)

# Check for any JavaScript alerts
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
except Exception as e:
    print("No alert present or error:", e)

# Check for error messages after entering the password
try:
    username_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    expected_error = "Error message displayed for empty username."
    if username_error != expected_error:
        raise AssertionError(f"Expected error message: '{expected_error}', but got: '{username_error}'")
except Exception as e:
    print("Error checking for username error message:", e)

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
    raise AssertionError(f"Failed to click the login button: {str(e)}")

# Verify if the error message for empty username is displayed
try:
    username_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    actual_error_message = username_error.text
    expected_error_message = "This field is required."  # Assuming this is the expected error message
    assert actual_error_message == expected_error_message, f"Expected error message: '{expected_error_message}', but got: '{actual_error_message}'"
except Exception as e:
    driver.save_screenshot('error_verifying_username_error.png')
    raise AssertionError(f"Failed to verify the username error message: {str(e)}")

# Detect any errors on the page
try:
    # Check for any JavaScript alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Please fill out this field."  # Assuming this is the expected alert text
    assert alert_text == expected_alert_text, f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'"
    alert.accept()
except Exception as e:
    driver.save_screenshot('error_alert_not_present.png')
    raise AssertionError(f"Alert not present or verification failed: {str(e)}")