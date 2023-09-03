"""
公共方法模块：命名utils
最好是放在工程公目录下
"""
from selenium import webdriver
from time import sleep


class DriverUtil(object):
    """浏览器对象管理类"""
    # 说明：对象变量只需要在类定义内部使用，因此定义为私有；避免后续别人调用出错
    __driver = None  # 浏览器对象变量初始化状态

    # 为了方便调用，定义为类方法；省去实例化对象那一步
    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        # 为了防止在同一次测试过程中，调用获取浏览器对象方法时，都会创建一个新的浏览器对象
        # 因此有必要先判断对象是否存在，不存在时再创建
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.get('http://novel.hctestedu.com/')
            cls.__driver.maximize_window()  # 窗口最大化
            cls.__driver.implicitly_wait(10)  # 隐式等待
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器对象方法"""
        # 说明：必须保证浏览器对象存在，才能执行退出操作
        if cls.__driver:  # 等价于：if self.__driver is not None:
            sleep(2)
            cls.__driver.quit()
            cls.__driver = None  # 保险手段：移除对象后，保留对象变量，以备下一次使用


if __name__ == '__main__':
    # my_driver = DriverUtil()  # 类实例化对象并且接收
    # my_driver.get_driver()
    # sleep(2)
    # my_driver.quit_driver()
    # 定义为类方法，可以直接由类对象调用，省略实例化对象步骤
    DriverUtil.get_driver()  # 获取浏览器对象
    sleep(2)
    DriverUtil.quit_driver()  # 退出浏览器对象
