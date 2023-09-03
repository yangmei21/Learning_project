from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

url=r"F:\web自动化\8天web自动化讲义\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

#1.使用css id选择器 定位用户名，输入admin
driver.find_element_by_css_selector("#userA").send_keys("admin22")
#2.使用css 属性选择器 定位密码框，输入123456
driver.find_element_by_css_selector("[name='passwordA']").send_keys("123456")
#3.使用css class选择器 定位电话号，输入电话号
driver.find_element_by_css_selector(".telA").send_keys("15552522236")
#4.使用css 元素选择器 定位span标签获取文本值
span=driver.find_element_by_css_selector("span").text
print("获取的span值为：",span)
#5.使用css 层级选择器 定位email，输入邮箱
driver.find_element_by_css_selector("p>input[placeholder='电子邮箱A']").send_keys("115436@123.com")
sleep(3)

driver.quit()






