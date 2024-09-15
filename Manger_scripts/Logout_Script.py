# Manager_scripts_inputs/Logout.py

import sys
import os

# Add the main directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Pages')))

from Pages.Login_page import setup_browser, open_webpage, login, click_manager, click_logout

def main():
    # Set up the browser
    driver = setup_browser()
    
    # Open the target webpage
    open_webpage(driver, "https://stagingleave.devexhub.com")
    
    # Perform login
    login(driver, "testmanager@gmail.com", "Test@123")
    
    # Click on the manager button
    click_manager(driver)
    
    # Click on the logout button
    click_logout(driver)
    
    # Optionally, close the browser after actions
    # driver.quit()

if __name__ == "__main__":
    main()



