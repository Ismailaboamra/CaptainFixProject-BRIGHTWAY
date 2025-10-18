from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open the login page
try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginForm")))
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to open the login page: " + str(e))

# Verification: Check if the login form is displayed
try:
    login_form = driver.find_element(By.ID, "loginForm")
    assert login_form.is_displayed(), "Login form is not displayed."
except AssertionError as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Verification failed: " + str(e))

# Error Detection: Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            raise AssertionError("Inline error detected: " + error.text)
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Error detection failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter username
try:
    username_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_input.send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Failed to enter username: {str(e)}")

# Step 3: Verify search results are displayed based on the product name
try:
    search_results_info = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "searchResultsInfo"))
    )
    actual_result = search_results_info.text
    expected_result = "Search results are displayed based on the product name."
    assert actual_result == expected_result, f"Expected: '{expected_result}', but got: '{actual_result}'"
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Verification failed: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
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

# Step 3: Check for search results
try:
    search_results_info = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "searchResultsInfo"))
    )
    
    # Verification: Check if search results are displayed
    assert search_results_info.is_displayed(), "Search results are not displayed."
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to verify search results: {str(e)}")

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
    
    # Verification: Check if search results are displayed
    try:
        search_results_info = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "searchResultsInfo"))
        )
        assert search_results_info.is_displayed(), "Search results are not displayed."
    except Exception as e:
        driver.save_screenshot("search_results_error.png")
        raise AssertionError("Expected search results are not displayed.") from e

except Exception as e:
    driver.save_screenshot("login_button_error.png")
    raise AssertionError("Login button could not be clicked.") from e

# Error detection after the step
# (This part would typically include checks for alerts, modals, inline errors, etc.)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter a product name in the search input
try:
    search_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "searchInput"))
    )
    search_input.clear()
    search_input.send_keys("Sample Product")  # Replace with the actual product name you want to search
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to enter product name in search input: {str(e)}")

# Step 3: Click the search button
try:
    search_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "searchBtn"))
    )
    search_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Failed to click the search button: {str(e)}")

# Step 4: Verify that search results are displayed
try:
    search_results_info = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "searchResultsInfo"))
    )
    actual_results = search_results_info.text
    expected_results = "Expected search results based on the product name"  # Define what the expected results should be
    assert actual_results != "", "No search results displayed."
    assert expected_results in actual_results, f"Expected results not found. Actual: {actual_results}"
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Search results verification failed: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Click the Search button
try:
    search_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "searchBtn"))
    )
    search_button.click()
    
    # Verification: Check if search results are displayed
    search_results_info = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "searchResultsInfo"))
    )
    assert search_results_info.is_displayed(), "Search results are not displayed."
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")