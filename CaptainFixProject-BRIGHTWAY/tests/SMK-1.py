from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that we are on the login page
    assert driver.find_element(By.ID, "loginPage").is_displayed(), "Login page is not displayed"
    
    # Simulate opening the login page (if needed, otherwise this step is already done)
    # This step is not necessary since we are already on the login page after driver.get()

    # Check for any errors on the page
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            print(f"Detected error: {error.text}")
            raise AssertionError(f"Unexpected error message: {error.text}")

    # After opening the login page, we expect to be redirected to the shop page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    
    # Verify that the user is redirected to the shop page
    assert driver.find_element(By.ID, "shopPage").is_displayed(), "User is not redirected to the shop page"

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Test failed due to: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username field to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys('emilys')
except Exception as e:
    driver.save_screenshot('error_username_input.png')
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Wait for the login button to be clickable and click it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('error_login_button_click.png')
    raise AssertionError("Failed to click login button: " + str(e))

# Check for any alerts after the action
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
except Exception as e:
    alert_text = None

# Verify redirection to the shop page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    actual_result = driver.find_element(By.ID, "shopPage").is_displayed()
    if not actual_result:
        raise AssertionError("User is not redirected to the shop page.")
except Exception as e:
    driver.save_screenshot('error_shop_page_verification.png')
    raise AssertionError("Failed to verify redirection to shop page: " + str(e))

# Log any detected errors on the page
error_messages = []
try:
    username_error = driver.find_element(By.ID, "usernameError").text
    if username_error:
        error_messages.append(username_error)
except Exception:
    pass

try:
    password_error = driver.find_element(By.ID, "passwordError").text
    if password_error:
        error_messages.append(password_error)
except Exception:
    pass

if alert_text:
    error_messages.append(alert_text)

if error_messages:
    raise AssertionError("Detected errors: " + ", ".join(error_messages))

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

# Verify if the user is redirected to the shop page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    actual_page = driver.find_element(By.ID, "shopPage").is_displayed()
    if not actual_page:
        raise AssertionError("User is not redirected to the shop page.")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify redirection to shop page: " + str(e))

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        if error_texts:
            raise AssertionError("Detected error messages: " + ", ".join(error_texts))
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to check for error messages: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
    
    # Wait for the shop page to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    
    # Verification step: Check if the user is redirected to the shop page
    shop_page = driver.find_element(By.ID, "shopPage")
    if not shop_page.is_displayed():
        raise AssertionError("User is not redirected to the shop page.")
    
except Exception as e:
    # Handle any alert or popup gracefully
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert appeared: {alert_text}")
    except:
        # Take a screenshot for debugging
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError(f"An error occurred: {str(e)}")