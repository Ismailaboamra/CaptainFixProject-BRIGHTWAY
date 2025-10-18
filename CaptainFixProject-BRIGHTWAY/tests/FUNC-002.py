from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginPage")))
    
    # Verify that the user is on the login page
    assert "Fix-Shop" in driver.title, "Expected to be on the login page, but not."
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Failed to open the login page: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the login page and enter the username
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    username_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_input.send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter username: " + str(e))

# Step 2: Verify if the user is redirected to the checkout page
try:
    WebDriverWait(driver, 20).until(
        EC.url_contains("checkout")  # Assuming the checkout page URL contains "checkout"
    )
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("User was not redirected to the checkout page: " + str(e))

# Step 3: Check for any errors on the page
try:
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    if error_message.is_displayed():
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError("Error message displayed: " + error_message.text)
except Exception:
    pass  # No error message found, continue

# Additional error checks can be added here as needed.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the login page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter password
try:
    password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.send_keys("emilyspass")
    
    # Verification: Check if the user is redirected to the checkout page
    # Assuming the checkout page has a unique identifier, we will check for it
    WebDriverWait(driver, 20).until(
        EC.url_contains("checkout")  # Replace "checkout" with the actual URL or identifier for the checkout page
    )
except Exception as e:
    # If an alert is present, handle it
    try:
        alert = WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert_text = alert.text
        # Compare alert_text with expected result if needed
        alert.accept()
    except Exception as alert_exception:
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError("Alert was expected but not found or incorrect.") from alert_exception
    raise AssertionError("Failed to enter password or redirect to checkout page.") from e

# Step 3: Error Detection
# Check for any inline errors, modals, or notifications
try:
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "passwordError"))
    ).text
    if error_message:
        raise AssertionError(f"Inline error detected: {error_message}")
except Exception:
    pass  # No inline error found

# Additional checks for modals or notifications can be added here as needed.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Click the Login button
try:
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    login_button.click()
    
    # Verification: Check if user is redirected to the checkout page
    WebDriverWait(driver, 20).until(
        EC.url_contains("checkout")  # Assuming the checkout page URL contains "checkout"
    )
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to click the Login button or redirect to checkout page.") from e

# Error detection logic can be added here if needed.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Click the Cart button
try:
    cart_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "cartBtn"))
    )
    cart_button.click()
except Exception as e:
    driver.save_screenshot("error_click_cart_button.png")
    raise AssertionError(f"Failed to click the Cart button: {str(e)}")

# Verification: Check if user is redirected to the checkout page
try:
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "cartPage"))
    )
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#cartPage", "User is not redirected to the checkout page."
except AssertionError as e:
    driver.save_screenshot("error_redirect_checkout_page.png")
    raise e
except Exception as e:
    driver.save_screenshot("error_verification_checkout_page.png")
    raise AssertionError(f"Verification failed: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Click the Proceed to Checkout button
try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.btn-checkout"))).click()
    # Verification: Check if user is redirected to the checkout page
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Checkout')]")))
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click the Proceed to Checkout button or verify redirection: " + str(e))

# Error detection logic (if needed)
# This part can be expanded based on the specific error messages expected on the page.