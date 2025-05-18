import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(4)
#####Right click
element=driver.find_element(By.XPATH,'//span[@class="context-menu-one btn btn-neutral"]')
print(element.text)
abs=ActionChains(driver)
abs.context_click(element).perform()
time.sleep(4)
driver.refresh()
time.sleep(8)
#####Double Clicking
element=driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")
print(element.text)
abs=ActionChains(driver)
abs.double_click(element).perform()
time.sleep(4)
driver.switch_to.alert
driver.switch_to.alert.dismiss()
time.sleep(4)