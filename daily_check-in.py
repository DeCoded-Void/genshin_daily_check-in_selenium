#!/usr/bin/env python
# time for delaying the command execution.
# windound for sound alert in case of error.
# pickle to save and load cookies.
# ctypes for error popup window.
# sys for exit text on console information.
# os to get script directory path (usefull if script is executed from another directory).

import time, winsound, pickle, ctypes, sys, os
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

# Assign script dir path to cwd.
cwd = os.path.dirname(os.path.realpath(__file__))
# Options for Firefox geckodriver.
options = FirefoxOptions()
options.headless = False
# You can change it to something else if you want to see geckodriver logs.
gecko_logpath = 'nul'
driver = webdriver.Firefox(options = options, executable_path = 'C:\geckodriver.exe', service_log_path = gecko_logpath)

# Open website with event.
def open_browser():
    driver.get('https://webstatic-sea.mihoyo.com'
               '/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us')

# Import cookies which was previously created.
def import_cookies():
    cookies = pickle.load(open("{0}//cookies.pkl".format(cwd), "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

# Cet cookie from browser (after logon) and store them as file.
def get_cookies():
    pickle.dump(driver.get_cookies(), open("{0}//cookies.pkl".format(cwd), "wb"))

# Checking if user is logged in. If not sound or/and popup will appear.
def check_logon():
    # Search for login icon and click it (to open submenu).
    submit = driver.find_element_by_xpath('//*[contains(@class, "---login")]')
    submit.click()
    # Checking if "Log out" option is present (if not you are not logged in).
    elements = driver.find_elements_by_xpath('//*[contains(text(), "Log out")]')
    if not elements:
        # Play sound when logon fails.
        #winsound.PlaySound("{0}//error.wav".format(cwd), winsound.SND_ASYNC | winsound.SND_ALIAS)
        driver.quit()
        # Show popup when logon fails.
        ctypes.windll.user32.MessageBoxW(0, "You are not logged in!", "Genshin Impact daily check-in event!", 0)
        sys.exit("You are not logged in!")

# When new "check-in" is present the class of the div contains "---active". So we are searching for it and click it.
def execute_click():
    submit = driver.find_element_by_xpath('//*[contains(@class, "---active")]')
    submit.click()

# Closing the opened browser.
def close_browser():
    driver.quit()

# Execution order.
if __name__ == '__main__':
    open_browser()
    #import_cookies()
    time.sleep(60) #get some time to log in
    get_cookies()
    open_browser() #to reload content
    time.sleep(5)
    check_logon()
    time.sleep(5)
    try:
        execute_click()
        time.sleep(5)
    except:
        print("Already redeemed.")
    close_browser()
