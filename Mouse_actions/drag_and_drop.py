import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
time.sleep(4)
f=driver.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(f)
s=driver.find_element(By.XPATH,"//img[@alt='The peaks of High Tatras']")
t=driver.find_element(By.XPATH,"//div[@class='ui-widget-content ui-state-default ui-droppable']")
abs=ActionChains(driver)
abs.drag_and_drop(s,t).perform()
time.sleep(5)
