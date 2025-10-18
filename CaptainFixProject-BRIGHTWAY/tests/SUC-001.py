from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%A7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Verify that the login page is displayed
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginForm")))
    actual_result = driver.find_element(By.ID, "loginForm").is_displayed()
    expected_result = True
    assert actual_result == expected_result, "Login page is not displayed as expected."
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Error while verifying login page: {str(e)}")

# Step 2: Check for errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        assert not error_texts, f"Inline errors detected: {error_texts}"
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Error while checking for inline errors: {str(e)}")

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
    
    # Verification: Check if products in the selected category are displayed
    products_displayed = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "productsList"))
    )
    assert products_displayed.is_displayed(), "Expected products are not displayed."
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter password
try:
    password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.send_keys("emilyspass")
    
    # Verification: Check if products in the selected category are displayed
    products_displayed = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "productsList"))
    )
    assert products_displayed.is_displayed(), "Expected products are not displayed."
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Click the Login button
try:
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    login_button.click()
    
    # Verification: Check if products in the selected category are displayed
    products_displayed = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "productsList"))
    )
    assert products_displayed.is_displayed(), "Expected products are not displayed."
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Select a category from the category filter
try:
    category_filter = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "categoryFilter"))
    )
    category_filter.click()
    # Assuming we want to select the first option (All Categories)
    category_filter.find_element(By.XPATH, "//option[1]").click()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Failed to select category: {str(e)}")

# Step 3: Verify that products in the selected category are displayed
try:
    products_displayed = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "productsList"))
    )
    assert products_displayed.is_displayed(), "Products are not displayed in the selected category."
except AssertionError as ae:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Verification failed: {str(ae)}")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Error during verification: {str(e)}")

# Step 4: Check for any errors on the page
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    if error_messages:
        error_texts = [error.text for error in error_messages if error.text]
        assert not error_texts, f"Inline errors detected: {error_texts}"
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Error checking for inline errors: {str(e)}")

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
    
    # Verification: Check if products in the selected category are displayed
    products_displayed = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "productsList"))
    )
    assert products_displayed.is_displayed(), "Expected products are not displayed."
    
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")