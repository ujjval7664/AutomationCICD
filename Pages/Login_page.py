# login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import credentials 

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, role):
        creds = credentials.CREDENTIALS[role]
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "form_submit")

        username_field.send_keys(creds["username"])
        password_field.send_keys(creds["password"])
        login_button.click()

    def click_login_button(self):
        login_button = self.driver.find_element(By.ID, "form_submit")       
        login_button.click()
