from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that we are on the login page
    assert driver.find_element(By.ID, "loginPage").is_displayed(), "Login page is not displayed"
    
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input field to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_username_input.png")
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Wait for the login button to be present and click it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot("error_login_button_click.png")
    raise AssertionError("Failed to click login button: " + str(e))

# Check for any alerts after clicking the login button
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()  # Accept the alert after verification
except Exception as e:
    alert_text = None  # No alert present

# Verify if the user is redirected to the checkout page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-summary")))
    actual_result = driver.find_element(By.CSS_SELECTOR, ".cart-summary").is_displayed()
    if not actual_result:
        raise AssertionError("User is not redirected to the checkout page.")
except Exception as e:
    driver.save_screenshot("error_checkout_page_verification.png")
    raise AssertionError("Failed to verify redirection to checkout page: " + str(e))

# Detect any errors on the page
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

# Log detected error messages
if error_messages:
    for message in error_messages:
        print("Detected error message:", message)
    raise AssertionError("Errors detected on the page: " + ", ".join(error_messages))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter password: " + str(e))

try:
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to click login button: " + str(e))

# Verify if the user is redirected to the checkout page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "cart-summary")))
    actual_title = driver.title
    expected_title = "Checkout - Fix-Shop"  # Assuming the title of the checkout page is known
    if actual_title != expected_title:
        raise AssertionError(f"Expected title '{expected_title}' but got '{actual_title}'")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("User was not redirected to the checkout page: " + str(e))

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Error message displayed: {error.text}")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Error checking failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for the page to load and verify redirection to the checkout page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    
    # Verification step
    actual_page_id = driver.current_url
    expected_page_id = "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#cartPage"
    
    if actual_page_id != expected_page_id:
        raise AssertionError(f"Expected to be on checkout page, but was on {actual_page_id}")

except Exception as e:
    # Handle any alerts or errors
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert appeared with text: {alert_text}")
    except:
        # Check for inline errors or notifications
        error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
        for error in error_messages:
            if error.is_displayed():
                raise AssertionError(f"Error message displayed: {error.text}")
    
    # Take a screenshot for debugging
    driver.save_screenshot('error_screenshot.png')
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
    
    # Wait for the page to load and verify redirection to the checkout page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    
    # Verification step
    actual_page_id = driver.current_url
    expected_page_id = "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#cartPage"
    
    if actual_page_id != expected_page_id:
        raise AssertionError(f"Expected to be on checkout page, but was on {actual_page_id}")

except Exception as e:
    # Handle any alerts or errors
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert appeared with text: {alert_text}")
    except:
        # Check for inline errors or notifications
        error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
        for error in error_messages:
            if error.is_displayed():
                raise AssertionError(f"Inline error message displayed: {error.text}")
    
    # If no alert or inline errors, take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("An unexpected error occurred.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Proceed to Checkout button
    proceed_to_checkout_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.btn-checkout"))
    )
    proceed_to_checkout_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to click the Proceed to Checkout button: {str(e)}")

# Verify redirection to the checkout page
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "checkoutPage"))  # Assuming the checkout page has an ID of 'checkoutPage'
    )
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("User was not redirected to the checkout page.")

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        if error_texts:
            raise AssertionError(f"Detected errors on the page: {error_texts}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Error checking for inline errors: {str(e)}")