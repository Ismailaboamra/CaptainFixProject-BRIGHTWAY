from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Wait for the username element to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    
    # Verify the username displayed
    user_name_displayed = driver.find_element(By.ID, "userName").text
    expected_user_name = 'emilys'
    
    if user_name_displayed != expected_user_name:
        raise AssertionError(f"Expected user name '{expected_user_name}' but got '{user_name_displayed}'")
    
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input field to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys('emilys')
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to enter username: {str(e)}")

try:
    # Verify that the username entered matches the expected result
    actual_username = driver.find_element(By.ID, "username").get_attribute("value")
    expected_username = 'emilys'
    assert actual_username == expected_username, f"Expected username '{expected_username}' but got '{actual_username}'"
except AssertionError as e:
    driver.save_screenshot('verification_error_screenshot.png')
    raise e
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Verification failed: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password field to be present and enter the password
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys('emilyspass')
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to enter password: {str(e)}")

try:
    # Verify the user name displayed matches 'emilys'
    user_name_displayed = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName")))
    actual_user_name = user_name_displayed.text
    expected_user_name = 'emilys'
    assert actual_user_name == expected_user_name, f"Expected user name '{expected_user_name}', but got '{actual_user_name}'"
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Verification failed: {str(e)}")

# Check for any errors on the page
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    if error_message.is_displayed():
        error_text = error_message.text
        raise AssertionError(f"Error message displayed: {error_text}")
except Exception as e:
    pass  # No error message found, continue

# Check for JavaScript alerts
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()  # Accept the alert after verification
except Exception as e:
    pass  # No alert present, continue

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
except Exception as e:
    driver.save_screenshot('error_click_login_button.png')
    raise AssertionError("Failed to click the Login button") from e

try:
    # Wait for the user name to be displayed
    user_name_displayed = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName")))
    actual_user_name = user_name_displayed.text
    expected_user_name = 'emilys'
    
    # Verify the user name
    assert actual_user_name == expected_user_name, f"Expected user name '{expected_user_name}', but got '{actual_user_name}'"
except Exception as e:
    driver.save_screenshot('error_verify_user_name.png')
    raise AssertionError("Failed to verify the user name") from e

# Check for any errors on the page
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    if error_message.is_displayed():
        error_text = error_message.text
        raise AssertionError(f"Inline error detected: {error_text}")
except Exception as e:
    pass  # No inline error detected

# Additional checks for alerts or popups can be added here if necessary.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the user name element to be present
    user_name_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "userName"))
    )
    actual_user_name = user_name_element.text

    # Verify the user name
    expected_user_name = 'emilys'
    assert actual_user_name == expected_user_name, f"Expected user name '{expected_user_name}' but got '{actual_user_name}'"

except Exception as e:
    # Handle any errors and take a screenshot for debugging
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")