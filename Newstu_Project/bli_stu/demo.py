# 重新找了一个B站课程信息自动化；2024/1/1
# 运行不了的话 操作菜单栏  Run-->run-->demo(运行整个文件) 原因：默认情况下，PyCharm将检查以test开头的文件，它们是unittest.TestCase的子类
# 代码内容为webdriver常用属性：

from selenium import webdriver


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.52shici.com/')
        # self.driver.maximize_window()

    def test_prop(self):
        print("浏览器名称：" + self.driver.name)  # 浏览器名称
        print("当前URL地址：" + self.driver.current_url)  # 当前URL地址
        print("当前页面title：" + self.driver.title)  # 当前页面title
        print(self.driver.window_handles)  # 页面句柄
        print(self.driver.page_source)  # 页面源码
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_prop()
