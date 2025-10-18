from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Verify that the login page is displayed
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginPage")))
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html", "User is not on the login page"
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to open the login page: " + str(e))

# Step 2: Simulate the action of logging in (if needed for further steps)
# This step is not required for the current task but can be added if necessary.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the login page and enter the username
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter username: " + str(e))

# Step 2: Verify if the user is redirected to the cart page
try:
    WebDriverWait(driver, 20).until(EC.url_contains("cartPage"))
    current_url = driver.current_url
    assert "cartPage" in current_url, f"Expected to be redirected to cart page, but current URL is: {current_url}"
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Redirection to cart page failed: " + str(e))

# Step 3: Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        assert not error_texts, f"Found error messages on the page: {error_texts}"
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Error detection failed: " + str(e))

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
    
    # Verification: Check if the password input is filled correctly
    assert password_input.get_attribute('value') == "emilyspass", "Password input verification failed."
    
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to enter password: {str(e)}")

# Step 3: Submit the login form
try:
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    login_button.click()
    
    # Verification: Check if user is redirected to the cart page
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "cartPage"))
    )
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#cartPage", "Redirection to cart page failed."
    
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to submit login form or redirect: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Click the Login button
try:
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    login_button.click()
    
    # Verification: Check if redirected to the cart page
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "cartPage"))
    )
    assert "cartPage" in driver.current_url, "User is not redirected to the cart page."
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
    
    # Verification: Check if redirected to the cart page
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "cartPage"))
    )
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#cartPage", "User is not redirected to the cart page."
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Failed to click the Cart button or verify redirection: {str(e)}")