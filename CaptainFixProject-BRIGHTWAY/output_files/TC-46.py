
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")

# Test Step: - **Expected Result:** Item is added to the cart, and a confirmation message is displayed.

driver.quit()
