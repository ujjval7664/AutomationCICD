from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
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
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "form_submit")

username_field.send_keys("testmanager@gmail.com")
password_field.send_keys("Test@123")
time.sleep(1) 

# Click the login button
login_button.click()
time.sleep(1) 

# Wait for the page to load and scroll down
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "btn-secondary"))
)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1) 

# Wait until the button is clickable
view_detail_buttons = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn-secondary"))
)

# Click the button
view_detail_buttons.click()
time.sleep(1) 

# Click set action 

# Wait until the button is clickable
Set_Action_buttons = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn-success"))
)
# Click the button
Set_Action_buttons.click()
time.sleep(1) 


dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "custom-select"))
)
dropdown.click()
time.sleep(1) 

# Select the "Approve" option by visible text
# After clicking the dropdown, the options should be visible, so you can select by text
approve_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//option[text()='Approve']"))
)
approve_option.click()
time.sleep(1) 

# Write description for the leave - 

Description_box = driver.find_element(By.ID, "textarea1").send_keys("Your leave is approved from my side ")
time.sleep(1) 

# Click Apply

Apply_button = driver.find_element(By.XPATH, "//button[@type='submit']").click()

alert_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible"))
)
time.sleep(1) 

# Check if the text is present

alert_text = alert_element.text

expected_text = "Info: Leave updated Successfully"
if expected_text in alert_text:
    print(f"The text '{expected_text}' is present on the website.")
else:
    print(f"The text '{expected_text}' is not present on the website.")

