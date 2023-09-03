#select选择
from selenium import webdriver
from time import sleep

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

url=r"F:\web自动化\8天web自动化讲义\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

driver.maximize_window()
driver.implicitly_wait(30)

el=driver.find_element_by_css_selector("#selectA")
sleep(2)
#通过下标形式访问
Select(el).select_by_index(1)
sleep(2)
Select(el).select_by_index(2)

#通过value值形式访问
sel=Select(el)               #获取Select引用对象
sel.select_by_value("sh")    #切换上海
sleep(2)
sel.select_by_value("gz")    #切换广州

#通过显示文本切换
sleep(2)
Select(el).select_by_visible_text("A上海")
sleep(2)
Select(el).select_by_visible_text("A重庆")
sleep(2)
driver.quit()








