driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
WebDriverWait(driver, 10).until(lambda d: d.find_element("id", "loginForm"))
driver.find_element("id", "username").send_keys("testuser")
driver.find_element("id", "password").send_keys("testpassword")
driver.find_element("css selector", ".btn.btn-primary").click()
WebDriverWait(driver, 10).until(lambda d: d.find_element("id", "shopPage"))
WebDriverWait(driver, 10).until(lambda d: d.find_element("id", "productsList"))
actual_result = driver.find_element("id", "productsList").text
expected_result = "Search results are displayed in the products list."
if actual_result != expected_result:
    driver.save_screenshot("screenshot.png")
    raise AssertionError(f"Expected: {expected_result}, but got: {actual_result}")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

search_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "searchInput"))
)
search_input.send_keys("example search term")

search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "searchBtn"))
)
search_button.click()

# Verification step
search_results = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "productsList"))
)

if search_results.text == "":
    driver.save_screenshot("search_results_empty.png")
    raise AssertionError("Expected search results to be displayed, but none were found.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Click on the 'Search' button
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "searchBtn"))
)
search_button.click()

# Verification step
search_results = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "productsList"))
)
if not search_results.is_displayed():
    driver.save_screenshot('search_results_not_displayed.png')
    raise AssertionError("Search results are not displayed in the products list.")