"""
对当前页面截图，保存至同目录指定文件夹中，并指定年月日时间文件名
"""
import os.path

from selenium import webdriver
from time import sleep, strftime, localtime, time

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def test1(self):
        self.driver.find_element(By.ID, 'kw').send_keys('新年大吉啊啊啊')
        self.driver.find_element(By.ID, 'su').click()
        sleep(2)

        # 简易截图：
        # self.driver.save_screenshot('baidu.png')

        # 带时间+保存到指定路径中
        st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
        fime_name = st + '.png'
        path = os.path.abspath('screenshot')
        file_path = path + '/' + fime_name
        self.driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    case = TestCase()
    case.test1()
