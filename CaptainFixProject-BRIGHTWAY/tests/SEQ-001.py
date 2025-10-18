from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Verification: Check if the login page is displayed
try:
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginPage")))
    assert driver.find_element(By.ID, "loginPage").is_displayed(), "Login page is not displayed."
except Exception as e:
    driver.save_screenshot("error_login_page.png")
    raise AssertionError("Failed to verify login page visibility: " + str(e))

# Step 2: Simulate login (if needed) and check redirection to checkout page
# Assuming the user logs in successfully, we would check for redirection to the checkout page
try:
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "shopPage")))
    assert driver.find_element(By.ID, "shopPage").is_displayed(), "User is not redirected to the shop page."
except Exception as e:
    driver.save_screenshot("error_checkout_page.png")
    raise AssertionError("Failed to verify redirection to shop page: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the login page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter username
try:
    username_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_input.send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter username: " + str(e))

# Step 3: Verify redirection to the checkout page
try:
    WebDriverWait(driver, 20).until(
        EC.url_contains("checkout")  # Assuming the checkout page URL contains "checkout"
    )
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("User was not redirected to the checkout page: " + str(e))

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
    
    # Verification: Check if the user is redirected to the checkout page
    WebDriverWait(driver, 20).until(
        EC.url_contains("checkout")  # Assuming the URL contains 'checkout' after redirection
    )
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter password or redirect to checkout page: " + str(e))

# Step 3: Check for errors on the page
try:
    error_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "error-message"))
    )
    if error_message.is_displayed():
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError("An error message is displayed: " + error_message.text)
except Exception as e:
    pass  # No error message found, proceed

# Additional checks for alerts or popups can be added here if necessary.

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
    
    # Verification: Check if redirected to the checkout page
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "cartPage"))
    )
    assert "cartPage" in driver.current_url, "User is not redirected to the checkout page."
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the website (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Add a product to the cart
try:
    # Assuming there is a product to add, we need to find the button to add it to the cart
    add_to_cart_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.btn-checkout"))
    )
    add_to_cart_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click the add to cart button: " + str(e))

# Step 3: Verify redirection to the checkout page
try:
    WebDriverWait(driver, 20).until(
        EC.url_contains("checkout")  # Assuming the checkout page URL contains 'checkout'
    )
    current_url = driver.current_url
    assert "checkout" in current_url, f"Expected to be redirected to checkout page, but was on {current_url}"
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Redirection to checkout page failed: " + str(e))

# Step 4: Check for errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        assert not error_texts, f"Found error messages on the page: {error_texts}"
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Error detection failed: " + str(e))

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
    driver.save_screenshot('error_click_cart_button.png')
    raise AssertionError("Failed to click the Cart button: " + str(e))

# Verification: Check if redirected to the checkout page
try:
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "cartPage"))
    )
    assert "Your Cart" in driver.page_source, "User is not redirected to the checkout page."
except AssertionError as e:
    driver.save_screenshot('error_redirect_checkout.png')
    raise AssertionError("Verification failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Click the Proceed to Checkout button
try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.btn-checkout"))).click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click the Proceed to Checkout button: " + str(e))

# Verification: Check if user is redirected to the checkout page
try:
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "checkoutPage")))  # Assuming checkoutPage is the ID of the checkout page
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("User was not redirected to the checkout page: " + str(e))

# Error Detection: Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        raise AssertionError("Inline errors detected: " + ", ".join(error_texts))
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Error detection failed: " + str(e))