from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%A7%D8%AA%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Check if the login page is displayed
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that the user is redirected to the shop page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    
    # Check for any errors on the page
    error_messages = driver.find_elements(By.CSS_SELECTOR, ".error-message")
    if error_messages:
        for error in error_messages:
            if error.is_displayed():
                print(f"Detected error: {error.text}")
                raise AssertionError(f"Unexpected error message: {error.text}")

    # Verification step
    if not driver.find_element(By.ID, "shopPage").is_displayed():
        raise AssertionError("User is not redirected to the shop page as expected.")

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

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
    # Check for any errors on the page after entering the username
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message:
        raise AssertionError(f"Error message displayed: {error_message}")
except Exception as e:
    driver.save_screenshot('error_check.png')
    raise AssertionError("Failed to check for errors: " + str(e))

try:
    # Wait for the login form to be present and submit the form
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm"))).submit()
except Exception as e:
    driver.save_screenshot('error_form_submit.png')
    raise AssertionError("Failed to submit the login form: " + str(e))

try:
    # Wait for the shop page to be visible
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "shopPage")))
    actual_result = driver.find_element(By.ID, "shopPage").is_displayed()
    assert actual_result, "User is not redirected to the shop page."
except Exception as e:
    driver.save_screenshot('error_redirect_check.png')
    raise AssertionError("Failed to verify redirection to shop page: " + str(e))

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
    raise AssertionError(f"Failed to enter password: {str(e)}")

try:
    # Wait for the login button to be clickable and click it
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to click login button: {str(e)}")

# Verify if the user is redirected to the shop page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    assert driver.find_element(By.ID, "shopPage").is_displayed(), "Shop page is not displayed."
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"User is not redirected to the shop page: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for the shop page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    
    # Verification step
    shop_page = driver.find_element(By.ID, "shopPage")
    if not shop_page.is_displayed():
        raise AssertionError("User is not redirected to the shop page.")
    
except Exception as e:
    # Handle any alerts or errors
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert appeared: {alert_text}")
    except:
        # Check for inline errors or notifications
        error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
        for error in error_messages:
            if error.is_displayed():
                raise AssertionError(f"Error message displayed: {error.text}")
    
    # If no alert or error, take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")
    raise e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Back to Shop button
    back_to_shop_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "backToShopBtn")))
    back_to_shop_button.click()
except Exception as e:
    driver.save_screenshot('error_click_back_to_shop.png')
    raise AssertionError(f"Failed to click the Back to Shop button: {str(e)}")

try:
    # Verify that the user is redirected back to the shop page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    actual_page_state = driver.find_element(By.ID, "shopPage").is_displayed()
    if not actual_page_state:
        raise AssertionError("User is not redirected back to the shop page.")
except Exception as e:
    driver.save_screenshot('error_verify_redirect.png')
    raise AssertionError(f"Verification of redirection failed: {str(e)}")

# Detect any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        if error_texts:
            raise AssertionError(f"Detected error messages: {error_texts}")
except Exception as e:
    driver.save_screenshot('error_detection_failed.png')
    raise AssertionError(f"Error detection failed: {str(e)}")