import time

from selenium import webdriver

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")

driver.maximize_window()

time.sleep(3)
driver.quit()
