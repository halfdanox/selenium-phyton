'''
Created on 8 Haz 2016




@author: btan
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
import time
#invoking firefox browser


driver = webdriver.Firefox()
driver.get("http://kariyer.net")
driver.find_element_by_xpath(".//*[@id='Header']/div[2]/div[2]/div/div[1]/a[2]").click()
driver.implicitly_wait(3)
driver.find_element_by_id("lgnUserName").send_keys("your_username")
driver.find_element_by_id("lgnPassword").send_keys("your_password")
driver.find_element_by_id("LinkButton1").click()


ab=driver.find_element_by_xpath(".//*[@id='dvOzgecmis']/ul/li[1]/span[4]/a")
ActionChains(driver).move_to_element(ab).perform()
driver.implicitly_wait(3)


time.sleep(3)
driver.find_element_by_xpath(".//*[@id='dvOzgecmis']/ul/li[1]/span[4]/div/ul/li[1]/a").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='A2']/span").click()
time.sleep(3)

#print(driver.current_url)
#driver.get("http://gmail.com")

driver.maximize_window()
driver.close()