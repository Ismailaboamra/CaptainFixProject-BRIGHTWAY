from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Verify that the login page is displayed
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    login_page_visible = driver.find_element(By.ID, "loginPage").is_displayed()
    
    if not login_page_visible:
        raise AssertionError("Login page is not visible.")
    
    # Check for any errors on the page
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        raise AssertionError(f"Detected error messages: {error_texts}")

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input field to be present and enter the username
    username_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    username_input.send_keys('emilys')
    
    # Check for any inline errors after entering the username
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    if error_message.is_displayed() and error_message.text != "":
        raise AssertionError(f"Error message displayed: {error_message.text}")

    # Verify that no duplicate login attempts occurred (assuming a specific element or state indicates this)
    # This part may vary based on the actual implementation of the application
    # For example, checking if a specific element is visible or if an alert appears
    # Here we assume that if the username is entered correctly, no alert should appear
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()  # Accept the alert after verification
    if alert_text != "Expected alert text":
        raise AssertionError(f"Unexpected alert text: {alert_text}")

except Exception as e:
    # If any error occurs, take a screenshot for debugging
    driver.save_screenshot('error_screenshot.png')
    raise e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password field to be present and enter the password
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys('emilyspass')
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter password: " + str(e))

try:
    # Check for any error messages after entering the password
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    if error_message.is_displayed() and error_message.text != "":
        driver.save_screenshot('error_screenshot.png')
        raise AssertionError("Error message displayed: " + error_message.text)
except Exception as e:
    # If no error message is found, proceed
    pass

try:
    # Check for JavaScript alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    if alert_text != "Expected alert text":  # Replace with the expected alert text if any
        driver.save_screenshot('error_screenshot.png')
        raise AssertionError("Unexpected alert text: " + alert_text)
except Exception as e:
    # No alert was present
    pass

# Additional checks for inline errors or notifications can be added here if necessary.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for any potential alert to appear
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    
    # Verify the alert text if it appears
    expected_alert_text = "No error or duplicate login attempts should occur."
    if alert_text != expected_alert_text:
        driver.save_screenshot("alert_error.png")
        raise AssertionError(f"Expected alert text '{expected_alert_text}' but got '{alert_text}'")
    
    # Accept the alert
    alert.accept()

except Exception as e:
    # Handle any errors that may occur
    driver.save_screenshot("error.png")
    raise AssertionError(f"An error occurred: {str(e)}")

# Check for any inline errors or notifications
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    if error_message.is_displayed():
        error_text = error_message.text
        expected_error_text = ""
        if error_text != expected_error_text:
            raise AssertionError(f"Expected no error message but got '{error_text}'")
except Exception as e:
    # If no error message is found, continue
    pass

try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    if error_message.is_displayed():
        error_text = error_message.text
        expected_error_text = ""
        if error_text != expected_error_text:
            raise AssertionError(f"Expected no error message but got '{error_text}'")
except Exception as e:
    # If no error message is found, continue
    pass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button rapidly
    login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary")))
    for _ in range(5):  # Click the button 5 times rapidly
        login_button.click()

    # Wait for any potential alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()

    # Verify that no error or duplicate login attempts occurred
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message:
        raise AssertionError(f"Error message detected: {error_message}")

except Exception as e:
    # If any error occurs, take a screenshot and raise an assertion error
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")