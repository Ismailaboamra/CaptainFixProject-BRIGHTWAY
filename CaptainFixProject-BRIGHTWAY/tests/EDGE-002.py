driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the password input field to be visible and interact with it
password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "password"))
)
password_input.send_keys("123")  # Enter a short password to trigger the error message

# Wait for the login button to be clickable and click it
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
)
login_button.click()

# Wait for the error message to be visible
error_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "passwordError"))
)

# Verify the error message is displayed
if error_message.is_displayed():
    actual_message = error_message.text
    expected_message = "Password must be at least 6 characters long."  # Assuming this is the expected error message
    if actual_message != expected_message:
        driver.save_screenshot("error_message_verification_failed.png")
        raise AssertionError(f"Expected error message: '{expected_message}', but got: '{actual_message}'")
else:
    driver.save_screenshot("error_message_not_displayed.png")
    raise AssertionError("Error message for password length is not displayed.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D9%AA%D8%A8/e-com/index.html")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Enter valid username
username_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))
)
username_input.send_keys("emilys")

# Submit the form
login_form = driver.find_element(By.ID, "loginForm")
login_form.submit()

# Verify the error message for password length
error_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "passwordError"))
)
if error_message.is_displayed() == False:
    driver.save_screenshot('error_message_not_displayed.png')
    raise AssertionError("Expected error message for password length is not displayed.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Enter a password shorter than 6 characters
password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
password_input.send_keys("123")

# Submit the form
login_form = driver.find_element(By.ID, "loginForm")
login_form.submit()

# Verify the error message is displayed for password length
error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "passwordError")))
if error_message.is_displayed() and "length" in error_message.text:
    print("Error message displayed as expected.")
else:
    driver.save_screenshot("error_message_verification_failed.png")
    raise AssertionError("Expected error message for password length not displayed.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Click on the 'Login' button
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
)
login_button.click()

# Verification step
error_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "passwordError"))
)
if error_message.text == "":
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Expected error message for password length is not displayed.")