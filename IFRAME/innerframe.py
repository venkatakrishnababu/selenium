import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH,'//a[@href="#Multiple"]').click()
time.sleep(4)
parent_frame=driver.find_element(By.XPATH,'//*[@id="Multiple"]/iframe')
driver.switch_to.frame(parent_frame)
child_frame=driver.find_element(By.XPATH,'/html/body/section/div/div/iframe')
driver.switch_to.frame(child_frame)
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('welcome')
time.sleep(6)
