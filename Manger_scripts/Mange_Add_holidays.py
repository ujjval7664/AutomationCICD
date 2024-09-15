from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open a webpage
driver.get("https://stagingleave.devexhub.com")
driver.maximize_window()

# Log in to the website
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "form_submit")

username_field.send_keys("testmanager@gmail.com")
password_field.send_keys("Test@123")
time.sleep(1)  # Adjust sleep as necessary, though it's better to use WebDriverWait

# Click the login button
login_button.click()

# Wait for the page to load after logging in
time.sleep(1)  # Adjust sleep as necessary, though it's better to use WebDriverWait

# Click on the Manage Holidays button
link_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, 'Manage Holidays'))
)
link_element.click()

# Click on the Add New Holiday button
add_new_holiday = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'btn-sm'))
)
add_new_holiday.click()

# Send the date keys

wait = WebDriverWait(driver, 10)
date_input = wait.until(EC.presence_of_element_located((By.ID, "example-date-input")))

date_of_birth = "29-07-2024"
day, month, year = date_of_birth.split('-')
formatted_date = f"{year}-{month}-{day}"

driver.execute_script(f"document.getElementById('example-date-input').value = '{formatted_date}';")

# Add the name of the holiday 
Name = driver.find_element(By.ID,'example-text-input')
Name.send_keys('Test Holiday')

# Click the ADD button 

Add_Button = driver.find_element(By.ID,'add')
Add_Button.click()

