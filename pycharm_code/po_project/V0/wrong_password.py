"""
密码错误测试用例
"""

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://novel.hctestedu.com/')
driver.maximize_window()  # 窗口最大化
driver.implicitly_wait(10)  # 隐式等待

# 1.点击首页的”登录“链接，进入登录页面
driver.find_element_by_partial_link_text("登录").click()
# 2.输入用户名
driver.find_element_by_id("txtUName").send_keys("13039131596")
# 3.输入错误密码
driver.find_element_by_id("txtPassword").send_keys("123450")
# 4.点击登录按钮
driver.find_element_by_id("btnLogin").click()
# 5.获取错误提示信息
msg = driver.find_element_by_id("LabErr").text
# 断言
print("提示信息：", msg)


sleep(1)
driver.quit()