import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.toolsqa.com/selenium-webdriver/selenium-testing/")
time.sleep(4)
driver.find_element(By.XPATH,'//span[@class="navbar__tutorial-menu--text"]').click()
time.sleep(4)
a=driver.find_element(By.XPATH,"//span[normalize-space()='QA Practices']")
b=driver.find_element(By.XPATH,"//span[normalize-space()='Front-End Testing Automation']")
c=driver.find_element(By.XPATH,"//span[normalize-space()='Mobile Testing Automation']")
abs=ActionChains(driver)
abs.move_to_element(a).move_to_element(b).move_to_element(c).perform()
