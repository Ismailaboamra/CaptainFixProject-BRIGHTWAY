from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
print("Opened the login page.")

# Wait for the username input to be visible and clickable
try:
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    print("Username input is visible.")
    
    # Clear the username input and submit the form
    username_input.clear()
    print("Cleared the username input.")
    
    # Submit the form
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
            EC.visibility_of_element_located((By.ID, "usernameError"))
        )
        print("Error message displayed for empty username:", error_message.text)
    except TimeoutException:
        print("Error message not displayed within the expected time.")

except NoSuchElementException:
    print("Username input element not found.")
except TimeoutException:
    print("Username input element not visible within the expected time.")

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
    print("Username input field is visible. Sending empty input...")
    username_input.clear()  # Ensure it's empty
    username_input.send_keys("")  # Leave it empty

    print("Waiting for the password input field to be visible and clickable...")
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("Password input field is visible. Sending input...")
    password_input.send_keys("somepassword")  # Enter a dummy password

    print("Waiting for the login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    print("Login button is visible. Clicking the login button...")
    login_button.click()

    print("Checking for alerts after clicking the login button...")
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

    print("Waiting for the error message for empty username to be visible...")
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    print("Error message is visible. Verifying the text...")
    assert error_message.is_displayed(), "Error message is not displayed."
    print("Test ID: FORM-02 - Error message displayed for empty username as expected.")

except NoSuchElementException as e:
    print("Element not found:", e)
except TimeoutException as e:
    print("Timeout while waiting for an element:", e)

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
    password_input.send_keys("emilyspass")
    
    print("🔍 Waiting for the login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    print("✅ Login button is clickable. Clicking the button...")
    login_button.click()
    
    try:
        print("🔍 Checking for alerts after clicking the login button...")
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("⚠️ Alert detected:", alert.text)
        alert.accept()
    except TimeoutException:
        print("✅ No alert detected.")
    except UnexpectedAlertPresentException:
        try:
            alert = driver.switch_to.alert
            print("⚠️ Unexpected alert:", alert.text)
            alert.dismiss()
        except:
            print("✅ No unexpected alert detected.")
    
    print("🔍 Waiting for the error message for empty username to be visible...")
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    if error_message.is_displayed():
        print("✅ Error message displayed for empty username:", error_message.text)
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
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    print("Clicking the Login button...")
    login_button.click()
    
    try:
        print("Waiting for the username error message to be visible...")
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "usernameError")))
        print("Error message displayed:", error_message.text)
    except TimeoutException:
        print("Error message not displayed within the timeout period.")
    
except NoSuchElementException:
    print("Login button not found.")
except TimeoutException:
    print("Login button not clickable within the timeout period.")
except UnexpectedAlertPresentException:
    try:
        alert = driver.switch_to.alert
        print("⚠️ Unexpected alert:", alert.text)
        alert.dismiss()
    except:
        print("No unexpected alert found.")