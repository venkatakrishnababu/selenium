#Internal Link :- It will be on the same web page
#External Link:- It will Navigate to other web page
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as requests
from selenium.webdriver.chrome.service import Service
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
##Internal Link
# driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# driver.maximize_window()
# time.sleep(4)
#driver.find_element(By.LINK_TEXT,"Computers").click()
# time.sleep(4)
# ele=driver.find_elements(By.LINK_TEXT,"Computers")
# print(len(ele))

###Broken link
driver.get('http://www.deadlinkcity.com/')
driver.maximize_window()
### we can find Number of Links in the page
Links=driver.find_elements(By.XPATH,"//a")
print(len(Links))
b=0
c=0
for i in Links:
    broken=i.get_attribute('href')
    try:
        res=requests.head(broken)
    except:
        None
    if res.status_code>=400:
        print('Broken Link:-',broken)
        b+=1
    else:
        print('valid Link:-',broken)
        c+=1
print(b)
print(c)
