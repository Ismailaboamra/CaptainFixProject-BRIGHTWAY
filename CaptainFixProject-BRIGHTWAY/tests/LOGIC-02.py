from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
print("Opened the login page.")

# Wait for the cart count to be visible and check if it is 0
try:
    cart_count_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartCount"))
    )
    cart_count = cart_count_element.text
    print("Current cart count:", cart_count)
    assert cart_count == "0", "Total items in the cart is not 0 after removal."
    print("Total items in the cart is 0 as expected.")
except NoSuchElementException:
    print("⚠️ Cart count element not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for cart count element.")
except AssertionError as e:
    print("⚠️ Assertion Error:", e)

# Check for alerts after the action
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

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

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
    print("Waiting for the cart total items to be visible...")
    total_items = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "totalItems"))
    )
    total_items_value = total_items.text
    print(f"Total items in the cart: {total_items_value}")
    assert total_items_value == "0", "Total items in the cart should be 0 after removal."
    print("✅ Total items in the cart is as expected: 0")
except NoSuchElementException:
    print("⚠️ Total items element not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for total items element.")
except AssertionError as e:
    print(f"⚠️ Assertion failed: {e}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("Waiting for password input field to be visible and clickable...")
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("Password input field is visible. Entering password...")
    password_input.send_keys("emilyspass")
    print("Password entered successfully.")
    
    print("Waiting for login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    print("Login button is clickable. Clicking the login button...")
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

    print("Waiting for cart count to be visible...")
    cart_count = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartCount"))
    )
    total_items = cart_count.text
    print(f"Total items in the cart: {total_items}")
    
    assert total_items == "0", "Total items in the cart should be 0 after removal."
    print("Test passed: Total items in the cart is 0 as expected.")

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

    print("Checking total items in the cart...")
    total_items = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "totalItems")))
    print("Total items in the cart:", total_items.text)
    
except NoSuchElementException:
    print("Error: Login button not found.")
except TimeoutException:
    print("Error: Timeout while waiting for the Login button.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("🔍 Waiting for the 'Add to Cart' button to be clickable...")
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-cart')]"))
    )
    print("✅ 'Add to Cart' button is clickable. Clicking now...")
    add_to_cart_button.click()
except NoSuchElementException:
    print("❌ 'Add to Cart' button not found.")
except TimeoutException:
    print("❌ Timeout while waiting for 'Add to Cart' button to be clickable.")

try:
    print("🔍 Checking for alerts after adding to cart...")
    WebDriverWait(driver, 2).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("⚠️ Alert detected:", alert.text)
    alert.accept()
except TimeoutException:
    print("✅ No alert detected after adding to cart.")
except UnexpectedAlertPresentException:
    try:
        alert = driver.switch_to.alert
        print("⚠️ Unexpected alert:", alert.text)
        alert.dismiss()
    except:
        print("❌ No unexpected alert to dismiss.")

try:
    print("🔍 Waiting for the cart count to be visible...")
    cart_count = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartCount"))
    )
    total_items = cart_count.text
    print(f"🛒 Total items in cart after addition: {total_items}")
except NoSuchElementException:
    print("❌ Cart count element not found.")
except TimeoutException:
    print("❌ Timeout while waiting for cart count to be visible.")

try:
    print("🔍 Waiting for the 'Continue Shopping' button to be clickable...")
    continue_shopping_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "backToShopFromCart"))
    )
    print("✅ 'Continue Shopping' button is clickable. Clicking now...")
    continue_shopping_button.click()
except NoSuchElementException:
    print("❌ 'Continue Shopping' button not found.")
except TimeoutException:
    print("❌ Timeout while waiting for 'Continue Shopping' button to be clickable.")

try:
    print("🔍 Waiting for the cart count to be visible again...")
    cart_count_after_removal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "cartCount"))
    )
    total_items_after_removal = cart_count_after_removal.text
    print(f"🛒 Total items in cart after removal: {total_items_after_removal}")
except NoSuchElementException:
    print("❌ Cart count element not found after removal.")
except TimeoutException:
    print("❌ Timeout while waiting for cart count to be visible after removal.")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("Waiting for the cart button to be visible and clickable...")
    cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cartBtn")))
    print("Clicking on the cart button...")
    cart_button.click()
    
    print("Waiting for the continue shopping button to be visible and clickable...")
    continue_shopping_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "backToShopFromCart")))
    print("Clicking on the continue shopping button...")
    continue_shopping_button.click()
    
    print("Waiting for the cart items to be visible...")
    cart_items = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cartItems")))
    print("Checking if there are any items in the cart...")
    
    if cart_items.text.strip() == "":
        print("No items in the cart, proceeding to remove an item...")
        # Assuming there is a remove button for each item in the cart
        remove_buttons = driver.find_elements(By.CLASS_NAME, "remove-item-button")  # Adjust class name as necessary
        for button in remove_buttons:
            print("Clicking on the remove button for an item...")
            button.click()
            print("Waiting for alert after removing item...")
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

    print("Waiting for the total items count to be visible...")
    total_items = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "totalItems")))
    print("Total items in the cart:", total_items.text)
    
    if total_items.text == "0":
        print("Test Passed: Total items in the cart is 0 after removal.")
    else:
        print("Test Failed: Total items in the cart is not 0 after removal.")

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
    print("🔍 Waiting for the total items element to be visible...")
    total_items_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "totalItems"))
    )
    total_items = total_items_element.text
    print("🛒 Total items in the cart:", total_items)

    if total_items == "0":
        print("✅ Total items in the cart is as expected: 0")
    else:
        print("❌ Total items in the cart is not as expected. Found:", total_items)

except NoSuchElementException:
    print("❌ Error: Total items element not found.")
except TimeoutException:
    print("❌ Error: Timeout while waiting for total items element.")
except UnexpectedAlertPresentException:
    try:
        alert = driver.switch_to.alert
        print("⚠️ Unexpected alert detected:", alert.text)
        alert.dismiss()
    except:
        print("⚠️ No alert to dismiss.")