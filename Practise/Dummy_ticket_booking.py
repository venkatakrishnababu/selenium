import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
# serv_obj=Service("D:\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.XPATH,"//input[@id='product_549']").click()
driver.find_element(By.XPATH,"//input[@id='travname']").send_keys('krishna')
driver.find_element(By.XPATH,"//input[@id='travlastname']").send_keys('babu')
driver.find_element(By.XPATH,"//input[@id='dob']").click()
m=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
m.select_by_visible_text("Aug")
y=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
y.select_by_visible_text("1997")
driver.find_element(By.XPATH,'//table[@class="ui-datepicker-calendar"]//tbody/tr[2]/td[7]/a').click()
driver.find_element(By.XPATH,"//input[@class='input-radio thwcfe-input-field' and @id='sex_1']").click()
driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("Bengaluru")
driver.find_element(By.XPATH,"//input[@id='tocity']").send_keys("Hyderabad")
driver.find_element(By.XPATH,"//input[@name='departon']").send_keys("31/05/2025")
b=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month' and @aria-label='Select month']"))
b.select_by_visible_text("Jun")
c=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year' and @aria-label='Select year']"))
c.select_by_visible_text("2026")
DAY="6"
D=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for i in D:
    if i.text==DAY:
        i.click()
driver.find_element(By.XPATH,"//span[@id='select2-reasondummy-container']").click()
driver.find_element(By.XPATH,"//input[@role='combobox']").send_keys('Other')
driver.find_element(By.XPATH,"//*[@role='option']").click()
# E=driver.find_elements(By.XPATH,"//span[@class='woocommerce-input-wrapper']//select[@id='reasondummy']")
# for i in E:
#     print(i.text)
#     if i.text=="Other":
#         print(i.click())
driver.find_element(By.XPATH,"//*[@id='deliverymethod_3']").click()
driver.find_element(By.XPATH,"//*[@id='billing_phone']").send_keys("9063123456")
driver.find_element(By.XPATH,"//*[@id='billing_email']").send_keys("abc@gmail.com")
driver.find_element(By.XPATH,"//*[@id='select2-billing_country-container']").click()
driver.find_element(By.XPATH,"//input[@class='select2-search__field']").send_keys("india")
driver.find_element(By.XPATH,"//*[@role='option']").click()
driver.find_element(By.XPATH,"//input[@id='billing_address_1']").send_keys('abc')
driver.find_element(By.XPATH,"//input[@id='billing_city']").send_keys('efg')
driver.find_element(By.XPATH,"//input[@id='billing_state']").send_keys("Andhra")
# driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input").send_keys('Andhra')
# driver.find_element(By.XPATH,"//*[@role='option']").click()
driver.find_element(By.XPATH,"//input[@id='billing_postcode']").send_keys('523169')
driver.find_element(By.XPATH,"//button[@id='place_order']").click()
time.sleep(15)
