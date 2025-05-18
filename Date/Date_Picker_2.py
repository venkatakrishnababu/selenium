import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service(r"D:\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://jqueryui.com/datepicker/")
a=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(a)
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
time.sleep(4)
YEAR="2026"
MONTH="May"
DATE="31"
while True:
    month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if month==MONTH and year==YEAR:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
time.sleep(6)

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")
for D in dates:
    if D.text==DATE:
        D.click()
time.sleep(5)
