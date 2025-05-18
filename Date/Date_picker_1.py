import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
serv_obj=Service(r"D:\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://jqueryui.com/datepicker/")
a=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(a)
driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("04/23/2025")
#driver.quit()