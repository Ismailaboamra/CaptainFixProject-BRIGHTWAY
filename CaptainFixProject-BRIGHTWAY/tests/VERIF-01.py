from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
print("Opened the login page.")

# Wait for the username field to be visible and clickable
try:
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    print("Username field is visible.")
    
    # Wait for the password field to be visible and clickable
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("Password field is visible.")
    
    # Wait for the login button to be visible and clickable
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    print("Login button is clickable.")
    
    # Enter username and password
    username_field.send_keys("testuser")
    print("Entered username.")
    password_field.send_keys("testpassword")
    print("Entered password.")
    
    # Click the login button
    login_button.click()
    print("Clicked the login button.")
    
    # Check for alerts after login action
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

    # Verify if the user's name is displayed in the cart page
    try:
        user_name_displayed = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "userName"))
        )
        print("User's name is displayed in the cart page:", user_name_displayed.text)
    except (NoSuchElementException, TimeoutException):
        print("User's name is not displayed in the cart page.")

except (NoSuchElementException, TimeoutException) as e:
    print("An error occurred:", str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("Waiting for username input field to be visible and clickable...")
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    print("Username input field is visible. Entering username: emilys")
    username_input.send_keys("emilys")
except (NoSuchElementException, TimeoutException) as e:
    print("Error finding username input field:", e)

try:
    print("Waiting for password input field to be visible and clickable...")
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("Password input field is visible. Entering password: password123")
    password_input.send_keys("password123")
except (NoSuchElementException, TimeoutException) as e:
    print("Error finding password input field:", e)

try:
    print("Waiting for login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    print("Login button is clickable. Clicking the login button.")
    login_button.click()
except (NoSuchElementException, TimeoutException) as e:
    print("Error finding login button:", e)

try:
    print("Checking for alerts after login...")
    WebDriverWait(driver, 2).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("⚠️ Alert detected:", alert.text)
    alert.accept()
except TimeoutException:
    print("No alert detected after login.")
except UnexpectedAlertPresentException:
    try:
        alert = driver.switch_to.alert
        print("⚠️ Unexpected alert:", alert.text)
        alert.dismiss()
    except:
        print("No unexpected alert to dismiss.")

try:
    print("Waiting for user name display in cart page...")
    user_name_display = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "userNameCart"))
    )
    print("User name display is visible. Verifying the displayed name...")
    displayed_name = user_name_display.text
    if displayed_name == "emilys":
        print("Test ID: VERIF-01 - User's name is displayed correctly in the cart page.")
    else:
        print("Test ID: VERIF-01 - User's name is NOT displayed correctly. Found:", displayed_name)
except (NoSuchElementException, TimeoutException) as e:
    print("Error finding user name display:", e)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("🔍 Waiting for password input field to be visible and clickable...")
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("✅ Password input field is visible. Entering password...")
    password_input.send_keys("emilyspass")
    
    print("🔍 Waiting for login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    print("✅ Login button is clickable. Clicking the button...")
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

    print("🔍 Waiting for user name to be displayed on the cart page...")
    user_name_displayed = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "userNameCart"))
    )
    print("✅ User's name is displayed in the cart page:", user_name_displayed.text)

except NoSuchElementException as e:
    print("❌ Element not found:", e)
except TimeoutException as e:
    print("❌ Timeout while waiting for an element:", e)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("Waiting for the Login button to be clickable...")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn btn-primary")))
    print("Login button is clickable. Clicking the Login button...")
    login_button.click()
    print("Clicked the Login button.")
except NoSuchElementException:
    print("⚠️ Login button not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for the Login button to be clickable.")

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

try:
    print("Waiting for the user's name to be displayed on the cart page...")
    user_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
    print("User's name is displayed:", user_name.text)
except NoSuchElementException:
    print("⚠️ User's name element not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for the user's name to be displayed.")

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

    print("🔍 Waiting for the user's name to be visible on the Cart page...")
    user_name_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userNameCart")))
    user_name = user_name_element.text
    print("✅ User's name displayed in the cart page:", user_name)

except NoSuchElementException:
    print("❌ Cart button not found.")
except TimeoutException:
    print("❌ Timeout while waiting for the Cart button.")
finally:
    print("Test execution completed.")