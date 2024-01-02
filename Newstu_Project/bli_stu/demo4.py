# 隐式等待、显示等待使用

from selenium.webdriver.support import  expected_conditions as EC
from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def test_implicitly(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, 'kw').send_keys("心想事成")
        self.driver.find_element(By.ID, 'su').click()
        self.driver.quit()


    def test_wait(self):
        wait=WebDriverWait(self.driver,2)
        wait.until(EC.title_is('百度一下，你就知道'))
        self.driver.find_element(By.ID,'kw').send_keys('万事顺遂！')
        self.driver.find_element(By.ID,'su').click()
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    # case.test_implicitly()
    case.test_wait()
