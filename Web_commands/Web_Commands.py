from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
### Application Commands
# ur='https://money.rediff.com/gainers/bse/daily/groupa?src=gain_lose'
# driver.get(ur)
# print(driver.current_url)
# print(driver.title)
# b="Daily Gainers: BSE, NSE, Stock quotes, share market, stock market, stock tips: Rediff Stocks"
# if b==driver.title:
#     print('Expected title is valid')
# if ur==driver.current_url:
#     print('Current url valid')
# print(driver.page_source)

####Conditional commands
# driver.get('https://demo.nopcommerce.com/register?returnUrl=%2F')
# search_box=driver.find_element(By.XPATH,'//*[@id="small-searchterms"]')
# print(search_box.is_displayed())
# print(search_box.is_enabled())
# raido_button=driver.find_element(By.XPATH,'//*[@id="gender-male"]')
# print(raido_button.is_selected())
# raido_button.click()
# print(raido_button.is_selected())

###Browser Commands
#Close and quit --> Close will terminate only one browser window but quit all the browser windows

# driver.get('https://demo.nopcommerce.com/register?returnUrl=%2F')
# driver.find_element(By.XPATH,'/html/body/div[6]/div[4]/div[1]/div[4]/div[1]/ul/li[4]/a').click()
# time.sleep(3)
# #driver.close()
# driver.quit()

######Navigational Commands (Back,forward,Refresh)
# driver.get('https://demo.nopcommerce.com/register?returnUrl=%2F')
# time.sleep(3)
# driver.get('https://www.amazon.com/')
# time.sleep(3)
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.back()
# driver.refresh()
# time.sleep(3)

### Wait Commands
