
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")

# Test Step: 2. Enter a search term (e.g., "laptop") in the search bar.

driver.quit()
