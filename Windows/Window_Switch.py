import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH,'//input[@class="wikipedia-search-input"]').send_keys('selenium')
time.sleep(4)
driver.find_element(By.XPATH,'//input[@class="wikipedia-search-button"]').click()
time.sleep(4)
b=driver.find_elements(By.PARTIAL_LINK_TEXT,"Selenium")
print(driver.title)
print(len(b))
for i in b:
    i.click()
    time.sleep(4)
window_id=driver.window_handles
for i in window_id:
    driver.switch_to.window(i)
    print(driver.title)
#driver.quit()


