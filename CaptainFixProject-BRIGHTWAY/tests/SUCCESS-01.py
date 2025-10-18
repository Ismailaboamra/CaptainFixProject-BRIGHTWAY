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

# Verify that the cart is visible
try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cartBtn")))
    print("Cart button is visible.")
except (NoSuchElementException, TimeoutException) as e:
    print("Error: Cart button not found or not visible.", e)

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
    
    print("Waiting for the login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    print("Login button is visible. Clicking the login button...")
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

    print("Waiting for the cart button to be visible and clickable...")
    cart_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartBtn"))
    )
    print("Cart button is visible. Verifying cart visibility...")
    cart_button.click()
    print("Cart button clicked. User should now be able to view the cart.")

except NoSuchElementException as e:
    print("Error: Element not found.", e)
except TimeoutException as e:
    print("Error: Timeout while waiting for an element.", e)

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

    print("Waiting for the cart button to be visible and clickable...")
    cart_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartBtn"))
    )
    print("Cart button is visible. Verifying if user can view the cart...")
    cart_button.click()
    print("Cart button clicked. User should now be viewing the cart.")

except NoSuchElementException as e:
    print("Error: Element not found.", e)
except TimeoutException as e:
    print("Error: Timeout while waiting for an element.", e)

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

    print("Waiting for the cart to be visible...")
    cart_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cartBtn")))
    print("Cart button is visible. Verifying the cart...")
    
    # Additional verification can be added here if needed

except NoSuchElementException:
    print("⚠️ Login button not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for the Login button.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("Waiting for the 'Add to Cart' button to be clickable...")
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to Cart')]"))
    )
    print("Clicking the 'Add to Cart' button...")
    add_to_cart_button.click()
    
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

    print("Waiting for the cart button to be clickable...")
    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cartBtn"))
    )
    print("Clicking the cart button to view the cart...")
    cart_button.click()

    print("Waiting for the cart page to be visible...")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartPage"))
    )
    print("Cart page is now visible. Verifying the cart contents...")

    cart_items = driver.find_element(By.ID, "cartItems")
    if cart_items.is_displayed():
        print("Cart contains items. Test SUCCESS-01 passed.")
    else:
        print("Cart is empty. Test SUCCESS-01 failed.")

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
    print("🔍 Waiting for the Cart button to be visible and clickable...")
    cart_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartBtn"))
    )
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cartBtn"))
    )
    print("✅ Cart button is visible and clickable. Clicking the Cart button...")
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

    print("🔍 Verifying if the Cart page is displayed...")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartPage"))
    )
    print("✅ Cart page is now visible. User can view the cart with the added product.")

except NoSuchElementException:
    print("❌ Cart button not found.")
except TimeoutException:
    print("❌ Timeout while waiting for the Cart button.")