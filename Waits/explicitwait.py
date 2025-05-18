import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
time.sleep(4)
mywait=WebDriverWait(driver,10,2,[Exception])
try:
    element = mywait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="small-searchterms"]')))
    print('element found')
except:
    print("Condition Not satisfied,element not visible with in time","check the locator is valid or not")



