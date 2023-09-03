from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化方法
    def __init__(self):
        # 获取driver
        self.driver = webdriver.Chrome()
        # 最大化
        self.driver.maximize_window()
        # 打开URL
        self.driver.get("http://novel.hctestedu.com/")

        # 查找元素方法
        # loc:元素的配置信息，格式为元组；timeout：默认超市时间为30，可以通过传入参数进行修改
        # poll：默认访问频率0.5秒 return：查找到的元素
        def base_find_element(self, loc, timeout=30, poll=0.5):
            return WebDriverWait(self.driver,
                                 timeout=timeout,
                                 poll_frequency=poll).until(lambda x: x.find_element(*loc))

        # 点击方法
        def base_click(self, loc):
            self.base_find_element(loc).click()

        # 输入方法
        def base_input(self, loc, value):
            # 获取元素
            el = self.base_find_element(loc)
            # 清空
            el.clear()
            # 输入
            el.send_keys(value)
