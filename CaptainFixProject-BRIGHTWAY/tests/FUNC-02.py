from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Verify that the login page is displayed
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    assert driver.find_element(By.ID, "loginPage").is_displayed(), "Login page is not displayed."

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
    expected_alert_text = "User is prompted to proceed with checkout."
    if alert_text != expected_alert_text:
        driver.save_screenshot("error_alert_text.png")
        raise AssertionError(f"Unexpected alert text: {alert_text}. Expected: {expected_alert_text}")
    alert.accept()
except Exception as e:
    driver.save_screenshot("error_alert.png")
    raise AssertionError("No alert appeared or an error occurred: " + str(e))

# Verify the expected result on the page
try:
    # Check if the user is on the cart page or a relevant page indicating checkout
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    actual_text = driver.find_element(By.ID, "cartPage").text
    expected_text = "Your Cart"
    if expected_text not in actual_text:
        driver.save_screenshot("error_checkout_verification.png")
        raise AssertionError(f"Checkout not prompted. Actual text: {actual_text}. Expected to see: {expected_text}")
except Exception as e:
    driver.save_screenshot("error_checkout_verification.png")
    raise AssertionError("Failed to verify checkout prompt: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input field to be present and enter the password
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

# Check for any alerts after clicking the login button
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "User is prompted to proceed with checkout."
    if alert_text != expected_alert_text:
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError(f"Unexpected alert text: {alert_text}")
    alert.accept()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("No alert appeared or failed to handle alert: " + str(e))

# Verify the expected result after login
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-summary")))
    actual_text = driver.find_element(By.CSS_SELECTOR, ".cart-summary").text
    expected_text = "Proceed to Checkout"
    if expected_text not in actual_text:
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError(f"Expected text not found. Actual text: {actual_text}")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Verification failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for any potential alert and verify its presence
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    
    # Expected alert text (modify this based on the actual expected alert text)
    expected_alert_text = "User is prompted to proceed with checkout."
    
    # Verify the alert text
    if alert_text != expected_alert_text:
        driver.save_screenshot('alert_verification_failed.png')
        raise AssertionError(f"Expected alert text '{expected_alert_text}' but got '{alert_text}'")
    
    # Accept the alert
    alert.accept()

except Exception as e:
    # Handle any errors that occur during the process
    driver.save_screenshot('error_occurred.png')
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Cart button
    cart_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "cartBtn")))
    cart_button.click()
    
    # Wait for the alert to be present
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    
    # Verify the alert text
    expected_alert_text = "Proceed to checkout?"  # Assuming this is the expected alert text
    if alert_text != expected_alert_text:
        driver.save_screenshot('alert_verification_failed.png')
        raise AssertionError(f"Expected alert text '{expected_alert_text}' but got '{alert_text}'")
    
    # Accept the alert
    alert.accept()

except Exception as e:
    # Handle any errors that occur during the process
    driver.save_screenshot('error_occurred.png')
    raise AssertionError(f"An error occurred: {str(e)}")

# Check for any inline errors or notifications after the action
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartItems")))
    if error_message.is_displayed():
        error_text = error_message.text
        expected_error_text = ""  # Define expected error text if any
        if error_text != expected_error_text:
            raise AssertionError(f"Unexpected error message: {error_text}")
except Exception as e:
    # Log any detected errors
    print(f"No errors detected or an error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the Proceed to Checkout button to be present and click it
    proceed_to_checkout_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary.btn-checkout"))
    )
    proceed_to_checkout_button.click()
    
    # Wait for any alert to be present
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    
    # Verify the alert text
    expected_alert_text = "User is prompted to proceed with checkout."
    if alert_text != expected_alert_text:
        driver.save_screenshot('alert_verification_failed.png')
        raise AssertionError(f"Expected alert text: '{expected_alert_text}', but got: '{alert_text}'")
    
    # Accept the alert
    alert.accept()

except Exception as e:
    # Handle any errors that occur during the process
    driver.save_screenshot('error_occurred.png')
    raise AssertionError(f"An error occurred: {str(e)}")