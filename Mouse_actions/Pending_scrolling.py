import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select

serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
# driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")

#Scrolling :-

# Scroll to the element
#driver.execute_script("arguments[0].scrollIntoView();", element)

# Scroll to the bottom of the page
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# wait=WebDriverWait(driver,10,2)
element=driver.find_element(By.LINK_TEXT,"Bank Project").click()
#driver.execute_script("arguments[0].scrollIntoView();",element)

from selenium.webdriver.common.keys import Keys

body = driver.find_element("tag name", "body")
body.send_keys(Keys.END)  # Simulates pressing the "End" key

