from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# Initialize the WebDriver
driver = webdriver.Chrome()
# Maximize the browser window (optional)
driver.maximize_window()
##CSS using tag and id
driver.get('https://www.naukri.com/nlogin/login?URL=https://www.naukri.com/mnjuser/homepage')
driver.find_element(By.CSS_SELECTOR,"input#usernameField").send_keys('Msys')
driver.find_element(By.CSS_SELECTOR,"#usernameField").send_keys('Nutanix')
##CSS using tag and class
driver.find_element(By.CSS_SELECTOR,"input.pr-60").send_keys('venkata')
driver.find_element(By.CSS_SELECTOR,".pr-60").send_keys('krishna')
##CSS using tag and other attribute
driver.find_element(By.CSS_SELECTOR,'input[rel="required:passwordField_required|blur"]').send_keys('babu')
##CSS using class,tag and attribute(just for syntax purpose,It won't work)
#driver.find_element(By.CSS_SELECTOR,'tagname.valueofclass[attribute=value]').send_keys('abc')
driver.find_element(By.CLASS_NAME,"fs13").click()
time.sleep(4)
