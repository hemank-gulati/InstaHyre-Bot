from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome options
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30)

try:
    # Step 1: Go to the login page
    driver.get("https://www.instahyre.com/login/")

    # Find the email and password input fields
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password_input = driver.find_element(By.NAME, "password")

    # Enter the login credentials
    email_input.send_keys("your email")
    password_input.send_keys("your password")

    # Find and click the login button
    login_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-success') and @type='submit']")
    login_button.click()

    # Step 2: Apply filters after logging in
    wait.until(EC.presence_of_element_located((By.ID, 'job-functions-selectized')))

    # Select the first filter "All - Software Engineering"
    filter_input = driver.find_element(By.ID, 'job-functions-selectized')
    wait.until(EC.element_to_be_clickable(filter_input))
    filter_input.click()
    filter_input.send_keys("All - Software Engineering")
    filter_input.send_keys(Keys.ENTER)

    # Select the second filter "All - Data Science and Analysis"
    wait.until(EC.element_to_be_clickable(filter_input))
    filter_input.click()
    filter_input.send_keys("All - Data Science and Analysis")
    filter_input.send_keys(Keys.ENTER)

    experience_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'years'))
    )
    experience_input.clear()  # Clear the field in case there's a default value
    experience_input.send_keys("2")  # Set experience to 1 year

    # Step 3: Click "Show results" to apply the filters
    show_results_button = driver.find_element(By.ID, 'show-results')
    driver.execute_script("arguments[0].scrollIntoView(true);", show_results_button)
    driver.execute_script("arguments[0].click();", show_results_button)

    count = 0
    while count <= 1000:
        try:
            # Click the "View more" button if it's present
            view_more_button = wait.until(
                EC.element_to_be_clickable((By.ID, 'interested-btn'))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", view_more_button)
            driver.execute_script("arguments[0].click();", view_more_button)

            # Step 5: Click the "Apply" button repeatedly
            apply_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'new-btn'))
            )
            apply_button.click()
            count += 1
            print(f"Applied to {count} jobs.")
            time.sleep(2)
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, ElementClickInterceptedException):
            print("No more jobs left to apply.")
            break

finally:
    # Close the WebDriver
    driver.quit()