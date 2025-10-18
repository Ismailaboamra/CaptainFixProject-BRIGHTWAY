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

# Verify total items in the cart
try:
    print("Checking total items in the cart...")
    total_items = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "totalItems"))
    ).text
    print("Total items in the cart:", total_items)
except (NoSuchElementException, TimeoutException) as e:
    print("Error while checking total items in the cart:", str(e))

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
    print("Checking for alerts after entering username...")
    WebDriverWait(driver, 2).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("⚠️ Alert detected:", alert.text)
    alert.accept()
except TimeoutException:
    print("No alert detected after entering username.")
except UnexpectedAlertPresentException:
    try:
        alert = driver.switch_to.alert
        print("⚠️ Unexpected alert:", alert.text)
        alert.dismiss()
    except:
        print("⚠️ No unexpected alert to dismiss.")

try:
    print("Waiting for the cart items count to be visible...")
    cart_count = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartCount"))
    )
    print("Cart items count is visible. Current count:", cart_count.text)
except NoSuchElementException:
    print("⚠️ Cart items count not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for cart items count.")

# Assuming that products have been added to the cart in previous steps, we would check the total items.
# This part of the code would typically follow after adding products to the cart.
try:
    print("Verifying total items in the cart...")
    total_items = int(cart_count.text)
    if total_items > 0:
        print(f"Total items in the cart reflect the number of products added: {total_items}")
    else:
        print("⚠️ Total items in the cart do not reflect any products added.")
except ValueError:
    print("⚠️ Error converting cart count to integer.")

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
except NoSuchElementException:
    print("⚠️ Password input field not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for password input field.")

try:
    print("Waiting for the login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    print("Login button is clickable. Clicking the login button...")
    login_button.click()
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
    print("Waiting for the cart items to be visible...")
    cart_items = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartItems"))
    )
    print("Cart items are visible. Verifying total items...")
    total_items = driver.find_element(By.ID, "totalItems").text
    print("Total items in the cart:", total_items)
except NoSuchElementException:
    print("⚠️ Cart items not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for cart items.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("Waiting for the Login button to be clickable...")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary")))
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

    print("Verifying total items in the cart...")
    total_items = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "totalItems")))
    print("Total items in the cart:", total_items.text)

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
    print("🔍 Waiting for the product list to be visible...")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "productsList")))
    print("✅ Product list is visible.")
    
    print("🛒 Adding a product to the cart...")
    # Assuming there is a product to add, we will simulate clicking on a product (this part may need adjustment based on actual product elements)
    product = driver.find_element(By.CSS_SELECTOR, ".products-grid > div:first-child")  # Adjust selector as needed
    product.click()
    
    print("🔄 Waiting for the cart button to be clickable...")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cartBtnProduct")))
    cart_button = driver.find_element(By.ID, "cartBtnProduct")
    cart_button.click()
    
    print("🔄 Waiting for the cart count to update...")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cartCountProduct")))
    cart_count = driver.find_element(By.ID, "cartCountProduct").text
    print(f"✅ Cart count updated to: {cart_count}")
    
    # Verify the total items in the cart
    print("🔍 Verifying total items in the cart...")
    total_items = driver.find_element(By.ID, "totalItems").text
    print(f"Total items in the cart: {total_items}")
    
    if int(total_items) > 0:
        print("✅ Test LOGIC-01 passed: Items added to the cart successfully.")
    else:
        print("❌ Test LOGIC-01 failed: No items in the cart.")
    
except NoSuchElementException as e:
    print("❌ Element not found:", e)
except TimeoutException as e:
    print("⏳ Timeout while waiting for an element:", e)
except UnexpectedAlertPresentException:
    try:
        alert = driver.switch_to.alert
        print("⚠️ Unexpected alert detected:", alert.text)
        alert.dismiss()
    except Exception as e:
        print("❌ Error handling alert:", e)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("🔍 Waiting for the total items element to be visible...")
    total_items_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "totalItems"))
    )
    total_items = total_items_element.text
    print("✅ Total items in the cart:", total_items)

except NoSuchElementException:
    print("❌ Total items element not found.")
except TimeoutException:
    print("❌ Timeout while waiting for total items element.")
    
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