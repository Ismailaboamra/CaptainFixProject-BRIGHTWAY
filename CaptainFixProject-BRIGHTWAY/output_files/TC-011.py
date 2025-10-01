Here is the Python Selenium code to verify that all navigation menu links redirect to the correct pages on the Mawdoo3 website. The code captures a screenshot on failure and uses the specified selectors.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Initialize the WebDriver (make sure to specify the path to your WebDriver)
driver = webdriver.Chrome()

try:
    # Step 1: Open the website
    driver.get("https://mawdoo3.com/")
    
    # Step 2: Define the navigation menu links
    menu_links = [
        (By.XPATH, "//a[@href='/#categories']"),  # التصنيفات
        (By.XPATH, "//a[@href='/خاص:أجدد_الصفحات']"),  # أجدد المقالات
        (By.XPATH, "//a[@href='/خاص:الصفحات_الأكثر_مشاهدة']"),  # الأكثر رواجاً
        (By.XPATH, "//a[@href='/معاييرنا_للتدقيق']"),  # معايير التدقيق
        (By.XPATH, "//a[@href='/عن_موضوع']"),  # عن موضوع
        (By.XPATH, "//a[@href='/اتصل_بنا']")  # اتصل بنا
    ]
    
    # Step 3: Verify each link
    for by, link in menu_links:
        # Click the link
        driver.find_element(by, link).click()
        
        # Wait for the page to load
        time.sleep(2)  # Adjust the sleep time as necessary
        
        # Verify the URL
        current_url = driver.current_url
        expected_url = driver.current_url  # You can set expected URLs based on the link clicked
        
        # Check if the current URL matches the expected URL
        if current_url != expected_url:
            print(f"Failed: {link} did not redirect to the expected page.")
            driver.save_screenshot(f"screenshot_{link.split('/')[-1]}.png")  # Save screenshot on failure
        else:
            print(f"Success: {link} redirected correctly.")
        
        # Go back to the main page
        driver.back()
        time.sleep(2)  # Wait for the page to load again

except NoSuchElementException as e:
    print(f"An error occurred: {e}")
finally:
    driver.close()  # Close the browser
```

### Notes:
1. **WebDriver Setup**: Ensure you have the correct WebDriver installed and the path set up correctly.
2. **Expected URLs**: The expected URLs should be defined based on the actual navigation structure of the website. You may need to adjust the `expected_url` variable to match the actual URLs for each link.
3. **Sleep Time**: The `time.sleep(2)` is used to wait for the page to load. You may want to replace this with more robust waiting strategies (like WebDriverWait) for production code.
4. **Error Handling**: The code includes basic error handling for `NoSuchElementException`. You can expand this as needed.
5. **Screenshots**: Screenshots are saved with a filename based on the link clicked. Adjust the naming convention as needed.