from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
print("Opened the login page.")

# Wait for the username input to be visible and clickable
try:
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    print("Username input is visible.")
except (NoSuchElementException, TimeoutException) as e:
    print("Error: Username input not found or not visible.", e)

# Wait for the password input to be visible and clickable
try:
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("Password input is visible.")
except (NoSuchElementException, TimeoutException) as e:
    print("Error: Password input not found or not visible.", e)

# Wait for the login button to be visible and clickable
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    print("Login button is clickable.")
except (NoSuchElementException, TimeoutException) as e:
    print("Error: Login button not found or not clickable.", e)

# Attempt to submit invalid credentials
try:
    username_input.send_keys("invalid_user")
    print("Entered invalid username.")
    password_input.send_keys("invalid_pass")
    print("Entered invalid password.")
    login_button.click()
    print("Clicked the login button.")
except Exception as e:
    print("Error during login attempt.", e)

# Check for alerts after the login attempt
try:
    WebDriverWait(driver, 2).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("⚠️ Alert detected:", alert.text)
    alert.accept()
except TimeoutException:
    print("No alert detected after login attempt.")
except UnexpectedAlertPresentException:
    try:
        alert = driver.switch_to.alert
        print("⚠️ Unexpected alert:", alert.text)
        alert.dismiss()
    except Exception as e:
        print("Error handling unexpected alert.", e)

# Check for error message for invalid credentials
try:
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    if error_message.is_displayed():
        print("Error message displayed for invalid credentials:", error_message.text)
except (NoSuchElementException, TimeoutException) as e:
    print("Error: Error message not found or not displayed.", e)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("Waiting for the username input field to be visible and clickable...")
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    print("Username input field is visible. Entering username: emilys")
    username_input.send_keys("emilys")
except NoSuchElementException:
    print("⚠️ Username input field not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for username input field.")

try:
    print("Waiting for the password input field to be visible and clickable...")
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("Password input field is visible. Entering password: wrongpassword")
    password_input.send_keys("wrongpassword")
except NoSuchElementException:
    print("⚠️ Password input field not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for password input field.")

try:
    print("Waiting for the login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    print("Login button is clickable. Clicking the login button.")
    login_button.click()
except NoSuchElementException:
    print("⚠️ Login button not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for login button.")

try:
    print("Checking for alerts after login attempt...")
    WebDriverWait(driver, 2).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("⚠️ Alert detected:", alert.text)
    alert.accept()
except TimeoutException:
    print("No alert detected after login attempt.")
except UnexpectedAlertPresentException:
    try:
        alert = driver.switch_to.alert
        print("⚠️ Unexpected alert:", alert.text)
        alert.dismiss()
    except:
        print("⚠️ No unexpected alert found.")

try:
    print("Waiting for the error message to be visible...")
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    if error_message.is_displayed():
        print("✅ Error message displayed for invalid credentials:", error_message.text)
except NoSuchElementException:
    print("⚠️ Error message element not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for error message.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("🔍 Waiting for the password input field to be visible and clickable...")
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("✅ Password input field is visible. Entering password...")
    password_input.send_keys("wrongpassword")
    
    print("🔍 Waiting for the login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    print("✅ Login button is clickable. Clicking the button...")
    login_button.click()
    
    print("🔍 Checking for alerts after login attempt...")
    try:
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("⚠️ Alert detected:", alert.text)
        alert.accept()
    except TimeoutException:
        pass
    except UnexpectedAlertPresentException:
        try:
            alert = driver.switch_to.alert
            print("⚠️ Unexpected alert:", alert.text)
            alert.dismiss()
        except:
            pass

    print("🔍 Waiting for the error message to be visible...")
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    if error_message.is_displayed():
        print("✅ Error message displayed for invalid credentials:", error_message.text)
    else:
        print("❌ Error message not displayed.")

except NoSuchElementException as e:
    print("❌ Element not found:", e)
except TimeoutException as e:
    print("❌ Timeout while waiting for an element:", e)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("Waiting for the Login button to be clickable...")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    print("Login button is clickable. Clicking the Login button...")
    login_button.click()
    
    try:
        print("Checking for error message after clicking Login button...")
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "usernameError")))
        if error_message.is_displayed():
            print("Error message displayed:", error_message.text)
    except TimeoutException:
        print("No error message displayed after clicking Login button.")
    
except NoSuchElementException:
    print("Login button not found.")
except TimeoutException:
    print("Login button not clickable within the timeout period.")
    
try:
    WebDriverWait(driver, 2).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("⚠️ Alert detected:", alert.text)
    alert.accept()
except TimeoutException:
    pass
except UnexpectedAlertPresentException:
    try:
        alert = driver.switch_to.alert
        print("⚠️ Unexpected alert:", alert.text)
        alert.dismiss()
    except:
        pass