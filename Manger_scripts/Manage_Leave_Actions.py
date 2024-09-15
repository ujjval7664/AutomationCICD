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
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "form_submit")
username_field.send_keys("admin@superadmin.com")
password_field.send_keys("e#l5s&5NGnQQQ")
time.sleep(1) 

# Click the login button
login_button.click()

# Take click action on manage leave a dropdown will get open 

# link_element = driver.find_element(By.CSS_SELECTOR, "a[href='javascript:void(0)']")
# link_element.click()


manage_leave_icon = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/nav[1]/ul[1]/li[6]/a[1]")
manage_leave_icon[1].click()



