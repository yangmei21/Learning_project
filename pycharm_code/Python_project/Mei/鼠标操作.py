#模拟鼠标操作
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()

url=r"F:\web自动化\8天web自动化讲义\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)
driver.maximize_window()

#实例化并获取ActionChains类
action=ActionChains(driver)

#定位用户名 在用户名上右击鼠标  预期：粘贴
#获取用户名元素
username=driver.find_element_by_css_selector("#userA")
#调用右击方法
action.context_click(username).perform()
sleep(2)

#发送用户名admin，并进行双击 预期：选中admin
username.send_keys("admin")
action.double_click(username).perform()
sleep(2)

#移动到注册按钮上 预期：按钮变色 出现 加入会员A
action.move_to_element(driver.find_element_by_css_selector("button")).perform()
sleep(2)

#关闭浏览器驱动
driver.quit()











