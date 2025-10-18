from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that the cart count is updated correctly
    cart_count = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount")))
    actual_cart_count = cart_count.text
    
    # Expected cart count (assuming it should be 0 when on the login page)
    expected_cart_count = "0"
    
    if actual_cart_count != expected_cart_count:
        raise AssertionError(f"Expected cart count: {expected_cart_count}, but got: {actual_cart_count}")

except Exception as e:
    # Handle any errors that may occur
    print(f"An error occurred: {str(e)}")
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Test failed due to an unexpected error.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
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

# Verify the cart count is updated correctly
try:
    cart_count = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount"))).text
    if cart_count != "1":  # Assuming the cart count should be 1 after login
        raise AssertionError(f"Expected cart count to be '1', but got '{cart_count}'")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify cart count: " + str(e))

# Check for any alerts or error messages
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    # You can add verification for alert text if needed
except Exception as e:
    pass  # No alert present, continue

# Check for inline errors
try:
    username_error = driver.find_element(By.ID, "usernameError").text
    if username_error:
        raise AssertionError(f"Inline error detected: {username_error}")
except Exception as e:
    pass  # No inline error present, continue

# Check for any toast or banner notifications
# Assuming there's a way to detect toast notifications, you can add that check here if needed.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%A7%D8%AA%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

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

# Check for any alerts after login attempt
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
except Exception as e:
    alert_text = None

# Verify the cart count is updated correctly
try:
    cart_count = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount"))).text
    if cart_count != "1":  # Assuming the expected cart count after login is 1
        raise AssertionError(f"Expected cart count to be '1', but got '{cart_count}'")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to verify cart count: " + str(e))

# Check for any inline errors or notifications
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Inline error detected: {error.text}")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Error checking for inline messages: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for any potential alert and handle it
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
    except:
        alert_text = None

    # Verify the cart count is updated correctly
    cart_count = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount")))
    actual_cart_count = cart_count.text

    # Assuming the expected cart count after login is 1 (this should be defined based on the application logic)
    expected_cart_count = "1"  # Update this value based on the expected outcome after login

    if actual_cart_count != expected_cart_count:
        raise AssertionError(f"Expected cart count: {expected_cart_count}, but got: {actual_cart_count}")

except Exception as e:
    # Take a screenshot for debugging
    driver.save_screenshot('error_screenshot.png')
    raise e

# Check for any inline errors or notifications
error_messages = driver.find_elements(By.CSS_SELECTOR, ".error-message")
for error in error_messages:
    if error.is_displayed():
        raise AssertionError(f"Detected error message: {error.text}")

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
    # Verify the cart count is updated correctly
    cart_count = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount")))
    actual_cart_count = cart_count.text
    expected_cart_count = "1"  # Assuming the expected count after clicking is 1, adjust as necessary
    assert actual_cart_count == expected_cart_count, f"Expected cart count: {expected_cart_count}, but got: {actual_cart_count}"
except Exception as e:
    driver.save_screenshot('error_verify_cart_count.png')
    raise AssertionError(f"Failed to verify cart count: {str(e)}")

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Detected error message: {error.text}")
except Exception as e:
    driver.save_screenshot('error_checking_for_errors.png')
    raise AssertionError(f"Failed to check for errors: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the cart count element to be present
    cart_count_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "cartCount"))
    )
    # Get the actual cart count
    actual_cart_count = cart_count_element.text

    # Verify the cart count reflects the number of items (assuming it should be 0 initially)
    expected_cart_count = "0"  # Update this value based on the expected number of items
    if actual_cart_count != expected_cart_count:
        raise AssertionError(f"Expected cart count: {expected_cart_count}, but got: {actual_cart_count}")

except Exception as e:
    # Handle any errors that may occur
    print(f"An error occurred: {str(e)}")
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Test failed due to an unexpected error.")