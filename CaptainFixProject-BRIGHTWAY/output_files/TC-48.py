
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")

# Test Step: - **Objective:** Verify that users can complete a purchase through the checkout process.

driver.quit()
