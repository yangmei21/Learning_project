'''
test1:调用弹框
test2:获取窗口标题
test3:改变框色（但是没成功！！！）
test4:跳转到搜索结果页滑动到底部
'''
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def test1(self):
        self.driver.execute_script("alert('测试啊啊啊啊')")
        sleep(2)
        self.driver.switch_to.alert.accept()
        self.driver.quit()

    def test2(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)
        self.driver.quit()

    def test3(self):
        js = 'var q=document.getElementById("kw"); q.style.border="2px solid red"'
        self.driver.execute_script(js)
        sleep(5)
        self.driver.quit()

    def test4(self):
        self.driver.find_element(By.ID, 'kw').send_keys('新年快乐')
        self.driver.find_element(By.ID, 'su').click()
        sleep(2)
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)
        sleep(3)


if __name__ == '__main__':
    case = TestCase()
    # case.test1()
    # case.test2()
    case.test4()
