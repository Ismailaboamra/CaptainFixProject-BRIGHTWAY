
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")

# Test Step: - **Expected Result:** The website layout adjusts appropriately for mobile screens, and all functionalities work as intended.

driver.quit()
