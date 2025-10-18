from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input to be present
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
    
    # Check for any error messages on the page
    error_message = driver.find_element(By.ID, "usernameError").text
    if error_message:
        print("Error message detected:", error_message)
    else:
        print("No error message detected.")
    
    # Verify the expected result
    expected_error_message = "Error message displayed for empty search input."
    if error_message != expected_error_message:
        raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{error_message}'")

except Exception as e:
    # Handle any alerts or popups
    try:
        WebDriverWait(driver, 20).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        print("Alert detected:", alert_text)
        alert.accept()
    except:
        print("No alert detected.")

    # Log the exception for debugging
    print("An error occurred:", str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    print("Error entering username:", e)

try:
    # Check for any error messages after entering the username
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message != "":  # Assuming the expected error message is not empty
        print("Error message displayed:", error_message)
        assert error_message == "Error message displayed for empty search input.", "Expected error message not displayed."
    else:
        print("No error message displayed.")
except Exception as e:
    print("Error checking for error message:", e)

try:
    # Check for any JavaScript alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    print("Alert text:", alert_text)
    alert.accept()
except Exception as e:
    print("No alert present or error checking alert:", e)

# Detect any inline form errors or notifications
try:
    inline_error = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if inline_error:
        print("Inline error detected:", inline_error)
except Exception as e:
    print("No inline error detected or error checking inline error:", e)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the password input field to be present and enter the password
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("emilyspass")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter password: " + str(e))

try:
    # Check for any error messages on the page
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "passwordError"))).text
    if error_message != "":
        print("Error message displayed: ", error_message)
        assert error_message == "Error message displayed for empty search input."
    else:
        raise AssertionError("Expected error message not displayed.")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify error message: " + str(e))

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
    alert.accept()
except Exception as e:
    alert_text = None

# Verify if the error message for empty input is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError")))
    actual_error_text = error_message.text
    expected_error_text = "This field is required."  # Assuming this is the expected error message
    if actual_error_text != expected_error_text:
        raise AssertionError(f"Expected error message: '{expected_error_text}', but got: '{actual_error_text}'")
except Exception as e:
    driver.save_screenshot('error_message_verification.png')
    raise AssertionError("Error message for empty input not displayed") from e

# Detect any inline errors or notifications
try:
    inline_error = driver.find_elements(By.CSS_SELECTOR, ".error-message")
    for error in inline_error:
        if error.is_displayed():
            print(f"Detected error message: {error.text}")
except Exception as e:
    raise AssertionError("Failed to detect inline errors") from e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the search button to be present and click it
    search_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchBtn")))
    search_button.click()
except Exception as e:
    driver.save_screenshot('error_click_search_button.png')
    raise AssertionError("Failed to click the search button.") from e

# Check for any alerts after clicking the search button
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Please enter a search term."  # Assuming this is the expected alert text
    if alert_text != expected_alert_text:
        driver.save_screenshot('error_alert_text.png')
        raise AssertionError(f"Unexpected alert text: {alert_text}")
    alert.accept()
except Exception as e:
    driver.save_screenshot('error_no_alert.png')
    raise AssertionError("No alert appeared after clicking the search button.") from e

# Verify if the error message for empty search input is displayed
try:
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message")))
    if error_message.is_displayed() and error_message.text == "Please enter a search term.":
        print("Error message displayed as expected.")
    else:
        raise AssertionError("Error message not displayed or does not match expected text.")
except Exception as e:
    driver.save_screenshot('error_message_not_displayed.png')
    raise AssertionError("Failed to verify the error message for empty search input.") from e