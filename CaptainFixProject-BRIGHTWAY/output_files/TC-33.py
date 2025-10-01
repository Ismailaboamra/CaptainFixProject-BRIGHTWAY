
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")

# Test Step: 2. Apply filters (e.g., select "Used" and set a price range).

driver.quit()
