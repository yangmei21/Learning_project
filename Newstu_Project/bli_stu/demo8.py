# 页面存在frame时，通过以下方式，先进入frame里面进行操作才可，否则无法正确定位
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://sahitest.com/demo/framesTest.htm')

    def test1(self):
        top = self.driver.find_element(By.NAME, 'top')
        self.driver.switch_to.frame(top)
        self.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[1]').click()
        sleep(1)

        self.driver.switch_to.default_content()  # 从第一个frame出来，进去另一个frame
        sleep(2)
        second = self.driver.find_element(By.XPATH, '/html/frameset/frame[2]')
        self.driver.switch_to.frame(second)
        self.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[2]').click()
        sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test1()
