#录入、清除、点击按钮
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

url=r"F:\web自动化\8天web自动化讲义\web自动化_day01_课件+笔记+资料+代码\web自动化_day01_课件+笔记+资料+代码\02_其他资料\注册A.html"
driver.get(url)

driver.find_element_by_css_selector("#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
driver.find_element_by_css_selector("#telA").send_keys("12112522.com")
driver.find_element_by_css_selector("#emailA").send_keys("123@123.com")

sleep(2)
driver.find_element_by_css_selector("#telA").clear()
driver.find_element_by_css_selector("#telA").send_keys("15585855525")

driver.find_element_by_css_selector("button").click()
sleep(2)
driver.quit()