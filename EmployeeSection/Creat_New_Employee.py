import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture

def browser():
    # Setup Chrome options
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_employee(browser):
    # Open a webpage
    browser.get("https://stagingleave.devexhub.com")

    # Log in to the website
    username_field = browser.find_element(By.ID, "username")
    password_field = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.ID, "form_submit")

    username_field.send_keys("testmanager@gmail.com")
    password_field.send_keys("Test@123")

    # Click the login button
    login_button.click()
    time.sleep(1)

    # Wait until the menu element is clickable
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menu"]/li[3]/a'))
    )

    # Click on the menu element
    element.click()
    time.sleep(2)

    # Wait until the add new employee button is clickable
    element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'add-emp'))
    )

    # Click on the add new employee button
    element.click()
    time.sleep(2)

    # Fill the details of the employee
    browser.find_element(By.ID, "empid").send_keys('95')
    browser.find_element(By.ID, "firstName").send_keys('Test User')
    browser.find_element(By.ID, "lastName").send_keys('User')
    browser.find_element(By.ID, "email").send_keys('Testuser561@gmail.com')
    time.sleep(2)

    # Dropdown for department
    dropdown = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "department"))
    )
    select = Select(dropdown)
    select.select_by_visible_text("PHP")

    # Dropdown for gender
    dropdown = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "gender"))
    )
    select = Select(dropdown)
    select.select_by_visible_text("Male")

    # Date of birth field
    wait = WebDriverWait(browser, 10)
    date_input = wait.until(EC.presence_of_element_located((By.ID, "birthdate")))

    date_of_birth = "19-01-2001"
    day, month, year = date_of_birth.split('-')
    formatted_date = f"{year}-{month}-{day}"
    browser.execute_script(f"document.getElementById('birthdate').value = '{formatted_date}';")

    # Contact number
    browser.find_element(By.ID, "mobileno").send_keys('9018852741')

    # Joining date
    date_input = wait.until(EC.presence_of_element_located((By.ID, "joindate")))

    join_date = "23-03-2023"
    day, month, year = join_date.split('-')
    formatted_date = f"{year}-{month}-{day}"
    browser.execute_script(f"document.getElementById('joindate').value = '{formatted_date}';")

    # Fill other fields
    browser.find_element(By.ID, "country").send_keys('INDIA')
    browser.find_element(By.ID, "address").send_keys('Mohali sector 108')
    browser.find_element(By.ID, "city").send_keys('Mohali')
    browser.find_element(By.ID, "password").send_keys('Test@123')
    browser.find_element(By.ID, "confirm-password").send_keys('Test@123')

    # Submit the form
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
