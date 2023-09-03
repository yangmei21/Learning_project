#
from selenium import webdriver
from time import sleep


driver=webdriver.Chrome()

url=r"F:\web自动化\8天web自动化讲义\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

#定位alert按钮并点击
driver.find_element_by_css_selector("#alerta").click()
#切换到alert
#默认返回的alert对话框对象
at=driver._switch_to.alert


print("弹出框内容",at.text)
#at.accept()    #确认
at.dismiss()   #取消

driver.find_element_by_css_selector("#userA").send_keys("admin")



sleep(2)
driver.quit()




