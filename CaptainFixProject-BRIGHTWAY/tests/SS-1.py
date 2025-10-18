from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that the login page is displayed
    assert driver.find_element(By.ID, "loginPage").is_displayed(), "Login page is not displayed"
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred while opening the login page: {str(e)}")

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError(f"Error message displayed: {error.text}")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred while checking for errors: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username field to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys('emilys')
except Exception as e:
    driver.save_screenshot('error_username_input.png')
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Verify if the username was entered correctly
    actual_username = driver.find_element(By.ID, "username").get_attribute("value")
    expected_username = 'emilys'
    assert actual_username == expected_username, f"Expected username '{expected_username}', but got '{actual_username}'"
except Exception as e:
    driver.save_screenshot('error_username_verification.png')
    raise AssertionError("Verification of username input failed: " + str(e))

# Check for any errors on the page after entering the username
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            error_text = error.text
            raise AssertionError(f"Detected error message: {error_text}")
except Exception as e:
    driver.save_screenshot('error_detection.png')
    raise AssertionError("Error detection failed: " + str(e))

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
    raise AssertionError(f"Failed to enter password: {str(e)}")

try:
    # Wait for the login button to be clickable and click it
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    login_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to click login button: {str(e)}")

# Check for any alerts after clicking the login button
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Expected alert message"  # Replace with the actual expected alert message
    if alert_text != expected_alert_text:
        driver.save_screenshot('error_screenshot.png')
        raise AssertionError(f"Unexpected alert text: {alert_text}")
    alert.accept()
except Exception as e:
    pass  # No alert present, continue

# Verify that products are displayed after login
try:
    products_displayed = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    if not products_displayed.is_displayed():
        raise AssertionError("Products are not displayed after login.")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to verify products display: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for the products to be displayed
    products_displayed = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    
    # Verification step
    if products_displayed.is_displayed():
        print("Products are displayed successfully.")
    else:
        raise AssertionError("Products are not displayed.")
    
except Exception as e:
    # Handle any alerts or errors
    try:
        alert = WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert appeared: {alert_text}")
    except:
        # Check for inline errors or notifications
        error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
        for error in error_messages:
            if error.is_displayed():
                raise AssertionError(f"Error message displayed: {error.text}")
    
    # If no alert or error, take a screenshot for debugging
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("An unexpected error occurred.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the category filter to be present and select a category
    category_filter = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "categoryFilter")))
    category_filter.click()
    category_filter.find_element(By.XPATH, "//option[not(@value='')]").click()  # Select the first non-empty option

    # Verify that products from the selected category are displayed
    products_list = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    if products_list.is_displayed() and len(products_list.find_elements(By.XPATH, ".//*")) > 0:
        print("Products from the selected category are displayed.")
    else:
        raise AssertionError("No products are displayed for the selected category.")

except Exception as e:
    # Handle any errors that occur during the interaction
    print(f"An error occurred: {str(e)}")
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Test failed due to an error.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the search button to be present and click it
    search_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchBtn")))
    search_button.click()
    
    # Wait for the products to be displayed
    products_displayed = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    
    # Verification step
    if products_displayed.is_displayed():
        print("Products from the selected category are displayed.")
    else:
        raise AssertionError("Expected products are not displayed.")
    
except Exception as e:
    # Handle any alert or popup
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert displayed: {alert_text}")
    except:
        # Take a screenshot for debugging
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError("An error occurred: " + str(e))