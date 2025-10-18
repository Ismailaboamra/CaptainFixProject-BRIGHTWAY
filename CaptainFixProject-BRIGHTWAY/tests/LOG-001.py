from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open the login page
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    # Verify that we are on the login page by checking the presence of the login form
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "loginForm")))
    print("Login page is displayed.")
except Exception as e:
    driver.save_screenshot("login_page_error.png")
    raise AssertionError("Login page did not load as expected.") from e

# Step 2: Verify total items in the cart
try:
    total_items = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "cartCount"))).text
    expected_total_items = "0"  # Assuming no products have been added yet
    assert total_items == expected_total_items, f"Expected total items in cart: {expected_total_items}, but got: {total_items}"
    print("Total items in the cart reflect the added product correctly.")
except AssertionError as e:
    driver.save_screenshot("cart_count_error.png")
    raise AssertionError("Total items in the cart do not match expected value.") from e
except Exception as e:
    driver.save_screenshot("cart_count_error.png")
    raise AssertionError("Failed to retrieve total items in the cart.") from e

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the login page and enter the username
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

try:
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("emilys")
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to enter username: " + str(e))

# Step 2: Verify that the total items in the cart reflect the added product
try:
    total_items = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "totalItems"))).text
    assert total_items == "1", f"Expected total items to be '1', but got '{total_items}'"
except AssertionError as e:
    driver.save_screenshot("error_screenshot.png")
    raise e
except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError("Failed to verify total items in the cart: " + str(e))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Enter password
try:
    password_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.send_keys("emilyspass")
    
    # Verification: Check if the total items in the cart reflect the added product
    total_items = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "totalItems"))
    ).text
    
    # Assuming the expected total items after adding a product is 1
    expected_total_items = "1"  # Change this value based on the actual expected result
    assert total_items == expected_total_items, f"Expected total items to be {expected_total_items}, but got {total_items}"

except Exception as e:
    driver.save_screenshot("error_screenshot.png")
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Click the Login button
try:
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    login_button.click()
    
    # Verification: Check if total items in the cart reflect the added product
    total_items = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "totalItems"))
    ).text
    
    # Assuming the expected number of items is 1 for this example
    expected_items = "1"  # Change this value based on your test case
    assert total_items == expected_items, f"Expected total items in cart to be {expected_items}, but got {total_items}"

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError(f"An error occurred: {str(e)}")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Add a product to the cart
try:
    # Assuming there is a way to add a product, for example, clicking a button
    add_product_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))  # Adjust selector as needed
    )
    add_product_button.click()
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to click the add product button: " + str(e))

# Step 3: Verify the total items in the cart
try:
    total_items = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "cartCount"))
    ).text
    assert total_items == "1", f"Expected total items in cart to be '1', but got '{total_items}'"
except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise AssertionError("Failed to verify total items in cart: " + str(e))

# Step 4: Check for any errors on the page
try:
    # Check for JavaScript alerts
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()  # Accept the alert after verification
except Exception as e:
    # No alert present, continue checking for other errors
    pass

# Check for inline form errors
try:
    error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
    for error in error_messages:
        if error.is_displayed():
            driver.save_screenshot('error_screenshot.png')
            raise AssertionError(f"Inline error detected: {error.text}")
except Exception as e:
    pass

# Check for toast/banner notifications
try:
    toast_notifications = driver.find_elements(By.CSS_SELECTOR, ".toast")  # Adjust selector as needed
    for toast in toast_notifications:
        if toast.is_displayed():
            driver.save_screenshot('error_screenshot.png')
            raise AssertionError(f"Toast notification detected: {toast.text}")
except Exception as e:
    pass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Navigate to the page (only if this is the first step)
driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Step 2: Check the total items in the cart
try:
    total_items_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "totalItems"))
    )
    actual_total_items = total_items_element.text
    expected_total_items = "1"  # Replace with the expected value based on the test context

    assert actual_total_items == expected_total_items, f"Expected total items to be {expected_total_items}, but got {actual_total_items}"

except AssertionError as e:
    driver.save_screenshot('error_screenshot.png')
    raise e

# Step 3: Error detection (JavaScript alerts, modals, inline errors, notifications)
try:
    error_message = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
    ).text
    if error_message:
        raise AssertionError(f"Inline error detected: {error_message}")

    # Check for any alerts
    alert = WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert_text = alert.text
    expected_alert_text = ""  # Define expected alert text if any
    assert alert_text == expected_alert_text, f"Expected alert text to be '{expected_alert_text}', but got '{alert_text}'"
    alert.accept()

except Exception as e:
    driver.save_screenshot('error_screenshot.png')
    raise e