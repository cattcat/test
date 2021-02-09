from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


product="動物森友會 主機"

driver=webdriver.Chrome()
driver.get("https://shopping.pchome.com.tw/")
element = driver.find_element_by_id("keyword")
element.send_keys(product)
element=driver.find_element_by_id("doSearch")
element.click()
sleep(3)
element = driver.find_element_by_xpath("//*[@id='QAAS30-A900AMY35']/dd[2]/h5/a")
sleep(2)
element.click()
sleep(5)

