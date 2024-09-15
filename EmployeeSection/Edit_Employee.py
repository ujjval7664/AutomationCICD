from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# import credentials
# from login_page import LoginPage 

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open a webpage
driver.get("https://stagingleave.devexhub.com")
driver.maximize_window()

# Log in to the website
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "form_submit")
username_field.send_keys("testmanager@gmail.com")
password_field.send_keys("Test@123")
time.sleep(1) 

# Click the login button
login_button.click()
time.sleep(1) 

# Wait until the menu element is clickable
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="menu"]/li[3]/a'))
)

# Click on the menu element
element.click()
time.sleep(1) 

# Click on the + add button to edit the details of the employee

Add_button = driver.find_element(By.CLASS_NAME, "sorting_1")
Add_button.click()
time.sleep(1) 

# Click on the pencil edit button 

Click_PencilEdit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='dtr-data']//i[@class='fa fa-edit']"))
)
Click_PencilEdit.click()
time.sleep(1) 

# Edit the details 

First_name = driver.find_element(By.CLASS_NAME,"example-text-input")
First_name[1].send_keys("123")

last_Name = driver.find_element(By.XPATH, "//div[@class='card-body']//div[1]//input[1]")
last_Name.send_keys("Sir")

Address = driver.find_element(By.XPATH, "//input[@name='address']")
Address.clear()
Address.send_keys("Haryana")











