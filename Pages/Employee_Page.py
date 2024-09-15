# Employee_Page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.username = "testmanager@gmail.com"
        self.password = "Test@123"

    def login(self):
        self.driver.find_element(By.ID, "username").send_keys(self.username)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.ID, "form_submit").click()

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))

    def click_element(self, by, value, timeout=10):
        element = self.wait_for_element(by, value, timeout)
        element.click()

    def fill_input(self, by, value, text):
        element = self.driver.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def add_employee_details(self, first_name, last_name, address):
        first_name_field = self.driver.find_elements(By.CLASS_NAME, "example-text-input")[1]
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.XPATH, "//div[@class='card-body']//div[1]//input[1]")
        last_name_field.send_keys(last_name)

        address_field = self.driver.find_element(By.XPATH, "//input[@name='address']")
        address_field.clear()
        address_field.send_keys(address)

    def navigate_to_menu(self):
        self.click_element(By.XPATH, '//*[@id="menu"]/li[3]/a')

    def click_add_button(self):
        self.click_element(By.CLASS_NAME, "sorting_1")

    def click_edit_button(self):
        self.click_element(By.XPATH, "//span[@class='dtr-data']//i[@class='fa fa-edit']")
