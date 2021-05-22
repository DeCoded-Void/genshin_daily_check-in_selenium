#!/usr/bin/env python
import time
import pickle
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver

options = FirefoxOptions()
options.headless = False
driver = webdriver.Firefox(options=options, executable_path = 'C:\geckodriver.exe')

def open_browser():
    driver.get('https://webstatic-sea.mihoyo.com'
               '/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us')

def import_cookies():
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

def get_cookies():
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

def reload_browser():
    driver.get('https://webstatic-sea.mihoyo.com'
               '/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us')

def execute_click():
    submit = driver.find_element_by_xpath('//*[contains(@class, "---active")]')
    submit.click()

def close_browser():
    driver.quit()

if __name__ == '__main__':
    open_browser()
    #import_cookies()
    time.sleep(30) #get some time to log in
    get_cookies()
    reload_browser()
    time.sleep(5)
    try:
        execute_click()
        time.sleep(5)
    except:
        print("Alreaady redemeed.")
    close_browser()
