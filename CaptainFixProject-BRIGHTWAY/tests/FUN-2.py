driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the login form to be visible and fill in the username and password
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginForm")))

# Assuming login is required, fill in the username and password
driver.find_element(By.ID, "username").send_keys("your_username")
driver.find_element(By.ID, "password").send_keys("your_password")
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

# Wait for the shop page to be visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "shopPage")))

# Verify that the shop page is displayed
if not driver.find_element(By.ID, "shopPage").is_displayed():
    driver.save_screenshot('shop_page_not_displayed.png')
    raise AssertionError("Shop page is not displayed.")

# Wait for the products to be loaded
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "productsList")))

# Verify that products are filtered by the selected category
# Assuming a category is selected, you would typically select it here
# For example, selecting a category (if applicable)
# driver.find_element(By.ID, "categoryFilter").click()
# driver.find_element(By.XPATH, "//option[text()='Some Category']").click()

# Verify that products are displayed
if not driver.find_element(By.ID, "productsList").is_displayed():
    driver.save_screenshot('products_not_displayed.png')
    raise AssertionError("Products are not displayed.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Select a category from the category filter
category_filter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "categoryFilter"))
)
category_filter.click()

# Assuming we want to select the first option (All Categories)
category_filter.find_element(By.XPATH, "./option[1]").click()

# Verification step
filtered_products_info = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "searchResultsInfo"))
)

# Check if the products are filtered (this is a placeholder for actual verification logic)
if "filtered" not in filtered_products_info.text:
    driver.save_screenshot("screenshot.png")
    raise AssertionError("Products are not filtered by the selected category.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Select a category from the dropdown
category_filter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "categoryFilter"))
)
category_filter.click()

# Assuming we select a category (for example, the first option)
category_filter.find_element(By.XPATH, "//option[1]").click()

# Verify that the products displayed belong to the selected category
# This part assumes that there is a way to check the displayed products
# For example, we can check the text of the products in the productsList
products_list = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "productsList"))
)

# Here we would need to implement the logic to verify the products
# For demonstration, let's assume we check if the products list is not empty
if not products_list.text.strip():
    driver.save_screenshot('screenshot.png')
    raise AssertionError("Expected result: Products are filtered by the selected category, but no products are displayed.")