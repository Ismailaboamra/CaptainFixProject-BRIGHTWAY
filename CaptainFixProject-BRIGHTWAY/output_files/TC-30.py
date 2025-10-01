
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")

# Test Step: - **Objective:** Verify that users can filter search results by category, price, and condition.

driver.quit()
