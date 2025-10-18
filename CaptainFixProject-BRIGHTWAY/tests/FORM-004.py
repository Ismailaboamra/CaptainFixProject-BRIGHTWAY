driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
WebDriverWait(driver, 10).until(lambda d: d.find_element("id", "loginPage"))
assert driver.find_element("id", "loginPage").is_displayed(), "Login page is not displayed"

# Simulate login action to redirect to shop page
username_input = WebDriverWait(driver, 10).until(lambda d: d.find_element("id", "username"))
password_input = WebDriverWait(driver, 10).until(lambda d: d.find_element("id", "password"))
login_button = WebDriverWait(driver, 10).until(lambda d: d.find_element("css selector", ".btn.btn-primary"))

username_input.send_keys("testuser")
password_input.send_keys("testpassword")
login_button.click()

# Verify redirection to shop page
WebDriverWait(driver, 10).until(lambda d: d.find_element("id", "shopPage"))
if not driver.find_element("id", "shopPage").is_displayed():
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("User is not redirected to the shop page")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Enter valid username 'emilys'
username_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))
)
username_input.send_keys("emilys")

# Submit the form
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
)
login_button.click()

# Verification step
try:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "shopPage"))
    )
except:
    driver.save_screenshot("screenshot.png")
    raise AssertionError("User is not redirected to the shop page.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Enter valid password
password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "password"))
)
password_input.send_keys("emilyspass")

# Submit the login form
login_form = driver.find_element(By.ID, "loginForm")
login_form.submit()

# Verification step
try:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "shopPage"))
    )
    actual_result = driver.current_url
    expected_result = "file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html#shopPage"
    assert actual_result == expected_result, f"Expected URL: {expected_result}, but got: {actual_result}"
except AssertionError:
    driver.save_screenshot("screenshot.png")
    raise

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Click on the 'Login' button
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
)
login_button.click()

# Verification step
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "shopPage"))
)

# Check if the user is redirected to the shop page
if not driver.find_element(By.ID, "shopPage").is_displayed():
    driver.save_screenshot('screenshot.png')
    raise AssertionError("User is not redirected to the shop page.")