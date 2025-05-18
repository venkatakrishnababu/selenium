import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
driver.find_element(By.CSS_SELECTOR,"button[onclick='jsPrompt()']").click()
switch=driver.switch_to.alert ## This will switch to the alert popup
switch.send_keys('Welcome')
switch.accept() ## This is used to click on OK button
switch.dismiss() ## This will click on cancel button
time.sleep(4)

### Authentication POPUP
##Syntax :- http://username:password @test.com
driver=webdriver.Chrome()
driver.get('https://admin:admin@the-internet.herokuapp.com/digest_auth')