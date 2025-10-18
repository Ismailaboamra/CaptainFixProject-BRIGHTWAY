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
    raise AssertionError("Failed to open the login page: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the username input field to be present and enter the username
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter username: " + str(e))

try:
    # Check for any inline errors after entering the username
    error_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "usernameError"))).text
    if error_message:
        raise AssertionError(f"Inline error detected: {error_message}")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to check for username error: " + str(e))

try:
    # Submit the form
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))).click()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to click the login button: " + str(e))

try:
    # Wait for the search results to be displayed
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    products_list = driver.find_element(By.ID, "productsList").text
    if not products_list:
        raise AssertionError("No search results displayed.")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to verify search results: " + str(e))

try:
    # Check for any alerts after the action
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    # You can add verification for alert text if needed
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("No alert was present or failed to handle alert: " + str(e))

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

# Check for any alerts after login attempt
try:
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    # Verify alert text if needed
except Exception as e:
    pass  # No alert present, continue

# Verify if search results are displayed
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "productsList")))
    products_list = driver.find_element(By.ID, "productsList")
    if products_list.is_displayed():
        print("Search results are displayed.")
    else:
        raise AssertionError("Search results are not displayed.")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to verify search results: " + str(e))

# Detect and verify any errors on the page
error_messages = []
try:
    username_error = driver.find_element(By.ID, "usernameError").text
    if username_error:
        error_messages.append(username_error)
except Exception:
    pass

try:
    password_error = driver.find_element(By.ID, "passwordError").text
    if password_error:
        error_messages.append(password_error)
except Exception:
    pass

if error_messages:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Detected errors on the page: " + ", ".join(error_messages))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Click the Login button
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    login_button.click()
    
    # Wait for potential alert and verify its presence
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    expected_alert_text = "Expected alert message"  # Replace with the actual expected alert message
    if alert_text != expected_alert_text:
        driver.save_screenshot('alert_error.png')
        raise AssertionError(f"Unexpected alert text: {alert_text}")
    alert.accept()

except Exception as e:
    driver.save_screenshot('error.png')
    raise AssertionError(f"An error occurred: {str(e)}")

# Verify that search results are displayed
try:
    search_results_info = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchResultsInfo")))
    if not search_results_info.is_displayed():
        raise AssertionError("Search results are not displayed.")
except Exception as e:
    driver.save_screenshot('verification_error.png')
    raise AssertionError(f"Verification failed: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Wait for the search input to be present and enter a product name
    search_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchInput")))
    search_input.send_keys("Sample Product Name")  # Replace with the actual product name you want to search for

    # Wait for the search button to be clickable and click it
    search_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchBtn")))
    search_button.click()

    # Wait for search results to be displayed
    search_results_info = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchResultsInfo")))

    # Verify that search results are displayed
    if search_results_info.text == "":
        raise AssertionError("Expected search results to be displayed, but none were found.")

except Exception as e:
    # Handle any errors that occur during the process
    print(f"An error occurred: {e}")
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
    
    # Verify search results are displayed
    search_results_info = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchResultsInfo")))
    if not search_results_info.is_displayed():
        raise AssertionError("Search results are not displayed.")
    
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