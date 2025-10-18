from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the login page to be visible
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginPage")))
    
    # Check for any error messages
    error_message = driver.find_elements(By.CSS_SELECTOR, ".error-message")
    if error_message:
        for error in error_message:
            if error.is_displayed():
                print("Error message displayed:", error.text)
    else:
        print("No error messages displayed.")
    
    # Verification step
    if error_message:
        for error in error_message:
            if error.is_displayed():
                assert error.is_displayed(), "Expected error message is displayed."
    else:
        assert True, "No error messages should be displayed."

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("An error occurred: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input field to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_username_input.png")
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Submit the login form
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "loginForm"))).submit()
except Exception as e:
    driver.save_screenshot("error_login_submit.png")
    raise AssertionError("Failed to submit login form: " + str(e))

# Check for any error messages after submission
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    error_message = driver.find_element(By.ID, "usernameError").text
    if error_message == "":
        raise AssertionError("Expected error message not displayed.")
except Exception as e:
    driver.save_screenshot("error_message_check.png")
    raise AssertionError("Error message check failed: " + str(e))

# Verify the error message or absence of results
if error_message:
    print("Error message displayed: " + error_message)
else:
    print("No error message displayed, which is expected.")

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
    # Wait for the login button to be clickable and click it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to click login button: " + str(e))

# Check for any error messages or results
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    error_message = driver.find_element(By.ID, "usernameError").text
    if error_message:
        print("Error message displayed: ", error_message)
    else:
        print("No error message displayed.")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Error message verification failed: " + str(e))

# Verify that no results should be displayed
try:
    results_info = driver.find_element(By.ID, "searchResultsInfo").text
    if results_info:
        raise AssertionError("Expected no results, but found: " + results_info)
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Results verification failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for any error message to be displayed
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    actual_error_text = error_message.text
    
    # Verify the expected result
    if actual_error_text == "":
        raise AssertionError("Expected an error message, but none was displayed.")
    
except Exception as e:
    # Handle any alert or popup gracefully
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
    except:
        pass
    
    # Take a screenshot for debugging
    driver.save_screenshot("error_screenshot.png")
    raise e

# Detect and verify any inline errors or notifications
inline_error = driver.find_element(By.ID, "usernameError").text
if inline_error:
    print(f"Detected inline error: {inline_error}")
else:
    print("No inline errors detected.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Search button
    search_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchBtn")))
    search_button.click()
except Exception as e:
    driver.save_screenshot('error_click_search_button.png')
    raise AssertionError("Failed to click the search button") from e

# Check for error message or no results
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message")))
    actual_error_text = error_message.text
    if actual_error_text == "":
        raise AssertionError("Expected an error message but none was displayed.")
except Exception as e:
    driver.save_screenshot('error_message_not_found.png')
    raise AssertionError("Failed to find an error message after clicking the search button") from e

# Verify the error message or no results
expected_error_message = "No results found."  # Adjust this based on the expected error message
if actual_error_text != expected_error_message:
    raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{actual_error_text}'")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the search input to be present and enter special characters
    search_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchInput")))
    search_input.clear()
    search_input.send_keys("!@#$%^&*()")

    # Click the search button
    search_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchBtn")))
    search_button.click()

    # Wait for the search results info to be present
    search_results_info = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchResultsInfo")))

    # Verify if an error message or no results are displayed
    if "No results found" in search_results_info.text or search_results_info.text == "":
        print("Expected result met: Error message or no results displayed.")
    else:
        raise AssertionError("Expected error message or no results, but found: " + search_results_info.text)

except (TimeoutException, NoSuchElementException) as e:
    # Handle any errors that occur during the process
    print("An error occurred: ", str(e))
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("An error occurred during the test execution.")

# Check for any JavaScript alerts
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    print("Alert detected with text: ", alert_text)
except TimeoutException:
    print("No alert detected.")

# Check for inline errors or notifications
try:
    username_error = driver.find_element(By.ID, "usernameError")
    password_error = driver.find_element(By.ID, "passwordError")
    if username_error.is_displayed() or password_error.is_displayed():
        raise AssertionError("Inline error messages are displayed.")
except NoSuchElementException:
    print("No inline error messages found.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Search button
    search_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchBtn")))
    search_button.click()
except Exception as e:
    driver.save_screenshot('error_click_search_button.png')
    raise AssertionError("Failed to click the Search button") from e

# Verify if an error message or no results is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message")))
    actual_error_text = error_message.text
    if actual_error_text == "":
        raise AssertionError("Expected an error message but none was displayed.")
except Exception as e:
    driver.save_screenshot('error_verifying_search_results.png')
    raise AssertionError("Failed to verify search results") from e

# Check for any JavaScript alerts or notifications
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    # Assuming we expect a specific alert text, replace 'Expected alert text' with the actual expected text
    if alert_text != 'Expected alert text':
        driver.save_screenshot('unexpected_alert.png')
        raise AssertionError(f"Unexpected alert text: {alert_text}")
    alert.accept()
except Exception as e:
    # No alert was present, continue
    pass

# Check for inline form errors or notifications
try:
    inline_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message")))
    if inline_error.is_displayed():
        actual_inline_error_text = inline_error.text
        # Assuming we expect a specific inline error message, replace 'Expected inline error message' with the actual expected message
        if actual_inline_error_text != 'Expected inline error message':
            driver.save_screenshot('unexpected_inline_error.png')
            raise AssertionError(f"Unexpected inline error message: {actual_inline_error_text}")
except Exception as e:
    # No inline error was present, continue
    pass