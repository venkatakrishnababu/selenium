import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
## select specific check box
# driver.find_element(By.XPATH,"//input[@class='form-check-input' and @id='sunday']").click()
# time.sleep(3)
###select all the checkboxes
# elements=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and contains(@id,'day')]")
# for ele in elements:
#     ele.click()
# time.sleep(4)

elements=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and contains(@id,'day')]")
b=(len(elements))
###select last two check boxes
# for i in range(b-2,b):
#     elements[i].click()
# time.sleep(5)

###select multiple checkboxes by choice
# for i in range(b):
#     select_box=elements[i].get_attribute('id')
#     if select_box=='monday' or select_box=='friday':
#         print(select_box)
#         elements[i].click()
# time.sleep(5)

elements[0].click()
time.sleep(8)
### select all the checkboxes without unselecting enabled check box
### Method 1
elements[0].click()
time.sleep(8)
# for ele in elements:
#     if not ele.is_selected():
#         ele.click()
### Method 2
# for ele in elements:
#     if ele.is_selected():
#         pass
#     else:
#         ele.click()
#     time.sleep(4)

####unselect the checkbox --> Same click method is used to unselect the check boxes

for ele in elements:
    if not ele.is_selected():
        ele.click()
        time.sleep(2)
ele.click()



