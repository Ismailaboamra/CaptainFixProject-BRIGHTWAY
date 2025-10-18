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
    expected_total_items = "0"  # Assuming no items are added yet
    assert total_items == expected_total_items, f"Expected total items to be {expected_total_items}, but got {total_items}"

except Exception as e:
    # Handle any errors or alerts
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
    
    # If any other exception occurs, log it
    print(f"An error occurred: {str(e)}")

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
    # Check for any errors on the page after entering the username
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message:
        raise AssertionError("Error message displayed: " + error_message)
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to check for errors: " + str(e))

try:
    # Verify the total items in the cart
    total_items = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalItems"))).text
    if total_items != '0':
        raise AssertionError(f"Expected total items to be '0', but got '{total_items}'")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify total items in the cart: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password field to be present and enter the password
    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys('emilyspass')
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter password: " + str(e))

try:
    # Wait for the login button to be clickable and click it
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click login button: " + str(e))

# Check for any alerts after clicking the login button
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
except Exception as e:
    alert_text = None

# Verify the total items in the cart after login
try:
    total_items = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalItems")))
    actual_total_items = total_items.text
    expected_total_items = "1"  # Assuming one product is added to the cart after login

    if actual_total_items != expected_total_items:
        raise AssertionError(f"Expected total items: {expected_total_items}, but got: {actual_total_items}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify total items in the cart: " + str(e))

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

# Verify the total items in the cart
try:
    total_items = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalItems")))
    actual_total_items = total_items.text
    expected_total_items = "1"  # Assuming 1 item is added for verification

    if actual_total_items != expected_total_items:
        raise AssertionError(f"Expected total items: {expected_total_items}, but got: {actual_total_items}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to verify total items in the cart: {str(e)}")

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
    # Assuming there is a product to add, we will simulate adding a product to the cart
    # This step would typically involve clicking a button or link to add a product
    # For demonstration, let's assume we have a button with id 'addProductBtn' to add a product
    add_product_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "addProductBtn")))
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
        # Log alert text if needed
    except:
        pass
    
    # Check for inline errors or notifications
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            print(f"Error message found: {error.text}")
            raise AssertionError(f"Error message: {error.text}")

    # If any other exception occurs, log it
    print(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%A7%D9%87%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the total items element to be present
    total_items_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "totalItems"))
    )
    # Get the actual total items in the cart
    actual_total_items = total_items_element.text

    # Expected result (this should be set based on the test context)
    expected_total_items = "1"  # Example expected value, adjust as necessary

    # Verification step
    if actual_total_items != expected_total_items:
        raise AssertionError(f"Expected total items: {expected_total_items}, but got: {actual_total_items}")

except Exception as e:
    # Handle any errors that may occur
    print(f"An error occurred: {str(e)}")
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Test failed due to an unexpected error.")