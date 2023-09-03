#
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

driver.get("https://csdn.net/")
driver.maximize_window()
driver.implicitly_wait(30)
sleep(3)
js="window.scrollTo(0,100000)"
driver.execute_script(js)




sleep(2)
driver.quit()