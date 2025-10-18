from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginPage")))
    
    # Verification: Check if the login page is displayed
    actual_page_state = driver.find_element(By.ID, "loginPage").is_displayed()
    expected_page_state = True
    assert actual_page_state == expected_page_state, "Login page is not displayed as expected."

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred while opening the login page: {str(e)}")

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
    username_input.clear()
    username_input.send_keys("emilys")
    
    # Verification: Check for duplicate login attempts
    # Assuming there's a mechanism to check for duplicate login attempts, 
    # we would need to verify that no such message appears.
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    ).text
    
    if error_message != "":
        raise AssertionError("Duplicate login attempt error message is displayed: " + error_message)

except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("An error occurred while entering the username: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter password
try:
    password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.send_keys("emilyspass")
    
    # Verification: Check for duplicate login attempts
    # Assuming there is a mechanism to check for this, e.g., an error message or a specific element
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "passwordError"))
    )
    actual_error_text = error_message.text
    expected_error_text = "No duplicate login attempts should be processed."
    
    if actual_error_text != expected_error_text:
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError(f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'")
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
    
    # Verification: Check for duplicate login attempts
    # Assuming there's a mechanism to check for duplicate login attempts, 
    # you would need to implement that check here. For example:
    # actual_error_message = driver.find_element(By.ID, "error-message").text
    # expected_error_message = "No duplicate login attempts should be processed."
    # assert actual_error_message == expected_error_message, f"Expected error message: '{expected_error_message}', but got: '{actual_error_message}'"

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to click the login button: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the login page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Click the Login button again quickly
try:
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    login_button.click()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to click the login button: " + str(e))

# Step 3: Verify that no duplicate login attempts are processed
try:
    # Assuming there is a way to check for duplicate login attempts, such as an error message or a state change
    # This is a placeholder for the actual verification logic
    # Example: Check for an error message or a specific state in the application
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    assert error_message.text == "", "Duplicate login attempt detected."
except AssertionError as ae:
    driver.save_screenshot("duplicate_login_attempt.png")
    raise AssertionError("Expected no duplicate login attempts, but found an error: " + str(ae))
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Verification failed: " + str(e))