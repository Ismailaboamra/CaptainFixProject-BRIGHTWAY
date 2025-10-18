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
    
    username_field.click()
    username_field.send_keys("testuser")
    print("Entered username.")

    # Wait for the password field to be visible and clickable
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("Password field is visible.")
    
    password_field.click()
    password_field.send_keys("testpassword")
    print("Entered password.")

    # Wait for the login button to be visible and clickable
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    print("Login button is clickable.")
    
    login_button.click()
    print("Clicked the login button.")

    # Check for alerts after clicking the login button
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

    # Verify successful login by checking if the shop page is displayed
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "shopPage"))
        )
        print("User is logged in successfully, shop page is visible.")
    except TimeoutException:
        print("User login failed, shop page is not visible.")

except (NoSuchElementException, TimeoutException) as e:
    print("An error occurred:", str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("Waiting for the username input field to be visible and clickable...")
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    print("Username input field is visible. Entering username...")
    username_input.send_keys("emilys")
    print("Username entered: emilys")
except NoSuchElementException:
    print("⚠️ Username input field not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for username input field.")

try:
    print("Waiting for the password input field to be visible and clickable...")
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("Password input field is visible. Entering password...")
    password_input.send_keys("password123")  # Assuming a password for the test
    print("Password entered.")
except NoSuchElementException:
    print("⚠️ Password input field not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for password input field.")

try:
    print("Waiting for the login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    print("Login button is visible. Clicking the login button...")
    login_button.click()
    print("Login button clicked.")
except NoSuchElementException:
    print("⚠️ Login button not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for login button.")

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
    print("Waiting for the user name display to verify login...")
    user_name_display = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "userName"))
    )
    print("User is logged in successfully. User name displayed:", user_name_display.text)
except NoSuchElementException:
    print("⚠️ User name display not found. Login may have failed.")
except TimeoutException:
    print("⚠️ Timeout while waiting for user name display.")

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
    print("Password entered successfully.")

    print("Waiting for the login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    print("Login button is clickable. Clicking the login button...")
    login_button.click()
    print("Login button clicked.")

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

except NoSuchElementException as e:
    print("Error: Element not found.", e)
except TimeoutException as e:
    print("Error: Timeout while waiting for an element.", e)

print("Test step completed.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("🔍 Waiting for the Login button to be clickable...")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
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

except NoSuchElementException:
    print("❌ Login button not found.")
except TimeoutException:
    print("❌ Timeout while waiting for the Login button.")