driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Click on the 'Back to Shop' button
back_to_shop_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "backToShopBtn"))
)
back_to_shop_button.click()

# Verification step
shop_page = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "shopPage"))
)
if not shop_page.is_displayed():
    driver.save_screenshot('screenshot.png')
    raise AssertionError("User is not redirected back to the shop page.")