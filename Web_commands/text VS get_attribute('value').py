##text :- text will return the value only if there is any inner text available
##else it will return Nothing
##get_attribute :- it will return the value based on the attribute that we have provided
#for example class,id,href,value

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')

## Here the locator web element don't have any innertext so it is returning empty string
a=driver.find_element(By.XPATH,"//input[@id='Email']")
print('text value of a :',a.text)
print('get attribute value of a :',a.get_attribute('value'))
time.sleep(3)

## Here Login button has inner text so it text will return as LOGIN
b=driver.find_element(By.XPATH,'//button[@class="button-1 login-button"]')
print('text value of b :',b.text)
print('get class attribute value of b :',b.get_attribute('class'))
print('get value attribute value of b :',b.get_attribute('value'))