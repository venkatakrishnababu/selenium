##It will set default wait time for all the elements
##Performance will not be reduced
# If the element is available within the time it proceed to execute further statements.
## syntax :- driver.implicitly_wait(10)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get('https://msystechnologies.udemy.com/course/learn-selenium-with-python-d/learn/lecture/33507682#overview')
driver.find_element(By.ID,"form-group--3").send_keys('traininguser205@msyslearn.com')
driver.find_element(By.ID,"form-group--3").submit()
driver.find_element(By.ID,"form-group--5").send_keys('Training@205')
driver.find_element(By.CLASS_NAME,"ud-btn-label").click()
