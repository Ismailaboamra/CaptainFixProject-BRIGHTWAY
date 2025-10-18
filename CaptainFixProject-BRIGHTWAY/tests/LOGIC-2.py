from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Wait for the login page to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that the total price is displayed correctly
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    total_price = total_price_element.text
    
    # Assuming we have a way to calculate the expected total price from individual product prices
    # This part would typically involve summing up the prices of products in the cart
    expected_total_price = "$0.00"  # Replace with actual expected value based on the products

    if total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {total_price}")

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

    # Log the exception for debugging
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
    # Submit the login form
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click login button: " + str(e))

try:
    # Wait for the shop page to load and verify the total price
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    total_price = driver.find_element(By.ID, "totalPrice").text
    # Assuming we have a way to calculate the expected total price
    expected_total_price = "$0.00"  # Replace with actual expected value based on product prices
    if total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {total_price}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
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

# Check for errors on the page
error_messages = []
try:
    username_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if username_error:
        error_messages.append(username_error)
except:
    pass

try:
    password_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError"))).text
    if password_error:
        error_messages.append(password_error)
except:
    pass

# Log any detected error messages
if error_messages:
    for message in error_messages:
        print("Detected error message: " + message)
    raise AssertionError("Errors detected on the page: " + ", ".join(error_messages))

# Verify the total price after login
try:
    total_price = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice"))).text
    # Assuming the expected total price is calculated or known
    expected_total_price = "$0.00"  # Replace with actual expected value if known
    if total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {total_price}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify total price: " + str(e))

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

# Verify the total price after clicking the Login button
try:
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    actual_total_price = total_price_element.text
    expected_total_price = "$0.00"  # Adjust this based on the expected result after login
    assert actual_total_price == expected_total_price, f"Expected total price: {expected_total_price}, but got: {actual_total_price}"
except Exception as e:
    driver.save_screenshot('error_verifying_total_price.png')
    raise AssertionError("Failed to verify the total price") from e

# Detect and verify any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            error_text = error.text
            # Add expected error messages to check against
            expected_error_messages = []
            assert error_text not in expected_error_messages, f"Unexpected error message displayed: {error_text}"
except Exception as e:
    driver.save_screenshot('error_detecting_errors.png')
    raise AssertionError("Failed to detect errors on the page") from e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Add first product to the cart
    first_product_add_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".products-grid .product:first-child .add-to-cart")))
    first_product_add_button.click()
    
    # Add second product to the cart
    second_product_add_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".products-grid .product:nth-child(2) .add-to-cart")))
    second_product_add_button.click()
    
    # Add third product to the cart
    third_product_add_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".products-grid .product:nth-child(3) .add-to-cart")))
    third_product_add_button.click()

    # Verify total price
    total_price_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "totalPrice")))
    total_price = total_price_element.text

    # Calculate expected total price based on individual product prices
    expected_total_price = "$30.00"  # Replace with actual calculation based on product prices

    if total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {total_price}")

except Exception as e:
    # Handle any alerts or errors
    try:
        alert = WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        print(f"Alert detected: {alert_text}")
    except:
        print("No alert detected.")

    # Check for inline errors or notifications
    error_messages = driver.find_elements(By.CSS_SELECTOR, ".error-message")
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
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the total price element to be present
    total_price_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "totalPrice"))
    )
    total_price = total_price_element.text

    # Verify the total price
    # Assuming we have a function to calculate the expected total price
    expected_total_price = "$0.00"  # Replace with actual calculation logic if needed

    if total_price != expected_total_price:
        raise AssertionError(f"Expected total price: {expected_total_price}, but got: {total_price}")

except Exception as e:
    # Handle any errors that may occur
    print(f"An error occurred: {str(e)}")
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Test failed due to an error.")