
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")

# Test Step: - **Expected Result:** User account is created, and the user is redirected to the welcome page.

driver.quit()
