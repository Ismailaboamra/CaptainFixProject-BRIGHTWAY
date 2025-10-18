from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
print("Opened the login page.")

# Wait for the login form to be visible
try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginForm")))
    print("Login form is visible.")
except (NoSuchElementException, TimeoutException) as e:
    print("Error: Login form not found or not visible.", e)

# Check for alerts after opening the login page
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

# Verify redirection to the shop page
try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "shopPage")))
    print("User is redirected back to the shop page.")
except (NoSuchElementException, TimeoutException) as e:
    print("Error: User is not redirected to the shop page.", e)

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
    print("Username input field is visible. Entering username...")
    username_input.send_keys("emilys")
    print("Username entered: emilys")
except NoSuchElementException:
    print("⚠️ Username input field not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for username input field.")

try:
    print("Waiting for the login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    print("Login button is clickable. Clicking the button...")
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
    print("Waiting for the shop page to be visible...")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "shopPage"))
    )
    print("User is redirected back to the shop page successfully.")
except TimeoutException:
    print("⚠️ Timeout while waiting for shop page to be visible.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

# Navigate to the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step: Enter password: emilyspass
try:
    print("🔍 Waiting for the password input field to be visible and clickable...")
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("✅ Password input field is visible. Entering password...")
    password_input.send_keys("emilyspass")
    
    print("🔍 Waiting for the login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    print("✅ Login button is clickable. Clicking the button...")
    login_button.click()

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

    # Verify redirection to the shop page
    print("🔍 Waiting for the shop page to be visible...")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "shopPage"))
    )
    print("✅ User is redirected back to the shop page.")

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
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
    print("Login button is clickable. Clicking the Login button...")
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

    print("Waiting for the shop page to be visible...")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "shopPage")))
    print("User is redirected back to the shop page successfully.")

except NoSuchElementException:
    print("⚠️ Login button not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for the Login button to be clickable.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("🔍 Waiting for the Cart button to be clickable...")
    cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cartBtn")))
    print("🖱️ Clicking the Cart button...")
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

    print("🔄 Checking if redirected back to the shop page...")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "shopPage")))
    print("✅ Successfully redirected back to the shop page.")

except NoSuchElementException:
    print("❌ Cart button not found.")
except TimeoutException:
    print("❌ Timeout while waiting for the Cart button.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

print("Attempting to click the 'Continue Shopping' button.")
try:
    continue_shopping_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "backToShopFromCart"))
    )
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "backToShopFromCart"))
    ).click()
    print("Clicked the 'Continue Shopping' button.")
except NoSuchElementException:
    print("⚠️ 'Continue Shopping' button not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for 'Continue Shopping' button to be clickable.")

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

print("Verifying redirection to the shop page.")
try:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "shopPage"))
    )
    print("Successfully redirected to the shop page.")
except TimeoutException:
    print("⚠️ Failed to redirect to the shop page.")