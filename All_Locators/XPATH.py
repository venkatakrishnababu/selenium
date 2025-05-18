from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# Initialize the WebDriver
driver = webdriver.Chrome()
# Maximize the browser window (optional)
driver.maximize_window()
## Absolute and relative XPATH
# driver.get("https://demo.nopcommerce.com/")
# driver.find_element(By.XPATH,'//*[@id="small-searchterms"]').send_keys('computers')
# driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[2]/div[2]/form/button').click()
# time.sleep(10)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa?src=gain_lose")
### XPATH_AXES using self
b=driver.find_element(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[5]/td[1]/a/self::a').text
print(b)
###XPATH_AXES using parent
#a=driver.find_element(By.XPATH,'//*[@id="leftcontainer"]/table/tbody/tr[5]/td[1]/a/parent::td').text
a=driver.find_element(By.XPATH,"//a[contains(text(),'HCL Technologies')]/parent::td").text
print(a)
####XPATH_AXES using child through ancestor
c=driver.find_elements(By.XPATH,"//a[contains(text(),'HCL Technologies')]/ancestor::tr/child::td")
print(len(c))
# for element in c:
#     print(element.text,end=' ')
#XPATH AXES using ancestor
d=driver.find_element(By.XPATH,"//a[contains(text(),'HCL Technologies')]/ancestor::tr").text
print('ancestor',d)
#XPATH AXES using descendant
e=driver.find_elements(By.XPATH,"//a[contains(text(),'HCL Technologies')]/ancestor::tr/descendant::*")
print(len(e))
# for i in e:
#     print(i.text,end='')

#XPATH AXES using following
e=driver.find_elements(By.XPATH,"//a[contains(text(),'HCL Technologies')]/ancestor::tr/following::*")
print(len(e))

#XPATH AXES using following siblings
f=driver.find_elements(By.XPATH,"//a[contains(text(),'HCL Technologies')]/ancestor::tr/following-sibling::*")
print(len(f))
#XPATH AXES using preceding
g=driver.find_elements(By.XPATH,"//a[contains(text(),'HCL Technologies')]/ancestor::tr/preceding::*")
print(len(g))

#XPATH AXES using preceding siblings
g=driver.find_elements(By.XPATH,"//a[contains(text(),'HCL Technologies')]/ancestor::tr/preceding-sibling::*")
print(len(g))
