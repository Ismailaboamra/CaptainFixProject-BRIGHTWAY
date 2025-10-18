from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that the cart is empty initially
    cart_count = driver.find_element(By.ID, "cartCount").text
    if cart_count != "0":
        raise AssertionError(f"Expected cart count to be '0', but got '{cart_count}'")
    
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
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Check for any errors after entering the username
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message:
        raise AssertionError("Error message displayed: " + error_message)
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to check for username error: " + str(e))

try:
    # Submit the login form
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to click login button: " + str(e))

try:
    # Wait for the cart to be updated and verify that products are listed
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartItems")))
    cart_items = driver.find_element(By.ID, "cartItems").text
    if "Product" not in cart_items:  # Adjust this condition based on actual product text
        raise AssertionError("Expected product not found in the cart.")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to verify cart items: " + str(e))

try:
    # Check for any alerts after the login action
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    if "success" not in alert_text.lower():  # Adjust this condition based on expected alert text
        raise AssertionError("Unexpected alert text: " + alert_text)
    alert.accept()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("No alert appeared or unexpected error: " + str(e))

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

# Verify that the product is listed in the cart
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount")))
    cart_count = driver.find_element(By.ID, "cartCount").text
    if cart_count == "0":
        raise AssertionError("Expected product to be listed in the cart, but it is not.")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to verify cart count: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for the cart to be updated and verify the expected result
    cart_count = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount")))
    actual_cart_count = cart_count.text
    
    # Verify that the product is listed in the cart
    if actual_cart_count == "1":  # Assuming 1 product should be in the cart after login
        print("Test Passed: Product is listed in the cart.")
    else:
        raise AssertionError(f"Test Failed: Expected cart count to be '1', but got '{actual_cart_count}'.")

except Exception as e:
    # Handle any alerts or errors
    try:
        alert = WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert detected: {alert_text}")
    except:
        # Check for inline errors or notifications
        error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
        for error in error_messages:
            if error.is_displayed():
                raise AssertionError(f"Inline error detected: {error.text}")
        
        # If no alerts or inline errors, take a screenshot for debugging
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError("An unexpected error occurred.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the main shop page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the product list to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    
    # Assuming there is a product to add, we will simulate adding the first product
    # This part of the code would depend on the actual product structure in the HTML
    # For demonstration, let's assume we have a button to add the first product
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, ".products-grid .btn-add-to-cart")  # Adjust selector as needed
    add_to_cart_button.click()
    
    # Wait for the cart to update
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartCount")))
    
    # Verify the cart count has increased
    cart_count = driver.find_element(By.ID, "cartCount").text
    if cart_count == "1":  # Assuming we expect one product in the cart
        print("Product added to cart successfully.")
    else:
        raise AssertionError("Expected cart count to be 1, but got: " + cart_count)

except Exception as e:
    # Handle any errors that occur during the process
    print("An error occurred:", str(e))
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Test failed due to an error.")

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
    # Verify that the product is listed in the cart
    cart_items = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartItems")))
    if cart_items.text == "":
        raise AssertionError("Expected product to be listed in the cart, but it is empty.")
except Exception as e:
    driver.save_screenshot('error_verify_cart_items.png')
    raise AssertionError("Failed to verify cart items") from e

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
    # Wait for the cart items to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartItems")))
    cart_items = driver.find_element(By.ID, "cartItems").text

    # Verify the expected result
    if "Product" not in cart_items:  # Replace "Product" with the actual product name if known
        raise AssertionError("Expected product is not listed in the cart.")
except Exception as e:
    # Handle any errors and take a screenshot for debugging
    driver.save_screenshot('error_screenshot.png')
    raise e

# Check for any alerts or error messages
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    # Verify alert text if necessary
    alert.accept()
except:
    pass  # No alert present

# Check for inline errors or notifications
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Error message displayed: {error.text}")
except Exception as e:
    # Log the error for debugging
    print(f"Error checking inline messages: {str(e)}")