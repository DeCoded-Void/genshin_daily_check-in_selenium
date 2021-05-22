# genshin_daily_check-in_selenium
Python code for Genshin Impact daily check-in web event. For Firefox web browser.

# Requirements
1. Python 3.8
2. selenium
3. Official Mozilla geckodriver.exe (https://github.com/mozilla/geckodriver/releases)

# Usage
Edit the script and set the path to geckodriver.exe (default is C:\geckodriver.exe).  
You will need own cookie and store it locally for auto log in. Follow the steps mentioned below.  
Run the script. New Firefox window will appear.  
You have 60 seconds to log in. To log in click on the avatar on top right on the website and put your credentials.  
Wait the remaining time. Firefox will close automatically.  
In the directory of the script, new file **cookies.pkl** will be created. Never share this file with anyone!  
Now edit the mentioned below part of the python script.  

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
Add the script to Windows scheduler and... that's all!

# Additional option
When everything is set and you know it is working fine you can daily check-in with headless firefox (window will not appear)

Change:
```options.headless = False```
to
```options.headless = True```
