driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the login page to load and then log in (assuming login is required)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginForm")))

# Fill in the username and password (assuming valid credentials are known)
driver.find_element(By.ID, "username").send_keys("valid_username")
driver.find_element(By.ID, "password").send_keys("valid_password")
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

# Wait for the shop page to load
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "shopPage")))

# Verify that products are displayed
products_displayed = driver.find_element(By.ID, "productsList").is_displayed()
if not products_displayed:
    driver.save_screenshot("screenshot.png")
    raise AssertionError("Expected products to be displayed, but they are not.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Select a category from the 'Filter by Category' dropdown
category_filter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "categoryFilter"))
)
category_filter.click()

# Assuming we want to select the first option (All Categories)
category_filter.find_element(By.XPATH, ".//option[1]").click()

# Verification step
search_results_info = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "searchResultsInfo"))
)
if search_results_info.text == "":
    driver.save_screenshot("screenshot.png")
    raise AssertionError("Expected products to be displayed based on the selected category, but none were found.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the products to be displayed
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "productsList")))

# Verify that products are displayed
products_list = driver.find_element(By.ID, "productsList")
if products_list.is_displayed() and products_list.text.strip() != "":
    print("Products are displayed.")
else:
    driver.save_screenshot('screenshot.png')
    raise AssertionError("Expected products to be displayed, but none were found.")