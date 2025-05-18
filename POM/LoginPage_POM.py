# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://admin-demo.nopcommerce.com/admin/")
# driver.find_element(By.XPATH,"//*[@id='Email']").clear()
# driver.find_element(By.XPATH,"//*[@id='Email']").send_keys("admin@yourstore.com")
# driver.find_element(By.XPATH,"//*[@id='Password']").clear()
# driver.find_element(By.XPATH,"//*[@id='Password']").send_keys("admin")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# time.sleep(4)

class Test_Login_Page:
    #Locotors
    user_email_text= "//*[@id='Email']"
    user_pwd_text= "//*[@id='Password']"
    button_Login= "//button[@type='submit']"
    ##constructor
    def __init__(self,driver):
        self.driver=driver
    ##Actions
    def login_user(self,username):
        self.driver.find_element(By.XPATH,self.user_email_text).clear()
        self.driver.find_element(By.XPATH,self.user_email_text).send_keys(username)

    def login_password(self,password):
        self.driver.find_element(By.XPATH,self.user_pwd_text).clear()
        self.driver.find_element(By.XPATH,self.user_pwd_text).send_keys(password)

    def login_button(self):
        self.driver.find_element(By.XPATH,self.button_Login).click()





