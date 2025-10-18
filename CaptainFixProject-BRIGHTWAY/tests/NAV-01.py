from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%A7%D8%AA%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Verify that we are on the login page
    assert driver.find_element(By.ID, "loginPage").is_displayed(), "Login page is not displayed"
    
    # Simulate opening the login page (if needed, otherwise this step is just for verification)
    # This step is already covered by the initial driver.get() call.
    
    # Check for any errors on the page
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            print(f"Detected error message: {error.text}")
            raise AssertionError(f"Unexpected error message: {error.text}")

    # Check for JavaScript alerts
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"Detected alert: {alert_text}")
        alert.accept()  # Accept the alert after verification
    except:
        print("No alert detected.")

    # Verify redirection to the cart page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    assert driver.find_element(By.ID, "cartPage").is_displayed(), "User is not redirected to the cart page"

except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Test failed: {str(e)}")

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
    # Submit the login form
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginForm button[type='submit']"))).click()
except Exception as e:
    driver.save_screenshot("error_login_submit.png")
    raise AssertionError("Failed to click login button: " + str(e))

# Verify redirection to the cart page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    actual_url = driver.current_url
    expected_url = "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#cartPage"
    if actual_url != expected_url:
        raise AssertionError(f"Expected to be redirected to {expected_url}, but was redirected to {actual_url}.")
except Exception as e:
    driver.save_screenshot("error_cart_page.png")
    raise AssertionError("Failed to verify redirection to cart page: " + str(e))

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

# Wait for the cart page to be visible
try:
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "cartPage")))
    # Verify that the user is redirected to the cart page
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#cartPage", "User is not redirected to the cart page."
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Verification failed: " + str(e))

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError("Error message displayed: " + error.text)
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Error checking failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for potential alert and verify
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()  # Accept the alert after verification

except Exception as e:
    # Handle any errors that occur during the click or alert handling
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

# Verify redirection to the cart page
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    actual_page = driver.find_element(By.ID, "cartPage")
    if not actual_page.is_displayed():
        raise AssertionError("User is not redirected to the cart page.")
except Exception as e:
    driver.save_screenshot('redirection_error_screenshot.png')
    raise AssertionError(f"Redirection verification failed: {str(e)}")

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
    raise AssertionError(f"Failed to click the Cart button: {str(e)}")

try:
    # Verify redirection to the cart page
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cartPage")))
    actual_page = driver.find_element(By.ID, "cartPage")
    assert actual_page.is_displayed(), "Cart page is not displayed."
except Exception as e:
    driver.save_screenshot('error_verify_cart_page.png')
    raise AssertionError(f"Failed to verify redirection to the cart page: {str(e)}")