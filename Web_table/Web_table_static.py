import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
#Count Number of rows and columns
# ROW=len(driver.find_elements(By.XPATH,"//table[@id='productTable']//tbody/tr[1]/td"))
# print(ROW)
# COL=len(driver.find_elements(By.XPATH,"//table[@id='productTable']//tbody/tr/td[1]"))
# print(COL)

##Read all the rows and columns data
# C=driver.find_element(By.XPATH,"//table[@id='productTable']//tbody/tr[3]/td[2]")
# print(C.text)
# for COL in range(1,6):
#     for ROW in range(1,5):
#         f=driver.find_element(By.XPATH, "//table[@id='productTable']//tbody/tr["+str(COL)+"]/td["+str(ROW)+"]")
#         print(f.text,end=' ')
#     print()
#Read the data based on condition
# d=driver.find_elements(By.XPATH,"//table[@id='productTable']//tbody/tr/td[2]")
# print(len(d))

###READ the data based on conditions

for i in range(1,6):
    d=driver.find_element(By.XPATH,"//table[@id='productTable']//tbody/tr["+str(i)+"]/td[2]")
    if d.text=="Smartphone":
        e=driver.find_element(By.XPATH, "//table[@id='productTable']//tbody/tr[" + str(i) + "]/td[3]")
        print(e.text,d.text)