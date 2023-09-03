#访问CSDN首页：搜索框录入文字；清空搜索框文字；输出搜索按钮文字、搜索框大小
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('https://csdn.net/')
sleep(3)
#text_label1=driver.find_element_by_xpath('//*[@id="toolbar-search-input"]')
text_label1=driver.find_element_by_id("toolbar-search-input")
text_label1.send_keys("软件测试")
sleep(2)
text_label1.clear()
sleep(2)
button=driver.find_element_by_id("toolbar-search-button")
print("按钮大小：",button.size)
print("按钮文字：",button.text)
sleep(2)
driver.quit()