from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
print("Opened the login page.")

# Locate the password input field and leave it empty
try:
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("Password input field is visible.")
    
    # Submit the form without entering a password
    login_form = driver.find_element(By.ID, "loginForm")
    login_form.submit()
    print("Submitted the login form with empty password.")
    
except NoSuchElementException:
    print("⚠️ Error: Password input field not found.")
except TimeoutException:
    print("⚠️ Error: Timeout while waiting for password input field.")
    
# Check for alert after submission
try:
    WebDriverWait(driver, 2).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("⚠️ Alert detected:", alert.text)
    alert.accept()
except TimeoutException:
    print("No alert detected after form submission.")
except UnexpectedAlertPresentException:
    try:
        alert = driver.switch_to.alert
        print("⚠️ Unexpected alert:", alert.text)
        alert.dismiss()
    except:
        print("⚠️ No unexpected alert found.")

# Check for error message for empty password
try:
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "passwordError"))
    )
    if error_message.is_displayed():
        print("Error message displayed for empty password:", error_message.text)
    else:
        print("⚠️ Error message not displayed for empty password.")
except NoSuchElementException:
    print("⚠️ Error: Password error message element not found.")
except TimeoutException:
    print("⚠️ Error: Timeout while waiting for password error message.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("Waiting for username input field to be visible and clickable...")
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    print("Username input field is visible. Entering username: emilys")
    username_input.send_keys("emilys")
except (NoSuchElementException, TimeoutException) as e:
    print("Error: Username input field not found or not clickable.", e)

try:
    print("Waiting for password input field to be visible and clickable...")
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("Password input field is visible. Leaving it empty.")
    password_input.send_keys("")  # Intentionally leaving it empty
except (NoSuchElementException, TimeoutException) as e:
    print("Error: Password input field not found or not clickable.", e)

try:
    print("Waiting for login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    print("Login button is visible. Clicking the login button.")
    login_button.click()
except (NoSuchElementException, TimeoutException) as e:
    print("Error: Login button not found or not clickable.", e)

try:
    print("Checking for error message for empty password...")
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "passwordError"))
    )
    if error_message.is_displayed():
        print("Error message displayed for empty password:", error_message.text)
except (NoSuchElementException, TimeoutException) as e:
    print("Error: Error message not found or not displayed.", e)

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

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
print("Navigated to the login page.")

# Wait for the password input field to be visible and interactable
try:
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("Password field is visible.")
    
    # Leave the password field empty and submit the form
    print("Leaving the password field empty.")
    login_form = driver.find_element(By.ID, "loginForm")
    login_form.submit()
    print("Submitted the login form.")
    
    # Check for alerts after submission
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

    # Wait for the error message to be visible
    try:
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "passwordError"))
        )
        print("Error message displayed:", error_message.text)
    except TimeoutException:
        print("Error message not displayed within the expected time.")

except (NoSuchElementException, TimeoutException) as e:
    print("An error occurred while interacting with the password field:", str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("Waiting for the Login button to be clickable...")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    print("Clicking the Login button...")
    login_button.click()
    
    try:
        print("Checking for alert presence...")
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("⚠️ Alert detected:", alert.text)
        alert.accept()
    except TimeoutException:
        print("No alert present after clicking the Login button.")
    except UnexpectedAlertPresentException:
        try:
            alert = driver.switch_to.alert
            print("⚠️ Unexpected alert:", alert.text)
            alert.dismiss()
        except:
            print("No unexpected alert to dismiss.")
    
    print("Waiting for the error message for empty password...")
    error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "passwordError")))
    if error_message.is_displayed():
        print("Error message displayed for empty password:", error_message.text)
    else:
        print("Error message not displayed.")
        
except NoSuchElementException:
    print("Login button not found.")
except TimeoutException:
    print("Login button not clickable within the timeout period.")