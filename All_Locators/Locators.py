from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# Initialize the WebDriver (Make sure ChromeDriver is installed)
driver = webdriver.Chrome()
# Maximize the browser window (optional)
driver.maximize_window()
# driver.get("https://www.naukri.com/nlogin/login?URL=https://www.naukri.com/mnjuser/homepage")
# time.sleep(5)
# driver.find_element(By.ID, "usernameField").send_keys("abc.gmail.com")
# # Wait for a few seconds before closing (optional)
# time.sleep(5)
# # Close the browser
# driver.quit()

driver.get("https://demo.nopcommerce.com/")
time.sleep(10)
b=driver.find_element(By.TAG_NAME,"a")
print(type(b))
# time.sleep(2)
# driver.quit()
