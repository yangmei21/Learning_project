#进入CSDN官网首页，悬停至收藏处；
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("https://csdn.net/")
sleep(3)
collect=driver.find_element_by_link_text("收藏")
collect.click()
#ActionChains(driver).move_to_element(collect).perform()
sleep(2)
driver.quit()