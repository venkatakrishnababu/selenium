import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# import os
# c=os.getcwd()
# print(c)
d=r"D:\chrome"
def chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    p={"download.default_directory":d}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",p)
    driver=webdriver.Chrome(service=serv_obj,options=ops)
    return driver
driver=chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/upload-download.php")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.XPATH,"//a[@id='downloadButton']").click()
time.sleep(4)
