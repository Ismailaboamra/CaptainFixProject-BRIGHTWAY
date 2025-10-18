from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that the user is on the login page
    assert driver.find_element(By.ID, "loginPage").is_displayed(), "Login page is not displayed"
    
    # Simulate opening the login page (if needed, otherwise this step is already done)
    # This step is just to ensure we are on the login page
    print("Login page opened successfully.")

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
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Test failed due to: {str(e)}")

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
    # Wait for the password input to be present and enter a dummy password (not specified in the step)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("dummyPassword")
except Exception as e:
    driver.save_screenshot("error_password_input.png")
    raise AssertionError("Failed to enter password: " + str(e))

try:
    # Wait for the login button to be present and click it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot("error_login_button.png")
    raise AssertionError("Failed to click login button: " + str(e))

# Verify if the user is redirected to the shop page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    actual_result = driver.find_element(By.ID, "shopPage").is_displayed()
    if not actual_result:
        raise AssertionError("User is not redirected to the shop page.")
except Exception as e:
    driver.save_screenshot("error_redirect.png")
    raise AssertionError("Failed to verify redirection to shop page: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input field to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
    
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
    
    # Wait for the shop page to be visible
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "shopPage")))
    
    # Verification step: Check if the user is redirected to the shop page
    if not driver.find_element(By.ID, "shopPage").is_displayed():
        raise AssertionError("User is not redirected to the shop page.")
    
except Exception as e:
    # Handle any alerts that may appear
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert appeared with text: {alert_text}")
    except:
        # If no alert appears, take a screenshot for debugging
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError("An error occurred during the test execution.") from e

# Check for any inline errors or notifications
error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
if error_messages:
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Inline error message displayed: {error.text}")

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
    
    # Take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")
    raise e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Cart button
    cart_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "cartBtn")))
    cart_button.click()
except Exception as e:
    driver.save_screenshot('error_click_cart_button.png')
    raise AssertionError(f"Failed to click the Cart button: {str(e)}")

try:
    # Verify redirection to the shop page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html", "User is not redirected back to the shop page."
except AssertionError as ae:
    driver.save_screenshot('error_redirect_shop_page.png')
    raise AssertionError(f"Verification failed: {str(ae)}")
except Exception as e:
    driver.save_screenshot('error_verify_redirect.png')
    raise AssertionError(f"Failed to verify redirection: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Continue Shopping button
    continue_shopping_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "backToShopFromCart"))
    )
    continue_shopping_button.click()
except Exception as e:
    driver.save_screenshot('error_continue_shopping.png')
    raise AssertionError(f"Failed to click Continue Shopping button: {str(e)}")

try:
    # Verify redirection to the shop page
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "shopPage"))
    )
    actual_page = driver.find_element(By.ID, "shopPage")
    if not actual_page.is_displayed():
        raise AssertionError("User is not redirected back to the shop page.")
except Exception as e:
    driver.save_screenshot('error_verification.png')
    raise AssertionError(f"Verification failed: {str(e)}")

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        for error in error_messages:
            if error.is_displayed():
                raise AssertionError(f"Detected error message: {error.text}")
except Exception as e:
    driver.save_screenshot('error_detection.png')
    raise AssertionError(f"Error detection failed: {str(e)}")