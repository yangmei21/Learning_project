#模拟拖拽
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()

url=r"F:\web自动化\8天web自动化讲义\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\drop.html"
driver.get(url)
driver.maximize_window()

#实例化并获取ActionChains类
action=ActionChains(driver)

#获取源元素
source=driver.find_element_by_css_selector("#div1")
#获取目标元素
target=driver.find_element_by_css_selector("#div2")
sleep(2)
action.drag_and_drop(source,target).perform()

sleep(2)

driver.quit()


