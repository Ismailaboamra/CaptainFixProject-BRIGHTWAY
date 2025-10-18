driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the login page to be visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginPage")))

# Perform action to trigger error message (e.g., submit the form with invalid data)
username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))

username_input.send_keys("invalidUser")
password_input.send_keys("invalidPass")
login_button.click()

# Verify that the error message is displayed
error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "passwordError")))

if error_message.is_displayed():
    print("Error message is displayed for invalid password.")
else:
    driver.save_screenshot("error_message_not_displayed.png")
    raise AssertionError("Expected error message for invalid password was not displayed.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Enter valid username
username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
username_input.send_keys("emilys")

# Submit the form
login_form = driver.find_element(By.ID, "loginForm")
login_form.submit()

# Verify that the error message for invalid password is displayed
error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "passwordError")))
if error_message.is_displayed() == False:
    driver.save_screenshot('error_message_not_displayed.png')
    raise AssertionError("Expected error message for invalid password is not displayed.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D9%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Enter invalid password
password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
password_input.send_keys("wrongpass")

# Submit the form
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
login_button.click()

# Wait for the error message to be visible
error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "passwordError")))

# Verify the expected result
if error_message.is_displayed():
    print("Error message is displayed for invalid password.")
else:
    driver.save_screenshot("error_message_not_displayed.png")
    raise AssertionError("Expected error message for invalid password was not displayed.")

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
if error_message.is_displayed() == False:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Expected error message for invalid password is not displayed.")