#刷新、获取页面标题、URL地址、关闭页面
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

url=r"F:\web自动化\8天web自动化讲义\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册实例.html"
driver.get(url)

driver.maximize_window()
driver.find_element_by_css_selector("#user").send_keys("admin")
sleep(2)
driver.refresh()
title=driver.title
print("当前页面标题：",title)
current_url=driver.current_url
print("当前URL地址为：",current_url)

driver.find_element_by_partial_link_text("注册A").click()
sleep(2)

driver.close()

sleep(2)

driver.quit()














