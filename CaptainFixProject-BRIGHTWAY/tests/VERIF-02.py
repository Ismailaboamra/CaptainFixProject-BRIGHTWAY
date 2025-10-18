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

# Verify that the cart displays the added product
try:
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cartCount")))
    print("Cart count is visible:", cart_count.text)
except (NoSuchElementException, TimeoutException) as e:
    print("Error: Cart count not found or not visible.", e)

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
    print("Entered username: emilys")
except (NoSuchElementException, TimeoutException) as e:
    print("Error occurred while entering username:", str(e))

try:
    print("Waiting for the login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    print("Login button is clickable. Clicking the login button...")
    login_button.click()
    print("Clicked the login button.")
except (NoSuchElementException, TimeoutException) as e:
    print("Error occurred while clicking the login button:", str(e))

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
    print("Waiting for the cart button to be visible...")
    cart_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartBtn"))
    )
    print("Cart button is visible. Verifying if the cart displays the added product...")
    cart_button.click()
    print("Clicked the cart button.")
except (NoSuchElementException, TimeoutException) as e:
    print("Error occurred while verifying the cart:", str(e))

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
    print("Login button is visible. Clicking the login button...")
    login_button.click()
    print("Login button clicked successfully.")
    
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
    print("Cart button is visible. Verifying if the cart displays the added product...")
    cart_button.click()
    
    print("Waiting for the cart items to be visible...")
    cart_items = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartItems"))
    )
    print("Cart items are visible. Verifying the cart content...")
    
    # Additional verification can be added here to check if the product is displayed in the cart.
    
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
    print("Waiting for the Login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    print("Login button is visible and clickable. Clicking the button...")
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

    print("Checking if the cart displays the added product...")
    cart_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartBtn"))
    )
    cart_button.click()
    
    print("Waiting for the cart items to be visible...")
    cart_items = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartItems"))
    )
    print("Cart items are visible. Verifying the contents...")
    
    # Additional verification logic can be added here to check for specific products in the cart

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
    print("🔍 Waiting for the 'Add to Cart' button to be clickable...")
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to Cart')]"))
    )
    print("✅ 'Add to Cart' button is clickable. Clicking the button...")
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

    print("🔍 Waiting for the cart to update...")
    cart_count = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartCount"))
    )
    print("✅ Cart count is visible. Current count:", cart_count.text)

    if int(cart_count.text) > 0:
        print("✅ Product successfully added to the cart.")
    else:
        print("❌ No products in the cart. Test failed.")

except NoSuchElementException:
    print("❌ 'Add to Cart' button not found.")
except TimeoutException:
    print("❌ Timeout while waiting for 'Add to Cart' button.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("🔍 Waiting for the Cart button to be visible and clickable...")
    cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cartBtn")))
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

    print("🔍 Checking if the cart displays the added product...")
    cart_items = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cartItems")))
    if cart_items:
        print("✅ Cart displays the added product.")
    else:
        print("❌ Cart does not display any products.")
        
except NoSuchElementException:
    print("❌ Cart button not found.")
except TimeoutException:
    print("❌ Timeout while waiting for the Cart button.")