import time
from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(4)
a=driver.find_element(By.XPATH,'//select[@id="country"]')
drop_down=Select(a)
drop_down.select_by_visible_text('Canada')
drop_down.select_by_value("uk")
drop_down.select_by_index(4)
time.sleep(4)
## To print Number of elements in the check box
b=drop_down.options
print(len(b))
##To print all the web elements
for i in b:
    print(i.text)