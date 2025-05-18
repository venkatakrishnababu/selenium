from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
serv_obj=Service(r"D:\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj,options=ops)
driver.get("https://www.gps-coordinates.net/my-location#google_vignette")
driver.quit()
