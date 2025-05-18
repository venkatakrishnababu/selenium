import openpyxl
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()
from Selenium.DDS_with_excel.XL import excel
driver.get('https://www.cit.com/cit-bank/resources/calculators/certificate-of-deposit-calculator')
path_of_file=r"D:\\chrome\\City bank_calculator.xlsx"
rows=excel.get_rows(path_of_file,'Sheet1')
print(rows)
driver.implicitly_wait(10)
for R in range(2,rows+1):
    ## read the data from excel
    DEP=excel.read_data(path_of_file,'Sheet1',R,1)
    MON=excel.read_data(path_of_file,'Sheet1',R,2)
    Int=excel.read_data(path_of_file,'Sheet1',R,3)
    comp=excel.read_data(path_of_file,'Sheet1',R,4)
    exp=excel.read_data(path_of_file,'Sheet1',R,5)
    ###passing the keys to application
    driver.find_element(By.XPATH,"//input[@id='mat-input-0']").clear()
    driver.find_element(By.XPATH,"//input[@id='mat-input-0']").send_keys(DEP)
    time.sleep(4)
    driver.find_element(By.XPATH, "//input[@id='mat-input-1']").clear()
    driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys(MON)
    time.sleep(4)

    driver.find_element(By.XPATH, "//*[@id='mat-input-2']").clear()
    driver.find_element(By.XPATH, "//*[@id='mat-input-2']").send_keys(Int)
    time.sleep(4)
    dropdown = driver.find_element(By.XPATH, "//div[@id='mat-select-value-1']")
    driver.execute_script("arguments[0].click();", dropdown)
    options = driver.find_elements(By.XPATH, "//mat-option/span")
    for option in options:
        if comp in option.text:
            option.click()
            break
    time.sleep(4)
    element = driver.find_element(By.XPATH, "//*[@id='CIT-chart-submit']/div")
    driver.execute_script("arguments[0].click();", element)

    ##Validation
    ele=driver.find_element(By.XPATH,"//*[@id='displayTotalValue']")
    #print(ele)# $10,202.01
    ele1=float(ele.text.replace("$",'').replace(',',''))
    #print(ele1)
    #print(type(ele1))
    #print(exp) # 10202.01
    #print(type(exp))#float
    if exp==ele1:
        print(R-1,'Row:- Test passed')
        excel.write_data(path_of_file,'Sheet1',R,6,ele.text)
        excel.write_data(path_of_file,'Sheet1',R,7,"Passed")
    else:
        print(R-1,"Row:- Test Failed")
        excel.write_data(path_of_file, 'Sheet1', R, 6, ele.text)
        excel.write_data(path_of_file, 'Sheet1', R, 7, "Failed")









