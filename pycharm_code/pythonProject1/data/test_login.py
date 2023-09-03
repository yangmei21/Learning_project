# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestLogin():
    def test_login(self,name,password):
        #  固定语法
        driver_path = r'E:\Python3.9\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.implicitly_wait(10)

        self.driver.get("http://novel.hctestedu.com/")
        self.driver.set_window_size(1065, 751)
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "txtUName").click()
        self.driver.find_element(By.ID, "txtUName").send_keys(name)
        time.sleep(2)
        self.driver.find_element(By.ID, "txtPassword").send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.ID, "btnLogin").click()
        time.sleep(2)
        assert self.driver.find_element(By.LINK_TEXT, "18890032513").text == "18890032513"
        self.driver.find_element(By.LINK_TEXT, "退出").click()
        self.driver.close()
