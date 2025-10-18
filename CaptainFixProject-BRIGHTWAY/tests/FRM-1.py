from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%A7%D9%87%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the login form to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm")))
    
    # Check if the user is logged in successfully by verifying the presence of the shop page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    
    # Verification step
    shop_page = driver.find_element(By.ID, "shopPage")
    if not shop_page.is_displayed():
        raise AssertionError("User is not logged in successfully. Shop page is not displayed.")
    
except Exception as e:
    # Handle any alerts or popups
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert appeared: {alert_text}")
    except:
        # If no alert is present, take a screenshot for debugging
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError("An error occurred: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username field to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys('emilys')
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Check for any errors on the page after entering the username
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message:
        raise AssertionError(f"Error detected: {error_message}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to check for errors: " + str(e))

try:
    # Submit the login form
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click login button: " + str(e))

try:
    # Wait for the user name element to be present on the main shop page to verify successful login
    user_name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName"))).text
    if not user_name:
        raise AssertionError("User is not logged in successfully.")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify successful login: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password field to be present and enter the password
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys('emilyspass')
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter password: " + str(e))

try:
    # Wait for the login button to be clickable and click it
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click login button: " + str(e))

# Check for any alerts after clicking the login button
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Login successful"  # Assuming this is the expected alert text
    if alert_text != expected_alert_text:
        driver.save_screenshot('error_screenshot.png')
        raise AssertionError(f"Unexpected alert text: {alert_text}")
    alert.accept()
except Exception as e:
    # No alert was present, continue with verification
    pass

# Verify successful login by checking the presence of the user's name or another indicator
try:
    user_name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName")))
    if user_name.text == "":
        driver.save_screenshot('error_screenshot.png')
        raise AssertionError("User is not logged in successfully.")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify user login: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
    
    # Wait for potential alert and verify
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "User is logged in successfully."  # Adjust this based on actual alert text if needed
    if alert_text == expected_alert_text:
        alert.accept()
    else:
        driver.save_screenshot("alert_error.png")
        raise AssertionError(f"Unexpected alert text: {alert_text}")

except Exception as e:
    driver.save_screenshot("error.png")
    raise AssertionError(f"An error occurred: {str(e)}")

# Verify user is logged in successfully
try:
    user_name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "userName")))
    if user_name.is_displayed():
        actual_user_name = user_name.text
        expected_user_name = "Expected User Name"  # Replace with the actual expected user name
        if actual_user_name != expected_user_name:
            raise AssertionError(f"Expected user name '{expected_user_name}' but got '{actual_user_name}'")
    else:
        raise AssertionError("User name element is not displayed.")
except Exception as e:
    driver.save_screenshot("verification_error.png")
    raise AssertionError(f"Verification failed: {str(e)}")