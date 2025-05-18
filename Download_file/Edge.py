import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# import os
# c=os.getcwd()
# print(c)
d=r"D:\chrome"
def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj=Service(r"D:\Downloads\edgedriver_win64\msedgedriver.exe")
    p={"download.default_directory":d}
    ops=webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",p)
    driver=webdriver.Edge(service=serv_obj, options=ops)
    return driver
driver=edge_setup()
driver.get("https://www.tutorialspoint.com/selenium/practice/upload-download.php")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.XPATH,"//a[@id='downloadButton']").click()
time.sleep(4)
