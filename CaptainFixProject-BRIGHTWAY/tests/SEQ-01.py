from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Verify that the login page is displayed
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    assert driver.find_element(By.ID, "loginPage").is_displayed(), "Login page is not displayed"

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
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot("error_login_button.png")
    raise AssertionError("Failed to click login button: " + str(e))

# Check for any alerts after clicking the login button
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Expected alert message"  # Replace with the actual expected alert message if any
    if alert_text != expected_alert_text:
        driver.save_screenshot("error_alert.png")
        raise AssertionError(f"Unexpected alert text: {alert_text}")
    alert.accept()
except Exception as e:
    # No alert was present, continue
    pass

# Verify that the user is taken through the checkout process successfully
try:
    # Wait for an element that indicates the user is on the checkout process page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    actual_result = driver.find_element(By.ID, "cartPage").is_displayed()
    if not actual_result:
        raise AssertionError("User is not taken through the checkout process successfully.")
except Exception as e:
    driver.save_screenshot("error_checkout_process.png")
    raise AssertionError("Failed to verify checkout process: " + str(e))

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
    expected_alert_text = "Expected alert text"  # Replace with the actual expected alert text if any
    if alert_text != expected_alert_text:
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError(f"Unexpected alert text: {alert_text}")
    alert.accept()
except Exception as e:
    pass  # No alert present, continue

# Verify if the user is taken to the checkout process successfully
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    actual_result = driver.find_element(By.ID, "cartPage").is_displayed()
    if not actual_result:
        raise AssertionError("User is not taken to the checkout process successfully.")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to verify checkout process: " + str(e))

# Detect and verify any errors on the page
error_messages = []
try:
    username_error = driver.find_element(By.ID, "usernameError").text
    if username_error:
        error_messages.append(username_error)
except Exception:
    pass

try:
    password_error = driver.find_element(By.ID, "passwordError").text
    if password_error:
        error_messages.append(password_error)
except Exception:
    pass

if error_messages:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Detected errors on the page: {', '.join(error_messages)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for any potential alerts and verify
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "User is taken through the checkout process successfully."
    
    if alert_text == expected_alert_text:
        alert.accept()
    else:
        driver.save_screenshot("alert_error.png")
        raise AssertionError(f"Unexpected alert text: {alert_text}")

except Exception as e:
    # Check for inline errors or notifications
    error_messages = driver.find_elements(By.CSS_SELECTOR, ".error-message")
    for error in error_messages:
        if error.is_displayed():
            print(f"Detected error: {error.text}")
            raise AssertionError(f"Detected error: {error.text}")

    # If no alerts or errors, check if the user is taken to the checkout process
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
        print("User successfully taken through the checkout process.")
    except:
        raise AssertionError("User was not taken through the checkout process successfully.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Log in to the application (assuming valid credentials are used)
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("valid_username")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("valid_password")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('login_error.png')
    raise AssertionError("Login failed: " + str(e))

# Check for any errors after login
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message:
        driver.save_screenshot('login_error.png')
        raise AssertionError("Login error: " + error_message)
except Exception:
    pass  # No error message found

# Add a product to the cart (assuming the product is available on the shop page)
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    # Assuming there is a product to add, we will simulate clicking on a product and adding it to the cart
    # This part of the code would depend on the actual product elements available on the page
    # For demonstration, we will assume there is a button with class 'btn-add-to-cart' for adding products
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-add-to-cart"))).click()
except Exception as e:
    driver.save_screenshot('add_to_cart_error.png')
    raise AssertionError("Failed to add product to cart: " + str(e))

# Verify that the user is taken through the checkout process
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-checkout"))).click()
    # Assuming the checkout page has a specific element to verify successful navigation
    checkout_header = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Checkout']")))
    if checkout_header.text != "Checkout":
        raise AssertionError("User was not taken to the checkout process successfully.")
except Exception as e:
    driver.save_screenshot('checkout_error.png')
    raise AssertionError("Checkout process failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the Cart button to be present and click it
    cart_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartBtn")))
    cart_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to click the Cart button: {str(e)}")

# Verify if the user is taken to the checkout process
try:
    # Wait for the cart page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    # Check if the cart page is displayed
    cart_page_visible = driver.find_element(By.ID, "cartPage").is_displayed()
    if not cart_page_visible:
        raise AssertionError("Cart page is not displayed after clicking the Cart button.")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Verification failed: {str(e)}")

# Detect any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Detected error message: {error.text}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Error detection failed: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the Proceed to Checkout button to be clickable and click it
    proceed_to_checkout_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.btn-checkout"))
    )
    proceed_to_checkout_button.click()
    
    # Verification step: Check if the user is taken to the checkout process
    # This can be done by checking the presence of an element that is only on the checkout page
    # Assuming there is an element with id 'checkoutPage' on the checkout page
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "checkoutPage"))
    )
    
except Exception as e:
    # Handle any alerts or popups
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        # Log the alert text for debugging
        print(f"Alert detected: {alert_text}")
    except:
        # If no alert is present, take a screenshot for debugging
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError("An error occurred during the checkout process.")

# Detect and verify any errors on the page
error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
for error in error_messages:
    if error.is_displayed():
        error_text = error.text
        # Log the error message for debugging
        print(f"Error detected: {error_text}")
        raise AssertionError(f"Unexpected error message: {error_text}")