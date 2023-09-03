#进入CSDN官网首页，点击（右击）搜索按钮；
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("https://csdn.net/")
sleep(3)
button=driver.find_element_by_id("toolbar-search-button")

ActionChains(driver).context_click(button).perform()
sleep(2)
driver.quit()