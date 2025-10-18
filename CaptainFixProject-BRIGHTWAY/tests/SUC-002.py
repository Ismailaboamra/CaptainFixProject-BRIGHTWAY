from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginPage")))
    
    # Verification: Check if the login page is displayed
    assert driver.find_element(By.ID, "loginPage").is_displayed(), "Login page is not displayed."
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred while opening the login page: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the login page and enter the username
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    username_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_input.send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Failed to enter username: {str(e)}")

# Step 2: Verify if the user is redirected to the checkout page
try:
    WebDriverWait(driver, 20).until(
        EC.url_contains("checkout")  # Assuming the checkout page URL contains "checkout"
    )
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("User was not redirected to the checkout page.")

# Step 3: Check for any errors on the page
try:
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "error-message"))
    )
    if error_message.is_displayed():
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError("There is an error message displayed on the page.")
except Exception as e:
    pass  # No error message found, proceed

# Additional checks for alerts or popups can be added here if necessary.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the login page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter password
try:
    password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.send_keys("emilyspass")
    
    # Verification: Check if the password field contains the expected value
    assert password_input.get_attribute('value') == "emilyspass", "Password was not entered correctly."
    
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to enter password: {str(e)}")

# Step 3: Click the login button
try:
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    login_button.click()
    
    # Verification: Check if the user is redirected to the checkout page
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart-summary"))
    )
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#checkout", "User was not redirected to the checkout page."
    
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to click login button or redirect: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Click the Login button
try:
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    login_button.click()
    
    # Verification: Check if user is redirected to the checkout page
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "cartPage"))
    )
    assert "cartPage" in driver.current_url, "User was not redirected to the checkout page."
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Click the Cart button
try:
    cart_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "cartBtn"))
    )
    cart_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to click the Cart button: {str(e)}")

# Verification: Check if user is redirected to the checkout page
try:
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "cartPage"))
    )
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#cartPage", "User is not redirected to the checkout page."
except AssertionError as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Verification failed: {str(e)}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Error during verification: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Click the Proceed to Checkout button
try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.btn-checkout"))).click()
    # Verification: Check if user is redirected to the checkout page
    WebDriverWait(driver, 20).until(EC.url_contains("checkout"))  # Assuming the checkout page URL contains "checkout"
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to click the Proceed to Checkout button or redirect to checkout page.") from e

# Error detection logic (if needed)
# This part can be expanded based on the specific error messages expected on the page.