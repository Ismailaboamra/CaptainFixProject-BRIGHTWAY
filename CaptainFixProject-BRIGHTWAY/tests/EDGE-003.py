driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the shop page
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "searchBtn"))).click()

# Verification step
error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "usernameError"))).text
expected_error_message = "This field is required."  # Assuming this is the expected error message for empty input
if error_message != expected_error_message:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"Expected error message: '{expected_error_message}', but got: '{error_message}'")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Click on the 'Search' button without entering any text
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "searchBtn")))
search_button.click()

# Wait for the error message to be displayed
time.sleep(1)  # Adjust sleep time if necessary

# Verify that the error message is displayed
error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "searchResultsInfo")))

if error_message.text == "":
    driver.save_screenshot("error_message_screenshot.png")
    raise AssertionError("Expected error message for empty search input was not displayed.")