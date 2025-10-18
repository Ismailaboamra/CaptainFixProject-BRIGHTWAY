from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
print("Opened the login page.")

# Check for alerts after opening the page
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

# Verify if the error message for empty cart is displayed
try:
    error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "usernameError")))
    if error_message.is_displayed():
        print("Error message displayed for empty cart:", error_message.text)
    else:
        print("No error message displayed for empty cart.")
except (NoSuchElementException, TimeoutException) as e:
    print("Error message not found:", str(e))

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
    print("Password input field is visible. Entering password: (hidden)")
    password_input.send_keys("password")  # Assuming a password is needed
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
    print("Waiting for the error message for empty cart to be visible...")
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    if error_message.is_displayed():
        print("Error message displayed:", error_message.text)
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
    print("Waiting for the password input field to be visible and clickable...")
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("Password input field is visible. Entering password...")
    password_input.send_keys("emilyspass")
    
    print("Waiting for the login form to be submitted...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    print("Clicking the login button...")
    login_button.click()
    
    print("Checking for alerts after login attempt...")
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

    print("Waiting for the error message to be visible...")
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    if error_message.is_displayed():
        print("Error message displayed for empty cart:", error_message.text)
    else:
        print("No error message displayed.")

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
    print("Waiting for the Login button to be clickable...")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
    print("Clicking the Login button...")
    login_button.click()
    
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

    print("Waiting for the error message to be visible...")
    error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "usernameError")))
    if error_message.is_displayed():
        print("Error message displayed for empty cart:", error_message.text)
    else:
        print("Error message not displayed.")

except NoSuchElementException:
    print("Login button not found.")
except TimeoutException:
    print("Login button was not clickable in time.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("🔍 Waiting for the Cart button to be clickable...")
    cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cartBtn")))
    print("✅ Cart button is clickable. Clicking the Cart button...")
    cart_button.click()
    
    try:
        print("🔍 Waiting for the error message to be visible...")
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cartItems")))
        if error_message.text == "":
            print("⚠️ Error message displayed for empty cart: No items in the cart.")
        else:
            print("✅ Error message displayed:", error_message.text)
    except TimeoutException:
        print("⚠️ Error message did not appear in the expected time.")
    
except (NoSuchElementException, TimeoutException) as e:
    print("⚠️ Exception occurred while trying to click the Cart button:", str(e))

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

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("Waiting for the Proceed to Checkout button to be clickable...")
    proceed_to_checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.btn-checkout"))
    )
    print("Proceed to Checkout button is clickable. Clicking the button...")
    proceed_to_checkout_button.click()
    
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

    print("Waiting for error message for empty cart to be visible...")
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message"))
    )
    print("Error message displayed:", error_message.text)

except NoSuchElementException:
    print("⚠️ Proceed to Checkout button not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for Proceed to Checkout button.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {str(e)}")