import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

### Opening link in the newtab

# driver.get("https://demo.nopcommerce.com/")
# time.sleep(4)
# driver.find_element(By.XPATH,'//a[@class="ico-register"]').send_keys(Keys.CONTROL+Keys.RETURN)
# time.sleep(5)

### open new tab and switches to new tab

# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://testautomationpractice.blogspot.com/")

####  open new window and switches to new window

driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window')
driver.get("https://testautomationpractice.blogspot.com/")



