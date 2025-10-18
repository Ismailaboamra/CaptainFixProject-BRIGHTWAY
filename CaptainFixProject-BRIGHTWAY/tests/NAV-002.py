from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginPage")))
    
    # Verify that the user is redirected to the shop page
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "shopPage")))
    actual_result = driver.find_element(By.ID, "shopPage").is_displayed()
    expected_result = True
    assert actual_result == expected_result, "User is not redirected to the shop page."

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the login page and enter the username
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to enter username: " + str(e))

# Step 2: Verify redirection to the shop page
try:
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "shopPage")))
    assert driver.current_url == "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#shopPage", "User is not redirected to the shop page."
except AssertionError as e:
    driver.save_screenshot('redirection_error.png')
    raise AssertionError("Redirection failed: " + str(e))
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Error during redirection verification: " + str(e))

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