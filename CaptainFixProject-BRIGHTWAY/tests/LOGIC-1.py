from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify the total items in the cart
    total_items = driver.find_element(By.ID, "totalItems").text
    expected_items = "0"  # Assuming no items are added yet
    assert total_items == expected_items, f"Expected total items to be {expected_items}, but got {total_items}"

except Exception as e:
    # Check for any alerts
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert detected: {alert_text}")
    except:
        pass  # No alert present

    # Check for inline errors
    username_error = driver.find_element(By.ID, "usernameError").text
    password_error = driver.find_element(By.ID, "passwordError").text
    if username_error or password_error:
        raise AssertionError(f"Inline errors detected: Username error - {username_error}, Password error - {password_error}")

    # Log the exception for debugging
    print(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input field to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Check for any errors after entering the username
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message:
        raise AssertionError(f"Error message displayed: {error_message}")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to check for username error: " + str(e))

try:
    # Submit the login form
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm"))).submit()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to submit the login form: " + str(e))

try:
    # Wait for the cart count to be updated and verify the expected result
    cart_count = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount"))).text
    if cart_count != "1":  # Assuming 1 item is added to the cart
        raise AssertionError(f"Expected cart count to be 1, but got {cart_count}")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to verify cart count: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
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

# Check for any alerts after login
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    # You can add verification for alert text if needed
except Exception:
    pass  # No alert present

# Verify the total items in the cart
try:
    total_items = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalItems"))).text
    expected_total_items = "1"  # Assuming 1 item was added for this test case
    if total_items != expected_total_items:
        raise AssertionError(f"Expected total items: {expected_total_items}, but got: {total_items}")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to verify total items in the cart: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for any potential alert and verify its presence
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        # Assuming expected alert text is known, replace 'Expected alert text' with the actual expected text
        if alert_text != 'Expected alert text':
            driver.save_screenshot('alert_error.png')
            raise AssertionError(f"Unexpected alert text: {alert_text}")
        alert.accept()
    except:
        pass  # No alert present

    # Verify the total items in the cart
    total_items = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalItems")))
    actual_total_items = total_items.text
    
    # Assuming expected total items is known, replace 'Expected total items' with the actual expected value
    expected_total_items = '1'  # Example expected value
    if actual_total_items != expected_total_items:
        raise AssertionError(f"Expected total items: {expected_total_items}, but got: {actual_total_items}")

except Exception as e:
    driver.save_screenshot('error.png')
    raise e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Assuming there is a product to add, we will simulate adding a product to the cart
    # This step would typically involve clicking a button or link to add a product
    # For demonstration, let's assume we have a button with id 'addProductBtn' to add a product
    add_product_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "addProductBtn")))
    add_product_button.click()
    
    # Wait for the cart count to update
    cart_count = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount")))
    actual_cart_count = int(cart_count.text)

    # Verify the expected result
    expected_cart_count = 1  # Assuming we are adding one product
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

    # If no alert or error messages, take a screenshot for debugging
    driver.save_screenshot('error_screenshot.png')
    raise e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the total items element to be present and get its text
    total_items_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "totalItems"))
    )
    total_items = total_items_element.text

    # Verify the total items in the cart
    expected_total_items = "0"  # Replace with the expected count if known
    if total_items != expected_total_items:
        raise AssertionError(f"Expected total items: {expected_total_items}, but got: {total_items}")

except Exception as e:
    # Handle any errors that occur during the process
    print(f"An error occurred: {str(e)}")
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Test failed due to an error.")