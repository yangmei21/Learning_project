"""
账号不存在测试用例
"""
# 1.点击首页的’登录‘链接，进入登录页面
# 2.输入一个不存在的用户名
# 3.输入密码
# 4.输入验证码
# 5.点击登录按钮
# 6.获取错误提示信息

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://novel.hctestedu.com/')
driver.maximize_window()  # 窗口最大化
driver.implicitly_wait(10)  # 隐式等待

# 1.点击首页的”登录“链接，进入登录页面
driver.find_element_by_partial_link_text("登录").click()
# 2.输入一个不存在的用户名
driver.find_element_by_id("txtUName").send_keys("88890032513")
# 3.输入密码
driver.find_element_by_id("txtPassword").send_keys("19980502")
# 4.点击登录按钮
driver.find_element_by_id("btnLogin").click()
# 5.获取错误提示信息
msg = driver.find_element_by_id("LabErr").text
# 断言
print("提示信息：", msg)


sleep(1)
driver.quit()




