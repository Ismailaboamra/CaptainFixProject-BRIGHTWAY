from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Assuming driver is already created and passed in
driver.get("https://mawdoo3.com/%D8%AE%D8%A7%D8%B5:%D8%A3%D8%AC%D8%AF%D9%87_%D8%A7%D9%84%D8%B5%D9%81%D8%AD%D8%A7%D8%AA")

try:
    # Wait for the newest pages section to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'أجدد المقالات')]"))
    )
    # Optionally, you can take a screenshot if needed
    driver.save_screenshot("newest_pages_visible.png")
except Exception as e:
    print("An error occurred:", e)
    driver.save_screenshot("error_screenshot.png")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Assuming driver is already created and passed in
driver.get("https://mawdoo3.com/")

try:
    # Wait for the newest articles section to be visible
    newest_articles_section = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'أجدد المقالات')]"))
    )
    
    # Verify that the newest articles are displayed
    articles = driver.find_elements(By.XPATH, "//h2[contains(text(), 'أجدد المقالات')]/following-sibling::div//a")
    if articles:
        print("Newest pages are displayed.")
    else:
        print("Newest pages are not displayed.")
        driver.save_screenshot("newest_pages_not_displayed.png")

except Exception as e:
    print(f"An error occurred: {e}")
    driver.save_screenshot("error_occurred.png")