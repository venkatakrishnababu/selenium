from re import search

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v133.fed_cm import click_dialog_button

driver=webdriver.Chrome()
#driver.get('https://demo.nopcommerce.com/register?returnUrl=%2F')
##find_element --> Returns a single web element
### 1.)Locator matching with one web element
# driver.find_element(By.LINK_TEXT,"Log in").click()
# time.sleep(5)
##example -2
# driver.get('https://demo.nopcommerce.com/')
# driver.find_element(By.XPATH,"//a[@class='ico-login']").click()
# time.sleep(3)
###### 2.) Locator with more than one web element
# driver.get('https://demo.nopcommerce.com/')
# abc=driver.find_element(By.XPATH,"//div[@class=' footer']//a").text
# print(abc)
#### 3.) Element which is not available will throw NoSuchElementException

#######find_elements-->>Returns multiple web elements

###1.) Locator matching only one element
# driver.get('https://demo.nopcommerce.com/')
# elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(elements))
# elements[0].send_keys('Apple')
# time.sleep(3)

###2.) Locator with more than one web element
# driver.get('https://demo.nopcommerce.com/')
# element=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(element))
# for i in element:
#     print(i.text)

### 3.) It will not throw any exception even if we didn't find the element
###It will returns empty list

