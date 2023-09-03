# 导包
from selenium import webdriver
from time import sleep

# 获取driver对象
driver = webdriver.Chrome()
# 打开URL
url = "http://novel.hctestedu.com/"
driver.get(url)

# 最大化浏览器
driver.maximize_window()
# 隐式等待
driver.implicitly_wait(20)
# 点击登录连接
driver.find_element_by_partial_link_text("登录").click()
# 输入用户名
driver.find_element_by_id("txtUName").send_keys("18890032513")
# 输入密码
driver.find_element_by_id("txtPassword").send_keys("199805021")
# 点击登录
driver.find_element_by_id("btnLogin").click()
# 获取错误提示信息
msg = driver.find_element_by_id("LabErr").text
# 断言
print("提示信息：", msg)
assert msg == "手机号或密码错误！"

driver.quit()
