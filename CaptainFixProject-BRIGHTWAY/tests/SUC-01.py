from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the login form to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm")))
    
    # Verify that we are on the login page by checking the presence of the login form
    assert driver.find_element(By.ID, "loginForm").is_displayed(), "Login form is not displayed."
    
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
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

# Check for any alerts after login
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    # Verify alert text if necessary
except Exception as e:
    pass  # No alert present, continue

# Verify that products are filtered correctly based on the selected category
try:
    # Assuming that the products are displayed in the productsList div
    products_list = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    if products_list.is_displayed():
        print("Products are displayed correctly.")
    else:
        raise AssertionError("Products are not displayed.")
except Exception as e:
    driver.save_screenshot("error_products_display.png")
    raise AssertionError("Failed to verify products display: " + str(e))

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
    username_error = driver.find_element(By.ID, "usernameError").text
    if username_error:
        error_messages.append(username_error)
except:
    pass

try:
    password_error = driver.find_element(By.ID, "passwordError").text
    if password_error:
        error_messages.append(password_error)
except:
    pass

if alert_text:
    error_messages.append(alert_text)

if error_messages:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Detected errors: " + ", ".join(error_messages))

# Verify that products are filtered correctly based on the selected category
try:
    # Assuming that after login, the products are displayed and we can check for their presence
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    products_list = driver.find_element(By.ID, "productsList").text
    assert products_list != "", "No products found after login."
except AssertionError as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Verification failed: " + str(e))
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify products: " + str(e))

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

# Verify if the products are filtered correctly based on the selected category
try:
    # Assuming that after login, we should check for the presence of products
    products_container = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsContainer")))
    assert products_container.is_displayed(), "Products are not displayed after login."
except Exception as e:
    driver.save_screenshot('error_verify_products_displayed.png')
    raise AssertionError("Failed to verify that products are displayed after login") from e

# Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            driver.save_screenshot('error_messages_found.png')
            raise AssertionError(f"Error message found: {error.text}")
except Exception as e:
    driver.save_screenshot('error_checking_messages.png')
    raise AssertionError("Failed to check for error messages") from e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the category filter to be present and select a category
    category_filter = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "categoryFilter")))
    category_filter.click()
    category_filter.find_element(By.XPATH, "//option[not(@value='')]").click()  # Select the first available category

    # Verify that products are filtered correctly
    # This part assumes that the filtered products will be displayed in the productsList div
    products_list = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    if not products_list.is_displayed() or len(products_list.find_elements(By.XPATH, ".//*")) == 0:
        raise AssertionError("No products found after filtering.")

except Exception as e:
    # Handle any errors that occur during the interaction
    print(f"An error occurred: {e}")
    driver.save_screenshot("error_screenshot.png")
    raise

# Check for any alerts or error messages
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    # You can add verification for alert text if needed
except:
    pass  # No alert present

# Check for inline errors or notifications
error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
for error in error_messages:
    if error.is_displayed():
        print(f"Error message detected: {error.text}")
        raise AssertionError(f"Unexpected error message: {error.text}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page (if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the category filter to be present and select a category
    category_filter = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "categoryFilter")))
    category_filter.click()
    # Assuming we want to select the first option (All Categories)
    category_filter.find_element(By.XPATH, "//option[1]").click()
    
    # Wait for the products to be displayed based on the selected category
    products_list = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    
    # Verify that products are displayed correctly
    if products_list.is_displayed() and len(products_list.find_elements(By.XPATH, ".//*")) > 0:
        print("Products are displayed correctly based on the selected category.")
    else:
        raise AssertionError("No products are displayed for the selected category.")
    
except Exception as e:
    # Handle any errors that occur during the process
    print(f"An error occurred: {str(e)}")
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Test failed due to an error.")