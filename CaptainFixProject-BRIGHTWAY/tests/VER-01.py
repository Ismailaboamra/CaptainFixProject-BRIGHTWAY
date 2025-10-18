from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%A7%D8%AA%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Verify that the login page is displayed
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Check if the username is displayed correctly in the navbar
    user_name_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName")))
    actual_user_name = user_name_element.text
    
    # Expected result (assuming the expected username is known, e.g., "Guest")
    expected_user_name = "Guest"  # Replace with the actual expected username if known
    
    if actual_user_name != expected_user_name:
        raise AssertionError(f"Expected username '{expected_user_name}' but got '{actual_user_name}'")
    
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
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Wait for the login button to be clickable and click it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click login button: " + str(e))

# Verify if the username is displayed correctly in the navbar
try:
    user_name_displayed = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName"))).text
    if user_name_displayed != "emilys":
        raise AssertionError(f"Expected username 'emilys', but got '{user_name_displayed}'")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify username display: " + str(e))

# Check for any errors on the page
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message:
        raise AssertionError(f"Error message displayed: '{error_message}'")
except Exception as e:
    pass  # No error message found, continue

try:
    alert = WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()
    raise AssertionError(f"Alert displayed: '{alert_text}'")
except Exception as e:
    pass  # No alert found, continue

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter password: " + str(e))

try:
    # Check for any errors on the page after entering the password
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError"))).text
    if error_message:
        raise AssertionError("Error message displayed: " + error_message)
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to check for error messages: " + str(e))

try:
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click login button: " + str(e))

try:
    # Wait for the user name to be displayed in the navbar
    user_name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName"))).text
    expected_user_name = "Your User Name"  # Replace with the actual expected user name after login
    if user_name != expected_user_name:
        raise AssertionError(f"Expected user name '{expected_user_name}' but got '{user_name}'")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify user name: " + str(e))

try:
    # Check for any alerts after login
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Login successful"  # Replace with the actual expected alert text
    if alert_text != expected_alert_text:
        raise AssertionError(f"Expected alert text '{expected_alert_text}' but got '{alert_text}'")
    alert.accept()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("No alert appeared or alert text did not match: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page (if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
except Exception as e:
    driver.save_screenshot('error_click_login_button.png')
    raise AssertionError(f"Failed to click the login button: {str(e)}")

try:
    # Wait for the user name to be displayed in the navbar
    user_name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName")))
    actual_user_name = user_name.text

    # Verify the expected result
    expected_user_name = "Expected User Name"  # Replace with the actual expected user name
    if actual_user_name != expected_user_name:
        raise AssertionError(f"Expected user name '{expected_user_name}' but got '{actual_user_name}'")
except Exception as e:
    driver.save_screenshot('error_verify_user_name.png')
    raise AssertionError(f"Failed to verify user name: {str(e)}")

# Check for any errors on the page
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    if error_message.is_displayed() and error_message.text:
        raise AssertionError(f"Error message displayed: {error_message.text}")
except Exception as e:
    pass  # No error message found, continue

try:
    alert = WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert_text = alert.text
    expected_alert_text = "Expected Alert Text"  # Replace with the actual expected alert text
    if alert_text != expected_alert_text:
        driver.save_screenshot('error_alert_text.png')
        raise AssertionError(f"Expected alert text '{expected_alert_text}' but got '{alert_text}'")
    alert.accept()
except Exception as e:
    pass  # No alert found, continue

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

    # Verify the expected result
    expected_user_name = "Expected User Name"  # Replace with the actual expected user name
    assert actual_user_name == expected_user_name, f"Expected user name '{expected_user_name}' but got '{actual_user_name}'"

except Exception as e:
    # Handle any alerts or popups
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        # Log alert text if needed
    except:
        pass  # No alert present

    # Take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")