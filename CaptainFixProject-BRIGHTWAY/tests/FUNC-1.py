from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the login form to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm")))
    
    # Verify that the login page is displayed by checking the presence of the username input
    username_input = driver.find_element(By.ID, "username")
    assert username_input.is_displayed(), "Login page is not displayed correctly."
    
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred while opening the login page: {str(e)}")

# Detect any errors on the page
try:
    error_message = driver.find_element(By.ID, "usernameError").text
    if error_message:
        raise AssertionError(f"Error detected on the page: {error_message}")
except Exception:
    pass  # No error message found, continue

# Proceed to search for 'laptop'
try:
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.send_keys("laptop")
    
    search_button = driver.find_element(By.ID, "searchBtn")
    search_button.click()
    
    # Wait for search results to be displayed
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    
    # Verify that search results are displayed
    products_list = driver.find_element(By.ID, "productsList")
    assert products_list.is_displayed() and len(products_list.find_elements(By.XPATH, ".//*")) > 0, "Search results for 'laptop' are not displayed."
    
except Exception as e:
    driver.save_screenshot('error_screenshot_after_search.png')
    raise AssertionError(f"An error occurred during the search: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input field to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys('emilys')
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Check for any inline errors or alerts after entering the username
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message:
        raise AssertionError(f"Inline error detected: {error_message}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to check for errors: " + str(e))

try:
    # Submit the form
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click the login button: " + str(e))

try:
    # Wait for the search results to be displayed
    search_results_info = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchResultsInfo"))).text
    if 'laptop' not in search_results_info:
        raise AssertionError("Expected search results for 'laptop' are not displayed.")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify search results: " + str(e))

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
    # Check for any errors on the page after entering the password
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError"))).text
    if error_message:
        raise AssertionError(f"Error detected: {error_message}")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to check for errors: " + str(e))

try:
    # Submit the login form
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm"))).submit()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to submit the login form: " + str(e))

try:
    # Wait for the search results to be displayed
    search_results_info = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchResultsInfo"))).text
    if 'laptop' not in search_results_info:
        raise AssertionError("Expected search results for 'laptop' are not displayed.")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify search results: " + str(e))

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

# Check for any alerts after clicking the button
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Expected alert text here"  # Replace with the actual expected alert text
    if alert_text != expected_alert_text:
        driver.save_screenshot('error_alert_text.png')
        raise AssertionError(f"Unexpected alert text: {alert_text}")
    alert.accept()
except Exception as e:
    pass  # No alert present, continue

# Verify that search results for 'laptop' are displayed
try:
    search_results_info = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchResultsInfo")))
    actual_text = search_results_info.text
    expected_text = "Search results for 'laptop' are displayed."  # Replace with the actual expected text
    if actual_text != expected_text:
        driver.save_screenshot('error_search_results.png')
        raise AssertionError(f"Expected: {expected_text}, but got: {actual_text}")
except Exception as e:
    driver.save_screenshot('error_verification_search_results.png')
    raise AssertionError("Failed to verify search results") from e

# Detect any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            driver.save_screenshot('error_messages_detected.png')
            raise AssertionError(f"Detected error message: {error.text}")
except Exception as e:
    pass  # No errors detected, continue

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the search input to be present and enter 'laptop'
    search_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchInput")))
    search_input.send_keys('laptop')
    
    # Click the search button
    search_button = driver.find_element(By.ID, "searchBtn")
    search_button.click()
    
    # Wait for search results to be displayed
    search_results_info = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchResultsInfo")))
    
    # Verify that search results for 'laptop' are displayed
    if 'laptop' not in search_results_info.text.lower():
        raise AssertionError("Expected search results for 'laptop' are not displayed.")
    
except Exception as e:
    # Handle any alerts or errors
    try:
        alert = WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert displayed: {alert_text}")
    except:
        # Check for inline errors or notifications
        error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
        for error in error_messages:
            if error.is_displayed():
                raise AssertionError(f"Inline error displayed: {error.text}")
    
    # If no alerts or errors, take a screenshot for debugging
    driver.save_screenshot('error_screenshot.png')
    raise e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Search button
    search_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchBtn")))
    search_button.click()
    
    # Wait for search results to be displayed
    search_results_info = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchResultsInfo")))
    
    # Verify that search results are displayed
    actual_result = search_results_info.text
    expected_result = "Search results for 'laptop' are displayed."
    
    if expected_result not in actual_result:
        raise AssertionError(f"Expected result not found. Actual result: {actual_result}")

except Exception as e:
    # Handle any alerts or popups
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        raise AssertionError(f"Alert appeared with text: {alert_text}")
    except:
        # Take a screenshot for debugging
        driver.save_screenshot("error_screenshot.png")
        raise AssertionError(f"An error occurred: {str(e)}")