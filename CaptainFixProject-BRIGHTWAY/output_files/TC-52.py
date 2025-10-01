
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")

# Test Step: 3. Click "Proceed to checkout."

driver.quit()
