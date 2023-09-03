#获取元素操作
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

url=r"F:\web自动化\8天web自动化讲义\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册实例.html"
driver.get(url)

driver.maximize_window()
#获取用户名文本框大小
size=driver.find_element_by_css_selector("#user").size
print("用户名大小为：",size)
#获取页面上第一个超文本连接内容
text=driver.find_element_by_css_selector("a").text
print("页面中第一个超文本链接内容：",text)
#获取第一个超文本链接地址-----get_attribute()
att=driver.find_element_by_css_selector("a").get_attribute("href")
print("第一个超文本链接地址：",att)
#判断span元素是否可见
display=driver.find_element_by_css_selector("span").is_displayed()
print("span元素是否可见：",display)
#判断取消按钮是否可用
enable=driver.find_element_by_css_selector("#cancel").is_enabled()
print("取消按钮是否可用",enable)
#判断旅游是否被选中
selected=driver.find_element_by_css_selector("#ly").is_selected()
print("是否被选中：",selected)

sleep(2)
driver.quit()















