from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that we are on the login page
    assert driver.find_element(By.ID, "loginPage").is_displayed(), "Login page is not displayed"
    
    # Check for any errors on the page
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            print(f"Detected error: {error.text}")
            raise AssertionError(f"Unexpected error message: {error.text}")

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

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
    # Wait for the login button to be clickable and click it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click login button: " + str(e))

# Verify redirection to the cart page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    actual_page = driver.find_element(By.ID, "cartPage").is_displayed()
    assert actual_page, "User is not redirected to the cart page."
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Redirection verification failed: " + str(e))

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        if error_texts:
            raise AssertionError("Detected error messages: " + ", ".join(error_texts))
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Error checking failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password field to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys('emilyspass')
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter password: " + str(e))

try:
    # Wait for the login button to be clickable and click it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click login button: " + str(e))

# Verify if the user is redirected to the cart page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    actual_page = driver.find_element(By.ID, "cartPage").is_displayed()
    if not actual_page:
        raise AssertionError("User is not redirected to the cart page.")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify redirection to cart page: " + str(e))

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        if error_texts:
            raise AssertionError("Detected error messages: " + ", ".join(error_texts))
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to check for error messages: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for the cart page to load
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    
    # Verification step
    cart_page_visible = driver.find_element(By.ID, "cartPage").is_displayed()
    if not cart_page_visible:
        raise AssertionError("User is not redirected to the cart page.")
    
except Exception as e:
    # Handle any alert or popup
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert appeared with text: {alert_text}")
    except:
        # Take a screenshot for debugging
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError("An error occurred during the login process.")

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
    # Verify redirection to the cart page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    actual_page = driver.find_element(By.ID, "cartPage")
    assert actual_page.is_displayed(), "Cart page is not displayed"
except Exception as e:
    driver.save_screenshot('error_verify_cart_page.png')
    raise AssertionError("User is not redirected to the cart page") from e

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        for error in error_messages:
            if error.is_displayed():
                raise AssertionError(f"Detected error message: {error.text}")
except Exception as e:
    driver.save_screenshot('error_checking_errors.png')
    raise AssertionError("Error checking for error messages failed") from e