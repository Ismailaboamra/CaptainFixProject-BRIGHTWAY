
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")

# Test Step: - **Expected Result:** Order confirmation page is displayed, and the order is recorded in the user’s purchase history.

driver.quit()
