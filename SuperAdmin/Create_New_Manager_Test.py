from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open a webpage
driver.get("https://stagingleave.devexhub.com")
driver.maximize_window()
time.sleep(2) 

# Log in to the website
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "form_submit")
username_field.send_keys("admin@superadmin.com")
password_field.send_keys("e#l5s&5NGnQQQ")
time.sleep(2) 

# Click the login button
login_button.click()
time.sleep(2) 

# Click on the manager section 

link = driver.find_element(By.CSS_SELECTOR, 'a[href="managers.php"]')
link.click()

# Click on the Add new administrator

Add_NewTypeleave = driver.find_element(By.CLASS_NAME, "btn-sm")
Add_NewTypeleave.click()
time.sleep(2) 

# Enter details 

Username = driver.find_element(By.ID,"username")
Username.send_keys("DV00096")

Name = driver.find_element(By.ID, "firstName")
Name.send_keys("Manager test rakesh")

Email = driver.find_element(By.ID, "email")
Email.send_keys("testrakesh@gmail.com")

Password =  driver.find_element(By.ID,"password")
Password.send_keys("Test@123")

Confirm_Password  = driver.find_element(By.ID,"confirm-password")
Confirm_Password.send_keys("Test@123")
time.sleep(2) 

# Click the proceed button 

Proceed_button = driver.find_element(By.ID, "update")
Proceed_button.click()
time.sleep(2) 

# Now fill the details of Add admin section 

driver.find_element(By.ID, "empid").send_keys('681')
driver.find_element(By.ID, "firstName").send_keys('Admin')
driver.find_element(By.ID, "lastName").send_keys('testUser')
driver.find_element(By.ID, "email").send_keys('Admintestuser121@gmail.com')
time.sleep(2) 

# Dropdown for gender
dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "gender"))
)

# Click on the dropdown to ensure it's in focus
dropdown.click()

# Create a Select object and select the option by visible text
select = Select(dropdown)
select.select_by_visible_text("Male")

# Date of birth field.

wait = WebDriverWait(driver, 10)
date_input = wait.until(EC.presence_of_element_located((By.ID, "birthdate")))

date_of_birth = "19-09-2000" 
day, month, year = date_of_birth.split('-')
formatted_date = f"{year}-{month}-{day}"  

driver.execute_script(f"document.getElementById('birthdate').value = '{formatted_date}';")

# Contact number
driver.find_element(By.ID, "mobileno").send_keys('9018852741')

# Joining date

wait = WebDriverWait(driver, 10)
date_input = wait.until(EC.presence_of_element_located((By.ID, "joindate")))

date_of_birth = "23-03-2023"
day, month, year = date_of_birth.split('-')
formatted_date = f"{year}-{month}-{day}"  

driver.execute_script(f"document.getElementById('joindate').value = '{formatted_date}';")

# Add the country  text 

Country = driver.find_element(By.ID,"country")
Country.send_keys("Bharat")

# Fill the address details

Address  = driver.find_element(By.ID, "address")
Address.send_keys("Mohali")

# Fill the city details 

City  = driver.find_element(By.ID, "city")
City.send_keys("city")

# Set password 

Password =  driver.find_element(By.ID,"password")
Password.send_keys("Test@123")

Confirm_Password  = driver.find_element(By.ID,"confirm-password")
Confirm_Password.send_keys("Test@123")
time.sleep(2)

# Click the proceed button 

Proceed_button = driver.find_element(By.CLASS_NAME, "btn-primary")
Proceed_button.click()
time.sleep(2) 













