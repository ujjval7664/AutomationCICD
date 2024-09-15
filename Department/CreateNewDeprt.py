from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open a webpage
driver.get("https://stagingleave.devexhub.com")
driver.maximize_window()

# Log in to the website
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("testmanager@gmail.com")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("Test@123")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "form_submit"))).click()

time.sleep(2) 

# Locate the "Department Section" link using the href attribute and click on it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="department.php"]'))).click()

time.sleep(2) 

# Click the Add new department button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-sm'))).click()
time.sleep(2) 

# Fill the department name
department_name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'example-text-input')))
department_name_field.send_keys('Test Department')
time.sleep(1) 

# Fill the shortform
shortform_field = driver.find_element(By.XPATH, '//div[@class="main-content"]//div[2]//input[1]')
shortform_field.send_keys('TD')
time.sleep(1) 

# Fill the code
code_field = driver.find_element(By.XPATH, '//input[@id="example-email-input"]')
code_field.send_keys('951')
time.sleep(1) 

# Click the add button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'add'))).click()

