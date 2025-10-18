from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that the login page is displayed
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
    # Wait for the username field to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys('emilys')
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click login button: " + str(e))

# Check for any alerts after clicking the login button
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
except Exception as e:
    alert_text = None

# Verify if the user is redirected to the checkout page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "cart-summary")))
    if alert_text:
        print("Alert text: ", alert_text)
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("User was not redirected to the checkout page: " + str(e))

# Check for any error messages on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            print("Error message found: ", error.text)
            raise AssertionError("Error message displayed: " + error.text)
except Exception as e:
    print("No error messages found.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password field to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys('emilyspass')
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter password: " + str(e))

try:
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click login button: " + str(e))

# Check for any alerts after clicking the login button
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Expected alert message"  # Replace with the actual expected alert message
    if alert_text != expected_alert_text:
        driver.save_screenshot('error_screenshot.png')
        raise AssertionError(f"Unexpected alert text: {alert_text}")
    alert.accept()
except Exception as e:
    pass  # No alert present, continue

# Verify if the user is redirected to the checkout page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-summary")))
    actual_page_title = driver.title
    expected_page_title = "Checkout - Fix-Shop"  # Replace with the actual expected title of the checkout page
    if actual_page_title != expected_page_title:
        driver.save_screenshot('error_screenshot.png')
        raise AssertionError(f"User not redirected to checkout page. Actual title: {actual_page_title}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify redirection to checkout page: " + str(e))

# Detect and verify any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            error_text = error.text
            expected_error_text = "Expected error message"  # Replace with the actual expected error message
            if error_text != expected_error_text:
                driver.save_screenshot('error_screenshot.png')
                raise AssertionError(f"Unexpected error message: {error_text}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Error detection failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
    
    # Wait for the page to load and verify redirection to the checkout page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    
    # Verification step
    actual_page_id = driver.find_element(By.ID, "cartPage").is_displayed()
    if not actual_page_id:
        raise AssertionError("User is not redirected to the checkout page.")
    
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
        raise AssertionError("An error occurred during the login process.") from e

# Detect and verify any errors on the page
error_messages = driver.find_elements(By.CSS_SELECTOR, ".error-message")
for error in error_messages:
    if error.is_displayed():
        error_text = error.text
        raise AssertionError(f"Inline error detected: {error_text}")

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
    raise AssertionError("Failed to click the Cart button") from e

try:
    # Verify redirection to the checkout page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    actual_page = driver.current_url
    expected_page = "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#cartPage"
    if actual_page != expected_page:
        raise AssertionError(f"Expected to be on checkout page, but was on {actual_page}")
except Exception as e:
    driver.save_screenshot('error_verify_redirection.png')
    raise AssertionError("Failed to verify redirection to the checkout page") from e

# Detect and verify any errors on the page
try:
    error_messages = driver.find_elements(By.CSS_SELECTOR, ".error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Detected error message: {error.text}")
except Exception as e:
    driver.save_screenshot('error_detection.png')
    raise AssertionError("Failed to detect errors on the page") from e

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
    raise AssertionError("User is not redirected to the checkout page.")

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