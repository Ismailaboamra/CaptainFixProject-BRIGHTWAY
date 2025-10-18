from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%A7%D8%AA%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Attempt to submit the login form without entering a password
    username_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_input.send_keys("testuser")  # Enter a username for testing

    login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()

    # Wait for the error message to be displayed
    password_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    
    # Verify the error message
    actual_error_message = password_error.text
    expected_error_message = "This field is required."  # Assuming this is the expected error message for empty password

    if actual_error_message != expected_error_message:
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{actual_error_message}'")

except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username field to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys('emilys')
except Exception as e:
    print("Error entering username:", e)

try:
    # Wait for the password field to be present and leave it empty
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys('')
except Exception as e:
    print("Error entering password:", e)

try:
    # Wait for the login button to be present and click it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    print("Error clicking login button:", e)

# Verify if the error message for the password is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError"))).text
    expected_error_message = "This field is required."  # Assuming this is the expected error message
    if error_message != expected_error_message:
        raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{error_message}'")
except Exception as e:
    print("Error verifying password error message:", e)

# Check for any JavaScript alerts
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = ""  # Define expected alert text if any
    if alert_text != expected_alert_text:
        raise AssertionError(f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'")
    alert.accept()
except Exception as e:
    print("No alert present or error occurred:", e)

# Check for inline errors or notifications
try:
    inline_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError"))).text
    if inline_error:
        print("Inline error detected:", inline_error)
except Exception as e:
    print("Error checking for inline errors:", e)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password field to be present and interact with it
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.clear()  # Leave the password field empty

    # Submit the form
    login_form = driver.find_element(By.ID, "loginForm")
    login_form.submit()

    # Wait for the error message to be present
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    actual_error_text = error_message.text

    # Verify the expected error message
    expected_error_text = "This field is required."  # Assuming this is the expected error message
    if actual_error_text != expected_error_text:
        driver.save_screenshot('error_screenshot.png')
        raise AssertionError(f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'")

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

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

# Verify if the error message for empty password is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    actual_error_text = error_message.text
    expected_error_text = "This field is required."  # Assuming this is the expected error message
    assert actual_error_text == expected_error_text, f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'"
except Exception as e:
    driver.save_screenshot('error_verifying_error_message.png')
    raise AssertionError("Error message for empty password not displayed or verification failed") from e

# Detect any errors on the page
try:
    alert = WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert_text = alert.text
    expected_alert_text = ""  # Define expected alert text if any
    assert alert_text == expected_alert_text, f"Unexpected alert text: '{alert_text}'"
    alert.accept()
except Exception as e:
    # No alert present, continue checking for inline errors
    pass

# Check for inline errors
try:
    inline_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    if inline_error.is_displayed():
        actual_inline_error_text = inline_error.text
        assert actual_inline_error_text == expected_error_text, f"Expected inline error message: '{expected_error_text}', but got: '{actual_inline_error_text}'"
except Exception as e:
    driver.save_screenshot('error_inline_error_check.png')
    raise AssertionError("Inline error check failed") from e