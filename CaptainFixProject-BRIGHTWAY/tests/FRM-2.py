from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("https://mawdoo3.com/")

try:
    # Wait for the search input to be present
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    # Attempt to submit an empty search
    search_input.submit()
    
    # Wait for the error message to be displayed
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'لا توجد نتائج')]"))
    )
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")  # Capture a screenshot if an error occurs
    print(f"An error occurred: {e}")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("https://mawdoo3.com/")

try:
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='search' and @placeholder='ابحث هنا...']"))
    )
    # Assuming the next step would be to check for results or an error message
except Exception as e:
    driver.save_screenshot("search_box_not_found.png")  # Capture screenshot if the element is not found
    print("Error:", e)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Navigate to the website
driver.get("https://mawdoo3.com/")

try:
    # Wait for the search input to be present and interact with it
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_input.clear()  # Leave the search input empty

    # Submit the search form
    search_input.submit()

    # Wait for the error message to be displayed
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'error')]"))
    )

    # Optionally, take a screenshot if needed
    driver.save_screenshot("error_message_screenshot.png")

except Exception as e:
    # Capture a screenshot if an error occurs
    driver.save_screenshot("error_message_screenshot.png")
    print(f"An error occurred: {e}")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Navigate to the website
driver.get("https://mawdoo3.com/")

try:
    # Click the search button
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Search']"))
    )
    search_button.click()

    # Wait for the error message to be displayed
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'لا توجد نتائج')]"))
    )

except Exception as e:
    driver.save_screenshot("error_screenshot.png")  # Capture a screenshot if an error occurs
    print(f"An error occurred: {e}")