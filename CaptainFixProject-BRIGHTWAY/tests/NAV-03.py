from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Assuming driver is already created and passed
driver.get("https://mawdoo3.com/")

try:
    # Wait for the page to load and the element to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'الأكثر رواجاً')]")))
    
    # Click on the link to navigate to the most viewed pages
    most_viewed_link = driver.find_element(By.LINK_TEXT, "الأكثر رواجاً")
    most_viewed_link.click()
    
    # Wait for the most viewed pages to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'الأكثر رواجاً')]")))
    
    # Capture a screenshot if the expected result is not found
    if not driver.find_elements(By.XPATH, "//div[contains(@class, 'category-items')]"):
        driver.save_screenshot("most_viewed_pages_not_found.png")
    
except Exception as e:
    driver.save_screenshot("error_occurred.png")
    print(f"An error occurred: {e}")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Navigate to the website
driver.get("https://mawdoo3.com/")

try:
    # Wait for the most viewed pages section to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'الأكثر رواجاً')]")))
    
    # Verify the most viewed pages are displayed
    most_viewed_section = driver.find_element(By.XPATH, "//h2[contains(text(), 'الأكثر رواجاً')]")
    assert most_viewed_section.is_displayed(), "Most viewed pages section is not displayed."
    
    # Optionally, you can check for the presence of articles in this section
    articles = driver.find_elements(By.XPATH, "//div[contains(@class, 'featured-article')]")
    assert len(articles) > 0, "No articles found in the most viewed pages section."
    
except Exception as e:
    # Capture a screenshot if an error occurs
    driver.save_screenshot("error_screenshot.png")
    print(f"An error occurred: {e}")