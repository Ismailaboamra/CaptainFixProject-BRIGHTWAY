from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Check for any errors on the page
    error_messages = driver.find_elements(By.CSS_SELECTOR, ".error-message")
    for error in error_messages:
        if error.is_displayed():
            print(f"Detected error: {error.text}")
            raise AssertionError(f"Error detected: {error.text}")

    # Verify that we are on the login page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm")))
    
    # Verify the total price in the cart
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    total_price = total_price_element.text
    
    # Assuming we have a function to calculate expected total price
    expected_total_price = "$0.00"  # This should be replaced with the actual expected value based on the products in the cart
    
    if total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {total_price}")

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot('error_username_input.png')
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('error_login_button.png')
    raise AssertionError("Failed to click login button: " + str(e))

# Check for any alerts after login attempt
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
except Exception as e:
    alert_text = None

# Verify if the total price is correct after logging in
try:
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    total_price = total_price_element.text
    # Assuming we have a function to calculate expected total price
    expected_total_price = "$0.00"  # Replace with actual expected value based on cart items
    if total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {total_price}")
except Exception as e:
    driver.save_screenshot('error_total_price_verification.png')
    raise AssertionError("Failed to verify total price: " + str(e))

# Detect and verify any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Detected error message: {error.text}")
except Exception as e:
    driver.save_screenshot('error_detection.png')
    raise AssertionError("Failed to detect errors on the page: " + str(e))

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
except Exception as e:
    pass  # No alert present

# Verify the total price after logging in
try:
    # Wait for the total price element to be present
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    actual_total_price = total_price_element.text
    # Here you would compare actual_total_price with the expected total price
    # For demonstration, let's assume the expected total price is "$100.00"
    expected_total_price = "$100.00"  # Replace with actual expected value
    if actual_total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {actual_total_price}")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to verify total price: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to click the Login button: {str(e)}")

# Verify the total price after login
try:
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    actual_total_price = total_price_element.text
    expected_total_price = "$0.00"  # Assuming no products are added yet; adjust as necessary

    if actual_total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {actual_total_price}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to verify total price: {str(e)}")

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CSS_SELECTOR, ".error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Detected error message: {error.text}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to check for error messages: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Add first product to the cart (assuming there's a way to add products, e.g., a button)
    first_product_add_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".products-grid .add-to-cart-button:first-child")))
    first_product_add_button.click()
    
    # Add second product to the cart
    second_product_add_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".products-grid .add-to-cart-button:nth-child(2)")))
    second_product_add_button.click()

    # Wait for the cart to update
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount")))
    
    # Verify total price in the cart
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    actual_total_price = total_price_element.text
    
    # Assuming we have a function to calculate expected total price based on added products
    expected_total_price = "$20.00"  # Replace with actual calculation logic
    
    if actual_total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {actual_total_price}")

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
        error_messages = driver.find_elements(By.CSS_SELECTOR, ".error-message")
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
    # Wait for the total price element to be present
    total_price_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "totalPrice"))
    )
    total_price = total_price_element.text

    # Verify the total price
    # Assuming we have a function to calculate the expected total price
    expected_total_price = "$0.00"  # Replace with actual calculation logic if available
    if total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {total_price}")

except Exception as e:
    # Handle any errors that occur during the process
    print(f"An error occurred: {str(e)}")
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Test failed due to an error.")