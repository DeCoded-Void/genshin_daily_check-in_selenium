#!/usr/bin/env python
import time, winsound, pickle, ctypes, sys, os
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

cwd = os.path.dirname(os.path.realpath(__file__))
options = FirefoxOptions()
options.headless = False
gecko_logpath = 'nul'
driver = webdriver.Firefox(options = options, executable_path = 'C:\geckodriver.exe', service_log_path = gecko_logpath)

def open_browser():
    driver.get('https://webstatic-sea.mihoyo.com'
               '/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us')

def import_cookies():
    cookies = pickle.load(open("{0}//cookies.pkl".format(cwd), "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

def get_cookies():
    pickle.dump(driver.get_cookies(), open("{0}//cookies.pkl".format(cwd), "wb"))

def reload_browser():
    driver.get('https://webstatic-sea.mihoyo.com'
               '/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us')

def check_logon():
    submit = driver.find_element_by_xpath('//*[contains(@class, "---login")]')
    submit.click()
    elements = driver.find_elements_by_xpath('//*[contains(text(), "Log out")]')
    if not elements:
        # Play sound when logon fails.
        #winsound.PlaySound("error.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
        driver.quit()
        # Show popup when logon fails.
        ctypes.windll.user32.MessageBoxW(0, "You are not logged in!", "Genshin Impact daily check-in event!", 0)
        sys.exit("You are not logged in!")

def execute_click():
    submit = driver.find_element_by_xpath('//*[contains(@class, "---active")]')
    submit.click()

def close_browser():
    driver.quit()

if __name__ == '__main__':
    open_browser()
    #import_cookies()
    time.sleep(60) #get some time to log in
    get_cookies()
    reload_browser()
    time.sleep(5)
    check_logon()
    time.sleep(5)
    try:
        execute_click()
        time.sleep(5)
    except:
        print("Already redeemed.")
    close_browser()
