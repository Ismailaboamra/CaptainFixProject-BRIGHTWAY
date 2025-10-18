from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

# Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D9%8A%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")
print("Opened the login page.")

# Wait for the username input to be visible and clickable
try:
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    print("Username input is visible.")
    
    # Attempt to submit the form without entering any credentials
    username_input.send_keys(Keys.RETURN)
    print("Submitted the login form without entering credentials.")
    
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
    except (NoSuchElementException, TimeoutException) as e:
        print("Error message not displayed:", str(e))

except (NoSuchElementException, TimeoutException) as e:
    print("Username input not found:", str(e))

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
    
    print("Waiting for the password input field to be visible and clickable...")
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    print("Password input field is visible. Leaving it empty for this test.")
    
    print("Waiting for the login button to be visible and clickable...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    print("Login button is visible. Clicking the login button.")
    login_button.click()
    
    print("Checking for alerts after clicking the login button...")
    try:
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("⚠️ Alert detected:", alert.text)
        alert.accept()
    except TimeoutException:
        print("No alert detected.")
    except UnexpectedAlertPresentException:
        try:
            alert = driver.switch_to.alert
            print("⚠️ Unexpected alert:", alert.text)
            alert.dismiss()
        except:
            print("No unexpected alert to dismiss.")
    
    print("Waiting for the error message for empty search term to be visible...")
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    if error_message.is_displayed():
        print("Error message displayed:", error_message.text)
    else:
        print("Error message not displayed.")

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
    
    print("🔍 Waiting for the login form to be submitted...")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    print("✅ Login button is clickable. Clicking the login button...")
    login_button.click()
    
    print("🔍 Checking for alerts after login...")
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

    print("🔍 Waiting for the error message to be visible...")
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "usernameError"))
    )
    if error_message.is_displayed():
        print("✅ Error message displayed for empty search term:", error_message.text)
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

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    print("Waiting for the Login button to be clickable...")
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
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
        print("Error message displayed for empty username input:", error_message.text)
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
    print("Waiting for the Search button to be clickable...")
    search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "searchBtn")))
    print("Clicking the Search button without entering a search term...")
    search_button.click()
except NoSuchElementException:
    print("⚠️ Search button not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for the Search button to be clickable.")

try:
    print("Checking for alerts after clicking the Search button...")
    WebDriverWait(driver, 2).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("⚠️ Alert detected:", alert.text)
    alert.accept()
except TimeoutException:
    print("No alert detected.")
except UnexpectedAlertPresentException:
    try:
        alert = driver.switch_to.alert
        print("⚠️ Unexpected alert:", alert.text)
        alert.dismiss()
    except:
        print("⚠️ No unexpected alert to dismiss.")

try:
    print("Waiting for the error message to be visible...")
    error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "searchResultsInfo")))
    if error_message.text:
        print("✅ Error message displayed:", error_message.text)
    else:
        print("⚠️ No error message displayed.")
except NoSuchElementException:
    print("⚠️ Error message element not found.")
except TimeoutException:
    print("⚠️ Timeout while waiting for the error message to be visible.")