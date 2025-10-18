from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Verify that the login page is displayed
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginPage")))
    assert driver.find_element(By.ID, "loginPage").is_displayed(), "Login page is not displayed."
except Exception as e:
    driver.save_screenshot("error_login_page.png")
    raise AssertionError(f"Failed to open login page: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the login page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter username
try:
    username_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_input.send_keys("emilys")
    
    # Verification: Check if the username is entered correctly
    assert username_input.get_attribute('value') == "emilys", "Username was not entered correctly."
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to enter username: {str(e)}")

# Step 3: Check for any errors on the page
try:
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    if error_message.is_displayed():
        error_text = error_message.text
        assert error_text == "", f"Unexpected error message: {error_text}"
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Error detection failed: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the login page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter password
try:
    password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.send_keys("emilyspass")
    
    # Verification: Check if the user is logged in successfully
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    login_button.click()
    
    # Check for successful login (this could be a redirect or a change in the page)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "shopPage"))
    )
    
    # Verification: Assert that the user is on the shop page
    assert "shopPage" in driver.page_source, "User is not logged in successfully."
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Click the Login button
try:
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    login_button.click()
    
    # Verification: Check if user is logged in successfully
    # This could be checking for a specific element that appears after login
    # For example, checking if the shop page is displayed
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "shopPage"))
    )
    
    # If the shop page is visible, the login was successful
    print("User is logged in successfully.")
    
except Exception as e:
    # If there's an error, take a screenshot and raise an assertion error
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Login button click failed or user is not logged in successfully.") from e

# Error detection after the step
try:
    # Check for JavaScript alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()  # Accept the alert after verification
    # Compare alert_text with expected result if needed
except Exception:
    pass  # No alert present

# Check for inline form errors
username_error = driver.find_element(By.ID, "usernameError").text
password_error = driver.find_element(By.ID, "passwordError").text

if username_error or password_error:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Inline errors detected: {username_error}, {password_error}")

# Check for toast/banner notifications if any
# Assuming there's a way to detect toast notifications, e.g., by a specific class or ID
# Example: toast_message = driver.find_element(By.CLASS_NAME, "toast-message").text
# if toast_message:
#     driver.save_screenshot('error_screenshot.png')
#     raise AssertionError(f"Toast notification detected: {toast_message}")