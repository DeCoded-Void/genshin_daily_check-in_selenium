import ctypes
import os
import shutil
import time
from selenium import webdriver

profile = "genshin"

# Used options to ensure that the enviornment is in-line with an actual browser instance
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")

# Check if chrome profile exists, will be used later on
newLoginFlag = False
if os.path.isdir(profile) is False:
    newLoginFlag = True
    
options.add_argument(f"--user-data-dir={os.path.dirname(os.path.realpath(__file__))}\{profile}")
driver = webdriver.Chrome(options=options)

# Open website with event.
def open_browser():
    driver.get('https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us')

# Checking if user is logged in.
def check_login():
    # Search for login icon and click it (to open submenu).
    submit = driver.find_element_by_xpath('//*[contains(@class, "---login")]')
    submit.click()
    # Checking if "Log out" option is present (if not you are not logged in).
    hasLogOut = driver.find_elements_by_xpath('//*[contains(text(), "Log out")]')
    if not hasLogOut:
        driver.quit()
        ctypes.windll.user32.MessageBoxW(0, "You are not logged in!", "Genshin Impact daily check-in event!", 0)
        shutil.rmtree(profile, ignore_errors=True) # Deletes user profile
        open('restartflag.txt', 'w').close() # Create a blank file to act as a flag for our batch file
        quit()

# Once there is an active daily, we so a simulated click to accept it
def execute_click():
    submit = driver.find_element_by_xpath('//*[contains(@class, "---active")]')
    submit.click()

# Execution order.
if __name__ == '__main__':
    if newLoginFlag is True: # if profile doesnt exist
        open_browser()
        input('\n\n\nLogin Requried, opening browser, once logged in, come back to this window and press enter to continue')
        print(f'\n\n\nContinuing with process, if you made a mistake, delete the "{profile}" folder and restart the program')
    
    open_browser() # to reload content
    time.sleep(5)
    check_login()
    time.sleep(5)
    try:
        execute_click()
        time.sleep(5)
        print("\n\n\nSucessfully redeemed daily! \n Gonna wait for a full 24 hours, to force a recheck, press any button to do so...")
    except Exception as error:
        print("\n\n\nAlready redeemed daily, gonna wait for a full 24 hours, to force a recheck, press any button to do so...")
    driver.quit()
