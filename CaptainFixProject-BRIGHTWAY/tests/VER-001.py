from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginPage")))
    
    actual_username_displayed = driver.find_element(By.ID, "username").is_displayed()
    assert actual_username_displayed, "Expected username field is not displayed correctly."
    
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Enter username
try:
    username_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_input.send_keys("emilys")
    
    # Verification: Check if the username is displayed correctly
    actual_username = username_input.get_attribute("value")
    expected_username = "emilys"
    assert actual_username == expected_username, f"Expected username '{expected_username}' but got '{actual_username}'"
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

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
    
    # Verification: Check if the user name is displayed correctly
    user_name_displayed = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "userName"))
    ).text
    
    expected_user_name = "Expected User Name"  # Replace with the actual expected user name
    assert user_name_displayed == expected_user_name, f"Expected user name '{expected_user_name}' but got '{user_name_displayed}'"

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# First step: Navigate to the page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Click the Login button
try:
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    login_button.click()
    
    # Verification: Check if the user name is displayed correctly
    user_name_displayed = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "userName"))
    ).text
    
    expected_user_name = "Expected User Name"  # Replace with the actual expected user name
    assert user_name_displayed == expected_user_name, f"Expected user name '{expected_user_name}', but got '{user_name_displayed}'"

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Verify that the user name is displayed in the navbar
try:
    user_name_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "userName"))
    )
    actual_user_name = user_name_element.text
    expected_user_name = "Expected User Name"  # Replace with the actual expected user name
    assert actual_user_name == expected_user_name, f"Expected user name '{expected_user_name}' but got '{actual_user_name}'"
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"Error occurred while verifying user name: {str(e)}")