import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/#google_vignette")
S=driver.find_element(By.XPATH,"//div[@id='slider-range']//span[1]")
E=driver.find_element(By.XPATH,"//div[@id='slider-range']//span[2]")
print('Before dragging')
print(S.location)
print(E.location)
abs=ActionChains(driver)
abs.drag_and_drop_by_offset(S,100,0).perform()
abs.drag_and_drop_by_offset(E,-100,0).perform()
time.sleep(5)
print('After dragging')
print(S.location)
print(E.location)