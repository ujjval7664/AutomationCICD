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
time.sleep(1) 

# Optionally, wait for the login to complete and the new page to load
# driver.implicitly_wait(5)

# Click on the first element with the href 'leave-section.php'
wait = WebDriverWait(driver, 10)
leave_types_link = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fa-sign-out")))
leave_types_link.click()
time.sleep(1) 

# Click on the + icon 

Click_Plus_icon = driver.find_element(By.CLASS_NAME, "sorting_1")
Click_Plus_icon[9].click()
time.sleep(1)

# Click the add new type leave
Add_NewTypeleave = driver.find_element(By.CLASS_NAME, "btn-sm")
Add_NewTypeleave.click()
time.sleep(1) 

# Enter the value in the field leave type
Leave_Type = driver.find_element(By.ID, "example-text-input")
Leave_Type.send_keys("Test Leave")
time.sleep(1) 

# Enter the value in the short description
Short_description = driver.find_element(By.XPATH, "//div[@class='main-content']//div[2]//input[1]")
Short_description.send_keys("test Leave description")
time.sleep(1) 

# Click add button
add_button = driver.find_element(By.ID, "add")
add_button.click()
time.sleep(1) 

# For checking the text - successful message 

try:
  
    alert_div = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible.fade.show")

    alert_text = alert_div.text
    print("Alert Text:", alert_text)


    expected_text = "Info: Leave type added Successfully"
    if "Leave type added Successfully" in alert_text:
        print("Success message is correct.")
    else:
        print("Success message is incorrect.")

except Exception as e:
    print("Error:", e)
