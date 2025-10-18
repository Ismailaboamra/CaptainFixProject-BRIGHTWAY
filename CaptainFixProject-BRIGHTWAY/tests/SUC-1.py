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
    # Wait for the username input to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_username_input.png")
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Submit the login form
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot("error_login_button.png")
    raise AssertionError("Failed to click login button: " + str(e))

# Check for any alerts after login attempt
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    # You can add verification for alert text if needed
except Exception as e:
    pass  # No alert present, continue

# Verify that products are displayed
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    products_displayed = driver.find_element(By.ID, "productsList").is_displayed()
    if not products_displayed:
        raise AssertionError("Products are not displayed after login.")
except Exception as e:
    driver.save_screenshot("error_products_display.png")
    raise AssertionError("Failed to verify products display: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter password: " + str(e))

try:
    # Wait for the login button to be clickable and click it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click login button: " + str(e))

# Verify if products are displayed after login
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    products_displayed = driver.find_element(By.ID, "productsList").is_displayed()
    if not products_displayed:
        raise AssertionError("Expected products are not displayed.")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Verification of products display failed: " + str(e))

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

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
except Exception as e:
    driver.save_screenshot('error_click_login_button.png')
    raise AssertionError("Failed to click the Login button") from e

# Verify if products are displayed
try:
    products_displayed = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    if not products_displayed.is_displayed():
        raise AssertionError("Products are not displayed after clicking the Login button")
except Exception as e:
    driver.save_screenshot('error_verify_products_displayed.png')
    raise AssertionError("Failed to verify that products are displayed") from e

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CSS_SELECTOR, ".error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        if error_texts:
            raise AssertionError(f"Detected errors on the page: {error_texts}")
except Exception as e:
    driver.save_screenshot('error_checking_for_errors.png')
    raise AssertionError("Failed to check for errors on the page") from e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

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
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Search button
    search_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchBtn")))
    search_button.click()
    
    # Verify that products from the selected category are displayed
    products_list = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    if products_list.is_displayed() and products_list.find_elements(By.XPATH, ".//*"):
        print("Products are displayed.")
    else:
        raise AssertionError("Expected products are not displayed.")
    
except Exception as e:
    # Handle any alert or popup gracefully
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert displayed: {alert_text}")
    except:
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError(f"An error occurred: {str(e)}")