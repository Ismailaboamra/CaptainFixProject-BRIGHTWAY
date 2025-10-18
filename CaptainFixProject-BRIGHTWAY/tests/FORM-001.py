driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the login page to be visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginPage")))

# Verify that error messages are displayed for both username and password fields
username_error_visible = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "usernameError")))
password_error_visible = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "passwordError")))

# Check if the error messages are displayed
if not username_error_visible.is_displayed() or not password_error_visible.is_displayed():
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Error messages are not displayed for both username and password fields.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Leave the username field empty
username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))

# Clear the username field (it should be empty already)
username_input.clear()

# Submit the form
login_form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginForm")))
login_form.submit()

# Verify that error messages are displayed
username_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "usernameError")))
password_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "passwordError")))

if username_error.is_displayed() and password_error.is_displayed():
    print("Error messages are displayed as expected.")
else:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Expected error messages are not displayed.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Leave the password field empty
username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
username_input.send_keys("testuser")  # Assuming a username is entered for testing

password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
password_input.send_keys("")  # Leave password empty

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
login_button.click()

# Verification step
try:
    username_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "usernameError")))
    password_error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "passwordError")))
    
    if username_error.text == "" or password_error.text == "":
        raise AssertionError("Error messages are not displayed as expected.")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise e

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Click on the 'Login' button
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
)
login_button.click()

# Verification step
time.sleep(1)  # Wait for error messages to be displayed
username_error = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "usernameError"))
)
password_error = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "passwordError"))
)

if username_error.text == "" or password_error.text == "":
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Error messages are not displayed for both username and password fields.")