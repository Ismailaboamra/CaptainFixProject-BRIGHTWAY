driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Click on a product to view details
product_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#productsList .product-item"))  # Assuming product items have a class 'product-item'
)
product_element.click()

# Verification step
WebDriverWait(driver, 10).until(EC.url_contains("productPage"))
if "productPage" not in driver.current_url:
    driver.save_screenshot("screenshot.png")
    raise AssertionError("User is not redirected to the product details page.")