driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%A7%D8%AA%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the login page to be visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginPage")))

# Verify that the error message for invalid username is displayed
error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "usernameError")))

# Check if the error message is displayed
if not error_message.is_displayed():
    driver.save_screenshot('error_message_not_displayed.png')
    raise AssertionError("Expected error message for invalid username is not displayed.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Enter invalid username
username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
username_input.clear()
username_input.send_keys("invalidUser")

# Submit the form
login_form = driver.find_element(By.ID, "loginForm")
login_form.submit()

# Verification step
try:
    error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "usernameError")))
    if error_message.text == "":
        raise AssertionError("Expected error message for invalid username is not displayed.")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise e

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Enter valid password
password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "password"))
)
password_input.send_keys("emilyspass")

# Verify that the error message for invalid username is displayed
error_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "usernameError"))
)

if error_message.is_displayed() == False:
    driver.save_screenshot('error_message_not_displayed.png')
    raise AssertionError("Expected error message for invalid username is not displayed.")

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
    EC.visibility_of_element_located((By.ID, "usernameError"))
)
if error_message.is_displayed() == False:
    driver.save_screenshot('error_message_not_displayed.png')
    raise AssertionError("Expected error message is not displayed for invalid username.")