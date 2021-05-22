# genshin_daily_check-in_selenium
Python code for Genshin Impact daily check-in web event. For Firefox web browser.

# Requirements
1. Python 3.8
2. selenium
3. Official Mozilla geckodriver.exe (https://github.com/mozilla/geckodriver/releases)

# Usage
Set the path to geckodriver.exe in script (default is C:\geckodriver.exe)
Now you need to get own cookie and store it locally.
Run the script. New Firefox window will appear.
You have 60 seconds to log in. To log in click on the avatar on top right on the website and put your credentials.
Wait the remaining time. Firefox will close automatically.
In the directory of the script new file **cookies.pkl** will be created. Never share this file with anyone!
Edit the part of the python script.

From:
```
    #import_cookies()
    time.sleep(60) #get some time to log in (60 seconds)
    get_cookies()
```
To:
```
    import_cookies()
    #time.sleep(60) #get some time to log in (60 seconds)
    #get_cookies()
```
Now when script is executed it will use **cookies.pkl** to log in.

# Additional option
When everything is set and you know it is working fine you can daily check-in with headless firefox (window will not appear)

Change:
```options.headless = False```
to
```options.headless = True```
