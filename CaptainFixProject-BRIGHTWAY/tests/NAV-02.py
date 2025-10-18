from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that the user is on the login page
    assert driver.find_element(By.ID, "loginPage").is_displayed(), "Login page is not displayed"
    
    # Simulate opening the login page (if there's a button or link to click, it would go here)
    # For this step, we assume the login page is already open after the initial get.

    # Check if the user is redirected back to the shop page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    
    # Verify that the user is redirected to the shop page
    assert driver.find_element(By.ID, "shopPage").is_displayed(), "User is not redirected to the shop page"

except Exception as e:
    # Handle any alerts or popups
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        print(f"Alert detected: {alert_text}")
    except:
        print("No alert detected.")
    
    # Take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_username_input.png")
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Wait for the login button to be clickable and click it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot("error_login_button.png")
    raise AssertionError("Failed to click login button: " + str(e))

# Verify redirection to the shop page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    actual_page = driver.find_element(By.ID, "shopPage").is_displayed()
    if not actual_page:
        raise AssertionError("User is not redirected to the shop page.")
except Exception as e:
    driver.save_screenshot("error_redirect.png")
    raise AssertionError("Redirection verification failed: " + str(e))

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        raise AssertionError(f"Detected error messages: {error_texts}")
except Exception as e:
    driver.save_screenshot("error_check.png")
    raise AssertionError("Error checking failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page (if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input field to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
    
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
    
    # Wait for the shop page to be visible
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "shopPage")))
    
    # Verification step: Check if the user is redirected to the shop page
    actual_page_state = driver.find_element(By.ID, "shopPage").is_displayed()
    expected_result = True  # We expect the shop page to be displayed
    
    if actual_page_state != expected_result:
        raise AssertionError("User is not redirected to the shop page as expected.")
    
except Exception as e:
    # Handle any alerts or popups
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert appeared: {alert_text}")
    except:
        # If no alert appears, take a screenshot for debugging
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError("An error occurred during the test execution.") from e

# Detect and verify any errors on the page
error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
for error in error_messages:
    if error.is_displayed():
        error_text = error.text
        raise AssertionError(f"Detected error message: {error_text}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
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
    
    # Take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")
    raise e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the "Back to Shop" button to be present and click it
    back_to_shop_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "backToShopBtn")))
    back_to_shop_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to click 'Back to Shop' button: {str(e)}")

try:
    # Verify that the user is redirected back to the shop page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    actual_page_state = driver.find_element(By.ID, "shopPage").is_displayed()
    assert actual_page_state, "User is not redirected back to the shop page."
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Verification failed: {str(e)}")