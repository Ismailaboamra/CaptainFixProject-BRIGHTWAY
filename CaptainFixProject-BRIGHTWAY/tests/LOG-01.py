from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that the total items in the cart reflect the number of products added
    total_items = driver.find_element(By.ID, "totalItems").text
    expected_total_items = "0"  # Assuming no products have been added yet
    assert total_items == expected_total_items, f"Expected total items to be {expected_total_items}, but got {total_items}"

except Exception as e:
    # Handle any errors or alerts
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert detected: {alert_text}")
    except:
        # Check for inline errors or notifications
        error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
        for error in error_messages:
            if error.is_displayed():
                raise AssertionError(f"Inline error detected: {error.text}")

    # If no alert or inline errors, take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An unexpected error occurred: {str(e)}")

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
    # Check for any errors after entering the username
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message:
        raise AssertionError(f"Error message displayed: {error_message}")
except Exception as e:
    driver.save_screenshot("error_check_username.png")
    raise AssertionError("Failed to check for username error: " + str(e))

try:
    # Submit the login form
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm"))).submit()
except Exception as e:
    driver.save_screenshot("error_login_submit.png")
    raise AssertionError("Failed to submit login form: " + str(e))

try:
    # Wait for the shop page to load and verify the total items in the cart
    total_items = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalItems"))).text
    if total_items != "0":  # Assuming we expect the total items to be 0 initially
        raise AssertionError(f"Expected total items to be 0, but got {total_items}")
except Exception as e:
    driver.save_screenshot("error_check_total_items.png")
    raise AssertionError("Failed to verify total items in the cart: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
    
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
    
    # Wait for the cart count to be updated
    cart_count_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount")))
    actual_cart_count = cart_count_element.text
    
    # Verify the expected result
    expected_cart_count = "0"  # Assuming no products are added yet, adjust as necessary
    if actual_cart_count != expected_cart_count:
        raise AssertionError(f"Expected cart count: {expected_cart_count}, but got: {actual_cart_count}")

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
    driver.save_screenshot("error_screenshot.png")
    raise e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
except Exception as e:
    driver.save_screenshot('error_click_login_button.png')
    raise AssertionError("Failed to click the Login button") from e

# Verify if the total items in the cart reflect the number of products added
try:
    total_items = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalItems")))
    actual_total_items = total_items.text
    expected_total_items = "0"  # Adjust this value based on the expected number of products added

    if actual_total_items != expected_total_items:
        raise AssertionError(f"Expected total items: {expected_total_items}, but got: {actual_total_items}")
except Exception as e:
    driver.save_screenshot('error_verifying_total_items.png')
    raise AssertionError("Failed to verify total items in the cart") from e

# Check for any alerts or error messages
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = ""  # Define the expected alert text if any
    if alert_text != expected_alert_text:
        driver.save_screenshot('error_alert.png')
        raise AssertionError(f"Unexpected alert text: {alert_text}")
    alert.accept()
except Exception as e:
    # No alert was present, continue checking for inline errors
    pass

# Check for inline form errors
try:
    username_error = driver.find_element(By.ID, "usernameError").text
    password_error = driver.find_element(By.ID, "passwordError").text
    if username_error or password_error:
        driver.save_screenshot('error_inline_form.png')
        raise AssertionError(f"Inline errors found: {username_error}, {password_error}")
except Exception as e:
    # No inline errors found
    pass

# Check for toast or banner notifications
# Assuming there's a way to identify toast notifications, e.g., by a specific class or ID
try:
    toast_notifications = driver.find_elements(By.CSS_SELECTOR, ".toast-notification")  # Adjust selector as needed
    if toast_notifications:
        driver.save_screenshot('error_toast_notifications.png')
        raise AssertionError("Toast notifications are present.")
except Exception as e:
    # No toast notifications found
    pass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Assuming there is a way to add a product to the cart, for example, clicking a button
    # This part of the code would depend on the actual implementation of the product addition
    # Here, we will simulate clicking a button to add a product to the cart
    add_product_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary.btn-checkout")))
    add_product_button.click()
    
    # Wait for the cart count to update
    cart_count = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount")))
    actual_cart_count = cart_count.text

    # Verify the expected result
    expected_cart_count = "1"  # Assuming we are adding one product
    if actual_cart_count != expected_cart_count:
        raise AssertionError(f"Expected cart count: {expected_cart_count}, but got: {actual_cart_count}")

except Exception as e:
    # Handle any alerts or errors
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        print(f"Alert detected: {alert_text}")
    except:
        print("No alert detected.")

    # Check for inline errors or notifications
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            print(f"Error message detected: {error.text}")
            raise AssertionError(f"Error message: {error.text}")

    # Take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")
    raise e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the total items element to be present
    total_items_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "totalItems"))
    )
    # Get the actual total items in the cart
    actual_total_items = total_items_element.text

    # Verify the expected result
    expected_total_items = "0"  # Replace with the expected number of items if known
    if actual_total_items != expected_total_items:
        raise AssertionError(f"Expected total items: {expected_total_items}, but got: {actual_total_items}")

except Exception as e:
    # Handle any errors that may occur
    print(f"An error occurred: {str(e)}")
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Test failed due to an unexpected error.")