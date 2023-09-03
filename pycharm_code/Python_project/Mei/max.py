from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
sleep(3)
driver.maximize_window()
sleep(2)
driver.set_window_size(300,200)
sleep(3)
driver.set_window_position(320,150)
sleep(3)
driver.quit()