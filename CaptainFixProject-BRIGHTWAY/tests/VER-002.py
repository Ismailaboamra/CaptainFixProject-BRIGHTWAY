from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Verify that the cart shows '0' items initially
    cart_count = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "cartCount"))
    ).text
    assert cart_count == '0', f"Expected cart count to be '0', but got '{cart_count}'"
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Error while verifying cart count: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter username
try:
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter username: " + str(e))

# Verification: Check if the cart shows '0' items initially
try:
    cart_count = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "cartCount"))).text
    assert cart_count == "0", f"Expected cart count to be '0', but got '{cart_count}'"
except AssertionError as ae:
    driver.save_screenshot("error_screenshot.png")
    raise ae
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to verify cart count: " + str(e))

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
    
    # Verification: Check if the cart shows '0' items initially
    cart_count = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "cartCount"))
    ).text
    assert cart_count == '0', f"Expected cart count to be '0', but got '{cart_count}'"
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
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
    
    # Verification: Check if the cart shows '0' items initially
    cart_count = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "cartCount"))
    ).text
    
    assert cart_count == '0', f"Expected cart count to be '0', but got '{cart_count}'"
    
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Click the Cart button
try:
    cart_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "cartBtn"))
    )
    cart_button.click()
    
    # Verification: Check if the cart shows '0' items initially
    cart_count = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "cartCount"))
    ).text
    assert cart_count == '0', f"Expected cart count to be '0', but got '{cart_count}'"
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Verify that the cart summary shows '0' items initially
try:
    cart_count_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "cartCount"))
    )
    actual_cart_count = cart_count_element.text
    expected_cart_count = '0'
    assert actual_cart_count == expected_cart_count, f"Expected cart count to be '{expected_cart_count}', but got '{actual_cart_count}'"
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Error occurred while verifying cart count: {str(e)}")