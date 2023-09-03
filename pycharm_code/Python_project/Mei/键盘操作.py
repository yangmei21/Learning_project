#键盘操作--复制、粘贴、删除
from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()

url=r"F:\web自动化\8天web自动化讲义\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)
driver.maximize_window()

username=driver.find_element_by_css_selector("#userA")
#输入admin

username.send_keys("admin1")
sleep(2)
#删除数字1
username.send_keys(Keys.BACK_SPACE)
#全选admin
sleep(2)
username.send_keys(Keys.CONTROL,'a')
#复制
username.send_keys(Keys.CONTROL,'c')
#定位密码框 并执行粘贴
driver.find_element_by_css_selector("#passwordA").send_keys(Keys.CONTROL,'v')

sleep(2)
driver.quit()

