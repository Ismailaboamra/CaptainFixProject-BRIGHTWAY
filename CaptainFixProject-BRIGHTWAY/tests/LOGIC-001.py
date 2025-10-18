driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Click on the cart button to open the cart page
cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "cartBtn"))
)
cart_button.click()

# Verify that the cart page is displayed and total items and total price are calculated
total_items = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "totalItems"))
).text
total_price = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "totalPrice"))
).text

# Expected values (these should be set according to the test case context)
expected_total_items = "0"  # Replace with the expected value
expected_total_price = "$0.00"  # Replace with the expected value

# Assertion to verify the total items and total price
if total_items != expected_total_items or total_price != expected_total_price:
    driver.save_screenshot('cart_verification_failure.png')
    raise AssertionError(f"Expected total items: {expected_total_items}, but got: {total_items}. "
                         f"Expected total price: {expected_total_price}, but got: {total_price}.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D9%AA%D8%A8/e-com/index.html")

# Assuming there are multiple products to add, we will simulate adding products to the cart.
# This part of the code will depend on the actual implementation of adding products, which is not provided in the HTML.
# For demonstration, let's assume we have a function to add products to the cart.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Example of adding products to the cart
def add_product_to_cart(product_index):
    # This function would interact with the product elements to add them to the cart
    # Assuming there are buttons to add products with a specific class
    add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "add-to-cart-button")
    add_to_cart_buttons[product_index].click()

# Add multiple products (for example, 3 products)
for i in range(3):
    add_product_to_cart(i)

# Wait for the cart count to update
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cartCount")))

# Verify the total items and total price
total_items = driver.find_element(By.ID, "totalItems").text
total_price = driver.find_element(By.ID, "totalPrice").text

# Assuming we know the expected values after adding 3 products
expected_total_items = "3"
expected_total_price = "$30.00"  # Example expected price

# Verification
if total_items != expected_total_items or total_price != expected_total_price:
    driver.save_screenshot('screenshot.png')
    raise AssertionError(f"Expected total items: {expected_total_items}, but got: {total_items}. "
                         f"Expected total price: {expected_total_price}, but got: {total_price}.")

driver.get("file:///C:/Users/Herba/OneDrive/%D8%B3%D8%B7%D8%AD%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%A8/e-com/index.html")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the cart summary to be visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cartPage")))

# Get the total items and total price
total_items = driver.find_element(By.ID, "totalItems").text
total_price = driver.find_element(By.ID, "totalPrice").text

# Expected values (these should be set according to the test scenario)
expected_total_items = "0"  # Replace with the expected value
expected_total_price = "$0.00"  # Replace with the expected value

# Verification
if total_items != expected_total_items or total_price != expected_total_price:
    driver.save_screenshot('screenshot.png')
    raise AssertionError(f"Expected total items: {expected_total_items}, but got: {total_items}. "
                         f"Expected total price: {expected_total_price}, but got: {total_price}.")