from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

url=r"F:\web自动化\8天web自动化讲义\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)
sleep(3)
username=driver.find_element_by_id("userA")
password=driver.find_element_by_id("passwordA")
tel=driver.find_element_by_class_name("telA")
username.send_keys("admin")
password.send_keys("123456")
tel.send_keys("15552522252")
sleep(3)
driver.find_element_by_link_text("访问 新浪 网站").click()
sleep(2)

driver.quit()