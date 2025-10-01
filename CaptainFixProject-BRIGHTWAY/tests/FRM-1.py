from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("https://mawdoo3.com/")

try:
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("تغذية")
    search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    search_button.click()

    # Wait for the results to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'نتائج البحث')]"))
    )
except Exception as e:
    driver.save_screenshot("error_screenshot.png")  # Capture a screenshot if an error occurs
    print(f"An error occurred: {e}")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Assuming driver is already defined and passed in
driver.get("https://mawdoo3.com/")

try:
    # Wait for the search input to be present
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    # Input the search term 'تغذية'
    search_input.send_keys("تغذية")
    
    # Submit the search form
    search_input.submit()
    
    # Wait for the results to be displayed
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'نتائج البحث')]"))
    )
    
except Exception as e:
    driver.save_screenshot("error_screenshot.png")  # Capture a screenshot if an error occurs
    print(f"An error occurred: {e}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

# Assuming driver is already defined and passed in
driver.get("https://mawdoo3.com/")

try:
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='search' and @placeholder='ابحث هنا...']"))
    )
    search_input.send_keys("تغذية")
    search_button = driver.find_element(By.XPATH, "//button[@type='submit' and @aria-label='Search']")
    search_button.click()
except Exception as e:
    driver.save_screenshot("error_screenshot.png")  # Capture a screenshot if an error occurs
    print(f"An error occurred: {e}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get("https://mawdoo3.com/")

try:
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Search']"))
    )
    search_button.click()
except Exception as e:
    driver.save_screenshot("screenshot.png")  # Capture a screenshot if the element is not found or action fails
    print(f"An error occurred: {e}")