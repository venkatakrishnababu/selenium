import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.ui import Select
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
time.sleep(4)
### Count Number of the Cookies
C=driver.get_cookies()
print(len(C)) ### 6

###Read all the all cookies
for CO in C:
    print(CO)
##add a cookie
driver.add_cookie({'name':'cookie','value':'330'})
C = driver.get_cookies()
print(len(C))### 7


###Delete a cookie
driver.delete_cookie('cookie')
C=driver.get_cookies()
print(len(C))### 6
