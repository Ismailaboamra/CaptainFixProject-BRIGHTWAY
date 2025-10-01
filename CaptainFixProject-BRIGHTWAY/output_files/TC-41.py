
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")

# Test Step: 6. **Test Case 6: Add Item to Cart**

driver.quit()
