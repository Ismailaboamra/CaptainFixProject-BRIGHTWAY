from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("https://mawdoo3.com/")

try:
    WebDriverWait(driver, 10).until(EC.title_contains("موضوع، أكبر موقع عربي بالعالم"))
    print("Homepage loaded successfully with status code 200.")
except Exception as e:
    driver.save_screenshot("homepage_load_error.png")
    print("Failed to load homepage:", e)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("https://mawdoo3.com/")

try:
    WebDriverWait(driver, 10).until(EC.title_contains("موضوع، أكبر موقع عربي بالعالم"))
    print("Homepage loaded successfully.")
except Exception as e:
    driver.save_screenshot("homepage_load_failed.png")
    print("Homepage failed to load.")
    print(e)