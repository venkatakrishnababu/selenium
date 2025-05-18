import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.tutorialspoint.com/selenium/practice/webtables.php")

### print Number of rows and colums
ROW=len(driver.find_elements(By.XPATH,"//table[@class='table table-striped mt-3']//tr[1]/td"))
print("length of the rows:-",ROW)
COL=len(driver.find_elements(By.XPATH,"//table[@class='table table-striped mt-3']//tr/td[1]"))
print("length of coloums:-",COL)

## Read specific element in a row or colums
ele=driver.find_element(By.XPATH,"//table[@class='table table-striped mt-3']//tr[2]/td[4]")
print('specific element:-',ele.text)

## Read all the elements in the row and coloums
# for c in range(1,COL+1):
#     for r in range(1,ROW+1):
#         ele=driver.find_element(By.XPATH, "//table[@class='table table-striped mt-3']//tr["+str(c)+"]/td["+str(r)+"]")
#         print(ele.text,end=' ')
#     print()

## find the elements based on the condtion
# for c in range(1,COL+1):
#     b=driver.find_element(By.XPATH,"//table[@class='table table-striped mt-3']//tr["+str(c)+"]/td[2]")
#     if b.text=='Cantrell':
#         d=driver.find_element(By.XPATH, "//table[@class='table table-striped mt-3']//tr["+str(c)+"]/td[5]")
#         print(d.text)
#         break
