from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.add_cookie({"name":"BDUSS","value":"0pITkxhRXdFZFFSOWNwR2pQU3VHfjNWaWc1cGdhRjlQZ3pQWEgtc2dlLWhRamhpRVFBQUFBJCQAAAAAAAAAAAEAAAC0ZnFd0e52aXYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKG1EGKhtRBiY"})

driver.maximize_window()
driver.implicitly_wait(20)

#获取所有的cookies信息
cookies=driver.get_cookies()
print("cookies内容：",cookies)
for co in cookies:
    print(co)

cokie=driver.get_cookies("name")
print(cokie)



sleep(3)
driver.refresh()

sleep(3)
driver.quit()