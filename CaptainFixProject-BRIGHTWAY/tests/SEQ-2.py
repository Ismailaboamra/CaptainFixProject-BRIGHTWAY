from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that the user is on the login page
    assert driver.find_element(By.ID, "loginPage").is_displayed(), "Login page is not displayed"
    
    # Simulate opening the login page (if needed, otherwise this step is just for verification)
    # This step is not necessary as we are already on the login page after the driver.get() call.
    
    # Check if the user is redirected back to the shop page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    
    # Verify that the shop page is displayed
    assert driver.find_element(By.ID, "shopPage").is_displayed(), "User is not redirected to the shop page"

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
            raise AssertionError(f"Error message found: {error.text}")
    
    # Take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

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
    # Wait for the login button to be clickable and click it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot("error_login_button.png")
    raise AssertionError("Failed to click login button: " + str(e))

# Check for any alerts after clicking the login button
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()  # Accept the alert after verification
except Exception as e:
    alert_text = None  # No alert present

# Verify if the user is redirected to the shop page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    actual_result = driver.find_element(By.ID, "shopPage").is_displayed()
    if not actual_result:
        raise AssertionError("User is not redirected to the shop page.")
except Exception as e:
    driver.save_screenshot("error_redirect.png")
    raise AssertionError("Failed to verify redirection to shop page: " + str(e))

# Check for any errors on the page
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
    driver.save_screenshot("error_messages.png")
    raise AssertionError("Detected errors on the page: " + ", ".join(error_messages))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page (if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
    
    # Click the login button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
    
    # Wait for the shop page to be visible
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "shopPage")))
    
    # Verification step: Check if the user is redirected to the shop page
    if not driver.find_element(By.ID, "shopPage").is_displayed():
        raise AssertionError("User is not redirected to the shop page.")
    
except Exception as e:
    # Handle any alerts or popups
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert appeared: {alert_text}")
    except:
        # Take a screenshot for debugging
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError("An error occurred during the login process.") from e

# Detect and verify any errors on the page
error_messages = []
try:
    username_error = driver.find_element(By.ID, "usernameError").text
    if username_error:
        error_messages.append(username_error)
    
    password_error = driver.find_element(By.ID, "passwordError").text
    if password_error:
        error_messages.append(password_error)

    if error_messages:
        raise AssertionError(f"Detected errors: {', '.join(error_messages)}")
except:
    pass  # No errors found, continue with the test

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
    
    # Wait for the shop page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    
    # Verification step
    shop_page = driver.find_element(By.ID, "shopPage")
    if not shop_page.is_displayed():
        raise AssertionError("User is not redirected to the shop page.")
    
except Exception as e:
    # Handle any alerts or errors
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert appeared: {alert_text}")
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
    # Click the Back to Shop button
    back_to_shop_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "backToShopBtn")))
    back_to_shop_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to click the Back to Shop button: {str(e)}")

try:
    # Verify that the user is redirected back to the shop page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    actual_page_state = driver.find_element(By.ID, "shopPage").is_displayed()
    if not actual_page_state:
        raise AssertionError("User is not redirected back to the shop page.")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Verification failed: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the product to be clickable and click on it (assuming a product is present)
    product = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".products-grid .product-item")))
    product.click()
    
    # Wait for the product details page to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productDetails")))
    
    # Click the back to shop button
    back_to_shop_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "backToShopBtn")))
    back_to_shop_button.click()
    
    # Verify that the user is redirected back to the shop page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    assert driver.find_element(By.ID, "shopPage").is_displayed(), "User is not redirected back to the shop page."

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
    
    # Take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("An error occurred during the test execution.") from e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Back to Shop button
    back_to_shop_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "backToShopBtn")))
    back_to_shop_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to click the Back to Shop button: {str(e)}")

try:
    # Verify that the user is redirected back to the shop page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "shopPage")))
    actual_page = driver.find_element(By.ID, "shopPage")
    if not actual_page.is_displayed():
        raise AssertionError("User is not redirected back to the shop page.")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Verification failed: {str(e)}")

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        if error_texts:
            raise AssertionError(f"Detected errors on the page: {error_texts}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Error checking failed: {str(e)}")