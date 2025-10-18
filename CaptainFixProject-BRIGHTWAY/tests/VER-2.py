from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify the total price reflects the sum of products in the cart
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    actual_total_price = total_price_element.text
    
    # Assuming the expected total price is $0.00 for the initial state
    expected_total_price = "$0.00"
    
    if actual_total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {actual_total_price}")

except Exception as e:
    # Handle any alerts or errors
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
    
    # If no alerts or errors, take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")
    raise e

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
    # Check for any errors after entering the username
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message:
        raise AssertionError(f"Error message displayed: {error_message}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to check for username error: " + str(e))

try:
    # Verify the total price reflects the sum of products in the cart
    total_price = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice"))).text
    if total_price != "$0.00":  # Assuming the expected total price is not zero
        raise AssertionError(f"Expected total price to be '$0.00', but got '{total_price}'")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify total price: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password field to be present and enter the password
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys('emilyspass')
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to enter password: {str(e)}")

try:
    # After entering the password, check for any errors on the page
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError")))
    if error_message.is_displayed():
        error_text = error_message.text
        raise AssertionError(f"Error message displayed: {error_text}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to check for error messages: {str(e)}")

try:
    # Verify the total price reflects the sum of products in the cart
    total_price = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    actual_total_price = total_price.text
    expected_total_price = "$0.00"  # Assuming no products are in the cart initially
    if actual_total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {actual_total_price}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to verify total price: {str(e)}")

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

# Verify the total price reflects the sum of products in the cart
try:
    total_price = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    actual_total_price = total_price.text
    expected_total_price = "$0.00"  # Assuming no products are in the cart initially

    if actual_total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {actual_total_price}")
except Exception as e:
    driver.save_screenshot('error_verify_total_price.png')
    raise AssertionError("Failed to verify the total price") from e

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Detected error message: {error.text}")
except Exception as e:
    driver.save_screenshot('error_checking_for_errors.png')
    raise AssertionError("Failed to check for errors on the page") from e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Cart button
    cart_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "cartBtn")))
    cart_button.click()
except Exception as e:
    driver.save_screenshot('error_click_cart_button.png')
    raise AssertionError("Failed to click the Cart button") from e

try:
    # Verify the total price reflects the sum of products in the cart
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    actual_total_price = total_price_element.text
    # Assuming we have a way to calculate the expected total price
    expected_total_price = "$0.00"  # Replace with actual expected value based on cart contents

    if actual_total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {actual_total_price}")
except Exception as e:
    driver.save_screenshot('error_verify_total_price.png')
    raise AssertionError("Failed to verify the total price") from e

# Detect and verify any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
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
    # Wait for the total price element to be present
    total_price_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "totalPrice"))
    )
    total_price = total_price_element.text

    # Verify the total price reflects the sum of products in the cart
    # Assuming we have a function to calculate the expected total price
    expected_total_price = "$0.00"  # Replace with actual calculation logic if needed

    if total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {total_price}")

except Exception as e:
    # Handle any errors that may occur
    print(f"An error occurred: {str(e)}")
    # Check for alerts or error messages
    try:
        alert = WebDriverWait(driver, 20).until(EC.alert_is_present())
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