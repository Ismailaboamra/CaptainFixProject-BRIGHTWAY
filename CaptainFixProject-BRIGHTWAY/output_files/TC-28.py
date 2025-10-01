
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")

# Test Step: - **Expected Result:** Search results page displays relevant items based on the search term.

driver.quit()
