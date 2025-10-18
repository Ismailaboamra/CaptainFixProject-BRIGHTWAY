driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the login form to be visible and log in (assuming login is required)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginForm")))

# Assuming the login process is done here (not shown in the step)
# After login, navigate to the shop page
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "shopPage")))

# Verify that the product in the cart is visible
cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cartCount")))
actual_cart_count = cart_count.text

# Expected result
expected_cart_count = "0"  # Assuming the initial state is 0

if actual_cart_count != expected_cart_count:
    driver.save_screenshot('screenshot.png')
    raise AssertionError(f"Expected cart count: {expected_cart_count}, but got: {actual_cart_count}")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

# Assuming there is a product to add, we will simulate adding a product to the cart.
# This part of the code would typically involve clicking on a product and adding it to the cart.
# Since the HTML does not provide specific product elements, we will assume a generic action.

# Example action to add a product to the cart (this would need to be replaced with actual product interaction)
# For demonstration, we will simulate clicking a button that would add a product to the cart.
# This is a placeholder as the actual product elements are not defined in the provided HTML.

# Wait for the product button to be clickable (assuming a button exists)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-cart"))).click()

# Verification step: Check if the cart count has increased
cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cartCount"))).text

# Assuming we expect the cart count to be 1 after adding a product
expected_cart_count = "1"
if cart_count != expected_cart_count:
    driver.save_screenshot("cart_verification_failed.png")
    raise AssertionError(f"Expected cart count: {expected_cart_count}, but got: {cart_count}")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Click on the cart button to navigate to the cart page
cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "cartBtn"))
)
cart_button.click()

# Verify that the user sees the product in the cart
cart_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "cartItems"))
)

if cart_items.text == "":
    driver.save_screenshot("cart_empty_screenshot.png")
    raise AssertionError("Expected to see products in the cart, but the cart is empty.")