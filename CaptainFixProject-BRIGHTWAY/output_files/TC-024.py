Here is the Python Selenium code that implements the specified QA step:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

# Initialize the driver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the website
    driver.get("https://mawdoo3.com/")
    
    # Step 2: Locate the search input field and enter the keyword "health"
    search_input = driver.find_element(By.XPATH, "//input[@type='search']")
    search_input.send_keys("health")
    
    # Step 3: Locate the search button and click it
    search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    search_button.click()
    
    # Step 4: Wait for the results to load (up to 3 seconds)
    time.sleep(3)  # This is a simple wait; consider using WebDriverWait for better practice
    
    # Step 5: Verify that the search results page displays relevant articles
    articles = driver.find_elements(By.CSS_SELECTOR, ".featured-article")
    assert len(articles) > 0, "No articles found for the keyword 'health'."
    
except Exception as e:
    # Capture screenshot on failure
    driver.save_screenshot("screenshot_failure.png")
    print(f"An error occurred: {e}")

# Note: Do not call driver.quit() as per the instructions.
```

### Explanation:
1. **Initialization**: The `webdriver.Chrome()` initializes the Chrome browser.
2. **Navigation**: The `driver.get()` method navigates to the specified URL.
3. **Search Input**: The search input field is located using an XPath selector, and the keyword "health" is entered.
4. **Search Button**: The search button is located and clicked to submit the search.
5. **Wait for Results**: A simple sleep is used to wait for the results to load. In a real-world scenario, you might want to use `WebDriverWait` for a more robust solution.
6. **Verification**: The code checks if any articles are displayed on the results page. If no articles are found, an assertion error is raised.
7. **Error Handling**: If any exception occurs, a screenshot is taken, and the error message is printed.

### Note:
- Ensure that you have the necessary WebDriver installed and configured for your browser.
- Adjust the selectors as needed based on the actual HTML structure of the page.