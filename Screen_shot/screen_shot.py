import time
from turtledemo.paint import switchupdown

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(4)
try:
    abs = ActionChains(driver)
    element = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
    abs.double_click(element).perform()
    b = driver.switch_to.alert
    b.accept()
    element = driver.find_element(By.XPATH, '//span[@class="context-menu-one btn btn-neutral"]')
    abs = ActionChains(driver)
    abs.context_click(element).perform()
    time.sleep(4)
    driver.save_screenshot(r"D:\chrome\pass_test.png")
except:
    driver.save_screenshot(r"D:\chrome\fail_test.png")
finally:
    print('Executed the code')