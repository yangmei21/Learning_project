#进入CSDN官网首页，点击（左击）搜索按钮；
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("https://csdn.net/")
sleep(3)
button=driver.find_element_by_id("toolbar-search-button")
button.click()
sleep(5)

driver.quit()