from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get('https://www.cit.com/cit-bank/resources/calculators/certificate-of-deposit-calculator')
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='mat-input-0']").clear()
driver.find_element(By.XPATH,"//input[@id='mat-input-0']").send_keys("10000")

driver.find_element(By.XPATH, "//input[@id='mat-input-1']").clear()
driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("24")
driver.find_element(By.XPATH,"//*[@id='mat-input-2']").clear()
driver.find_element(By.XPATH,"//*[@id='mat-input-2']").send_keys('4')
dropdown = driver.find_element(By.XPATH, "//div[@id='mat-select-value-1']")
driver.execute_script("arguments[0].click();", dropdown)
options = driver.find_elements(By.XPATH, "//mat-option/span")
for option in options:
    print(option.text)

# element=driver.find_element(By.XPATH,"//*[@id='CIT-chart-submit']/div")
# driver.execute_script("arguments[0].click();",element)

