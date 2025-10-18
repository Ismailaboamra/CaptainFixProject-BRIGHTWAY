from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that the total price reflects the sum of all products added
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    actual_total_price = total_price_element.text
    
    # Assuming the expected total price is calculated or known
    expected_total_price = "$0.00"  # This should be replaced with the actual expected value based on the test context
    
    if actual_total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {actual_total_price}")

except Exception as e:
    # Handle any alerts or errors on the page
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
    
    # If any other exception occurs, log it
    print(f"An error occurred: {str(e)}")

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
    # Wait for the shop page to load and check the total price
    total_price = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice"))).text
    if total_price != "$0.00":  # Assuming no products are added initially
        raise AssertionError(f"Expected total price to be '$0.00', but got '{total_price}'")
except Exception as e:
    driver.save_screenshot("error_check_total_price.png")
    raise AssertionError("Failed to verify total price: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter password: " + str(e))

try:
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click login button: " + str(e))

# Check for any alerts after login
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
except Exception as e:
    alert_text = None

# Verify if the total price reflects the sum of all products added
try:
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    total_price = total_price_element.text
    # Assuming we expect a specific total price, for example "$100.00"
    expected_total_price = "$100.00"  # Replace with the actual expected value
    if total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {total_price}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify total price: " + str(e))

# Check for any inline errors or notifications
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Detected error message: {error.text}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Error checking for inline errors: " + str(e))

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
    expected_alert_text = "Expected alert message"  # Replace with the actual expected alert message
    if alert_text != expected_alert_text:
        driver.save_screenshot("alert_error.png")
        raise AssertionError(f"Alert text '{alert_text}' does not match expected '{expected_alert_text}'")
    alert.accept()

except Exception as e:
    driver.save_screenshot("error.png")
    raise AssertionError(f"An error occurred: {str(e)}")

# Verify the total price reflects the sum of all products added
try:
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    actual_total_price = total_price_element.text
    expected_total_price = "$0.00"  # Replace with the actual expected total price after login
    if actual_total_price != expected_total_price:
        raise AssertionError(f"Total price '{actual_total_price}' does not match expected '{expected_total_price}'")
except Exception as e:
    driver.save_screenshot("total_price_error.png")
    raise AssertionError(f"An error occurred while verifying total price: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%A7%D8%AA%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Add first product to the cart
    product1_add_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#productsList .product1 .add-to-cart")))
    product1_add_button.click()
    
    # Add second product to the cart
    product2_add_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#productsList .product2 .add-to-cart")))
    product2_add_button.click()
    
    # Add third product to the cart
    product3_add_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#productsList .product3 .add-to-cart")))
    product3_add_button.click()

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Error adding products to cart: {str(e)}")

# Verify total price reflects the sum of all products added
try:
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    total_price = total_price_element.text
    
    # Assuming the prices of the products are known
    expected_total_price = "$30.00"  # Replace with the actual expected total price based on added products
    if total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {total_price}")

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Error verifying total price: {str(e)}")

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CSS_SELECTOR, ".error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Detected error message: {error.text}")

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Error checking for error messages: {str(e)}")

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

    # Verify the total price calculation
    # Assuming we have a function to calculate the expected total price
    expected_total_price = "$0.00"  # Replace with actual expected value based on products added

    if total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {total_price}")

except Exception as e:
    # Handle any errors that may occur
    print(f"An error occurred: {str(e)}")
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Test failed due to an unexpected error.")