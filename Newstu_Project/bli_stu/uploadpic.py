from selenium import webdriver
import os
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://baidu.com')
time.sleep(1)
driver.find_element(By.CLASS_NAME,'soutu-btn').click()
time.sleep(1)
driver.find_element(By.CLASS_NAME,'upload-pic').send_keys(r"F:\picture\pic1.png")
time.sleep(2)