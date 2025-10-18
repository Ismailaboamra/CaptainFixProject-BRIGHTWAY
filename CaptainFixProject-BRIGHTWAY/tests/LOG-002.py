from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open the login page
try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginForm")))
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to open the login page: " + str(e))

# Verification: Check if the total price is the sum of all added products
try:
    total_price = driver.find_element(By.ID, "totalPrice").text
    expected_total_price = "$0.00"  # Assuming no products are added yet
    assert total_price == expected_total_price, f"Expected total price to be {expected_total_price}, but got {total_price}"
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Total price verification failed: " + str(e))

# Error Detection: Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        assert not error_texts, f"Found inline errors: {error_texts}"
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Error detection failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the login page and enter the username
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter username: " + str(e))

# Verification step: Check if the total price is updated correctly
try:
    total_price = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "totalPrice"))).text
    # Assuming we have a function to calculate expected total price based on added products
    expected_total_price = "$0.00"  # Replace with actual expected value based on the context
    assert total_price == expected_total_price, f"Expected total price: {expected_total_price}, but got: {total_price}"
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Verification of total price failed: " + str(e))

# Error detection after the step
try:
    # Check for JavaScript alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()  # Accept the alert after verification
except Exception:
    alert_text = None

# Check for inline errors
try:
    username_error = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "usernameError"))).text
    if username_error:
        raise AssertionError(f"Inline error detected: {username_error}")
except Exception:
    pass  # No inline error found

# Check for toast/banner notifications
# Assuming there's a way to detect toast notifications, e.g., by checking a specific element
try:
    toast_message = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message"))).text
    if toast_message:
        raise AssertionError(f"Toast notification detected: {toast_message}")
except Exception:
    pass  # No toast notification found

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter password
try:
    password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.send_keys("emilyspass")
    
    # Verification: Check if the total price is updated correctly
    total_price = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "totalPrice"))
    ).text
    
    # Assuming we have a function to calculate expected total price based on added products
    expected_total_price = calculate_expected_total_price()  # This function needs to be defined based on your logic
    assert total_price == expected_total_price, f"Expected total price: {expected_total_price}, but got: {total_price}"

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

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
    
    # Verification: Check if the total price is the sum of all added products
    total_price_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "totalPrice"))
    )
    actual_total_price = total_price_element.text
    # Assuming we have a function to calculate expected total price
    expected_total_price = "$0.00"  # Replace with actual expected value based on added products
    assert actual_total_price == expected_total_price, f"Expected total price to be {expected_total_price}, but got {actual_total_price}"

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Add multiple products to the cart
try:
    # Assuming there are buttons to add products, we will simulate adding products
    # This is a placeholder for the actual product add buttons
    add_product_buttons = driver.find_elements(By.CSS_SELECTOR, ".btn-add-product")  # Replace with actual selector
    for button in add_product_buttons:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(button)).click()
    
    # After adding products, we need to check the total price
    total_price_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "totalPrice")))
    actual_total_price = total_price_element.text
    
    # Assuming we have a function to calculate expected total price based on added products
    expected_total_price = calculate_expected_total_price()  # Placeholder for actual calculation logic
    
    assert actual_total_price == expected_total_price, f"Expected total price: {expected_total_price}, but got: {actual_total_price}"

except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred while adding products to the cart: {str(e)}")

# Step 3: Error detection
try:
    # Check for JavaScript alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    # Compare alert text with expected
    assert alert_text == "Expected alert message", f"Unexpected alert message: {alert_text}"
    alert.accept()
except Exception as e:
    # Handle the case where no alert is present
    print("No alert present or unexpected alert:", str(e))

# Check for inline form errors, modals, and notifications
error_messages = driver.find_elements(By.CSS_SELECTOR, ".error-message")
for error in error_messages:
    assert error.text == "", f"Unexpected error message found: {error.text}"

# Check for toast/banner notifications
toast_notifications = driver.find_elements(By.CSS_SELECTOR, ".toast-notification")  # Replace with actual selector
for toast in toast_notifications:
    assert toast.is_displayed(), "Toast notification is displayed unexpectedly."

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Check the total price in the cart summary
try:
    total_price_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "totalPrice"))
    )
    actual_total_price = total_price_element.text
    # Assuming you have a way to calculate the expected total price
    expected_total_price = "$0.00"  # Replace with actual expected value

    assert actual_total_price == expected_total_price, f"Expected total price to be {expected_total_price}, but got {actual_total_price}"

except AssertionError as e:
    driver.save_screenshot('error_screenshot.png')
    raise e

# Step 3: Error detection (if any)
try:
    error_messages = []
    inline_errors = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in inline_errors:
        if error.is_displayed():
            error_messages.append(error.text)

    # Check for any JavaScript alerts
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        error_messages.append(alert_text)
        alert.accept()
    except:
        pass  # No alert present

    # Check for toast/banner notifications (if any)
    # Assuming there's a class for notifications
    notifications = driver.find_elements(By.CLASS_NAME, "notification")
    for notification in notifications:
        if notification.is_displayed():
            error_messages.append(notification.text)

    # Compare detected errors to expected error messages
    expected_errors = []  # Define expected errors here
    assert error_messages == expected_errors, f"Detected errors: {error_messages}, expected: {expected_errors}"

except AssertionError as e:
    driver.save_screenshot('error_screenshot.png')
    raise e