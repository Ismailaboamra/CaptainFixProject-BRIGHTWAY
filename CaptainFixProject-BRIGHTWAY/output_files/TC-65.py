
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")

# Test Step: - **Objective:** Verify that users can recover their password if forgotten.

driver.quit()
