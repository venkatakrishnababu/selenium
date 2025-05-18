import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains,Keys
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
ops=webdriver.ChromeOptions()
#ops.headless=True
ops.add_argument("--headless=new")
driver=webdriver.Chrome(service=serv_obj,options=ops)
driver.get("https://demo.nopcommerce.com/")
time.sleep(4)
