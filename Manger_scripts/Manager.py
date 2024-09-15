from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a webpage
driver.get("https://stagingleave.devexhub.com")
driver.maximize_window()

# Log in to the website
username_field = driver.find_element(By.ID, "username")  
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "form_submit")  

username_field.send_keys("testmanager@gmail.com")  
password_field.send_keys("Test@123")  

# Click the login button
login_button.click()

