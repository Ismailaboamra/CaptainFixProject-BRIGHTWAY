from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginPage")))
    
    # Verify that the user is redirected to the shop page
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "shopPage")))
    assert driver.find_element(By.ID, "shopPage").is_displayed(), "User is not redirected to the shop page."
    
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the login page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter username
try:
    username_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_input.send_keys("emilys")
    
    # Verification: Check if the user is redirected to the shop page
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "shopPage"))
    )
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#shopPage", "User is not redirected to the shop page."
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

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
    
    # Verification: Check if the user is redirected back to the shop page
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "shopPage"))
    )
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#shopPage", "User is not redirected to the shop page."
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
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    login_button.click()
    
    # Verification: Check if redirected to the shop page
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "shopPage"))
    )
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#shopPage", "User is not redirected to the shop page."
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Search for a product
try:
    search_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "searchInput"))
    )
    search_input.send_keys("example product")  # Replace with actual product name if needed
except Exception as e:
    driver.save_screenshot("search_input_error.png")
    raise AssertionError("Failed to interact with the search input: " + str(e))

try:
    search_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "searchBtn"))
    )
    search_button.click()
except Exception as e:
    driver.save_screenshot("search_button_error.png")
    raise AssertionError("Failed to click the search button: " + str(e))

# Step 3: Verify redirection back to the shop page
try:
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "shopPage"))
    )
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html", "User is not redirected back to the shop page."
except AssertionError as e:
    driver.save_screenshot("redirection_error.png")
    raise AssertionError("Redirection verification failed: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the shop page if this is the first step
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Click on a product to view details
try:
    product_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".products-grid .product-item"))  # Assuming product items have a class 'product-item'
    )
    product_element.click()
except Exception as e:
    driver.save_screenshot('error_click_product.png')
    raise AssertionError(f"Failed to click on the product: {str(e)}")

# Step 3: Verify user is redirected back to the shop page
try:
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "shopPage"))
    )
    assert "shopPage" in driver.current_url, "User is not redirected back to the shop page."
except Exception as e:
    driver.save_screenshot('error_redirect_shop_page.png')
    raise AssertionError(f"Redirection to shop page failed: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Click the Back to Shop button
try:
    back_to_shop_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "backToShopBtn"))
    )
    back_to_shop_button.click()
    
    # Verification: Check if user is redirected back to the shop page
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "shopPage"))
    )
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html", "User is not redirected back to the shop page."

except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")