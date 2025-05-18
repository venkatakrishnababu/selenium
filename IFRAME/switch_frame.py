import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://vinothqaacademy.com/iframe/")
driver.maximize_window()
###Switch between individuall frames
driver.switch_to.frame("employeetable")
time.sleep(2)
driver.find_element(By.ID,"nameInput").send_keys('abc')
time.sleep(4)
#b=WebDriverWait(driver, 10)
#checkbox =driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
time.sleep(4)
# for checkbox in checkboxes:
#     b.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']")))
#     checkbox.click()
# b=driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.switch_to.default_content()
driver.switch_to.frame("popuppage")
driver.find_element(By.NAME,"promptalertbox1234").click()
driver.switch_to.alert.send_keys('yes')
time.sleep(5)

