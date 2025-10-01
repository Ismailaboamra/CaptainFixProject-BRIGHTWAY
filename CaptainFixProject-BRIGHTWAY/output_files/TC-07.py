
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")

# Test Step: - **Objective:** Verify that a new user can successfully register for an account.

driver.quit()
