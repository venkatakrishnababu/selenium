import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from LoginPage_POM import Test_Login_Page
class Test_Login:
    def test_login(self):
        self.serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        self.driver=webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://admin-demo.nopcommerce.com/admin/")
        self.driver.maximize_window()
        time.sleep(10)
        self.lp=Test_Login_Page(self.driver)
        self.lp.login_user('admin@yourstore.com')
        self.lp.login_password('admin')
        self.lp.login_button()
        #self.driver.switch_to.frame(0)
        #time.sleep(10000000)
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        time.sleep(20)