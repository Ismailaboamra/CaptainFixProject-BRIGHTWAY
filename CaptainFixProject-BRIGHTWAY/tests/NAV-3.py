driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Click on the 'Continue Shopping' button
continue_shopping_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "backToShopFromCart"))
)
continue_shopping_button.click()

# Verification step
try:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "shopPage"))
    )
    actual_page_state = driver.find_element(By.ID, "shopPage").is_displayed()
    expected_result = True
    assert actual_page_state == expected_result, "User is not redirected back to the shop page."
except AssertionError:
    driver.save_screenshot('screenshot.png')
    raise