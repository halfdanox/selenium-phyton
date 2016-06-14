
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
import time
#invoking chrome  browser

giris = "#dynamicHead > div.banner > div.ortala2.OHll > div.banner_1 > #not_authenticated > div.accountTopMenu_2 > div:nth-child(1) > a"

driver = webdriver.Chrome('D:/Users/btan/workspace/Basic/com/introduction/chromedriver.exe');
driver.get("http://evidea.com")
driver.find_element_by_css_selector(giris).click()
if driver.current_url == "https://guvenli.evidea.com/uyeolx":
    driver.find_element_by_id("FullName").send_keys("otomasyon 123")
    driver.find_element_by_id("Email").send_keys("test@test.com")
    driver.find_element_by_id("Password").send_keys("123456")
    driver.find_element_by_id("ConfirmPassword").send_keys("123456")
    driver.find_element_by_id("AgreementConfirmed").click()
    driver.find_element_by_id("Newsletter").click()
    driver.find_element_by_id("submitOriginal").click()
else: 
    print ("sayfa bulunamadi")




#print(driver.current_url)
#driver.get("http://gmail.com")

driver.maximize_window()
driver.close()