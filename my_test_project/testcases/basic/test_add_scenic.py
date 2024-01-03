from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
import re


class TestAddScenic(object):
    def __init__(self, login):
        self.login = login

    # 测试添加景区失败，图片封面图为空
    def test_add_scenic_err(self):
        excpet = '请上传景点图片或景点缩略图！'
        # 点击关闭弹框
        self.login.driver.find_element(By.XPATH, '//*[@id="driver-popover-item"]/div[4]/button').click()
        sleep(1)

        # 点击发布信息管理
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="menuNav"]/div[1]/app-side-nav/div/div[2]/app-nav-bar/ul/li[3]/div[1]/span[1]').click()
        sleep(2)
        # 点击景点管理
        self.login.driver.find_element(By.LINK_TEXT,
                                       '景点管理').click()
        sleep(1)

        # 点击新建
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept/div/app-card-table-wrap/nz-card/div[1]/div/div[2]/div/div[1]/button/span').click()
        # 页面最大化
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/button/span/div/span[1]').click()
        # 定位分类选择框,点击展开
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[1]/nz-form-control/div/div/nz-select').click()

        options = WebDriverWait(self.login.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH,
                                                   '//*[@id="cdk-overlay-3"]/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item/div'))
        )
        # 定位并选择自己想要勾选的分类
        for option in options:
            if option.text == "温泉":
                option.click()
                break
        # self.login.driver.find_element(By.XPATH,'//*[@id="cdk-overlay-3"]/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[6]/div').click()
        sleep(2)
        # 点击确认按钮
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[3]/button[1]').click()

        loc = (By.XPATH, '//*[@id="cdk-overlay-4"]/nz-message-container/div/nz-message/div/div/div/span[2]')
        WebDriverWait(self.login.driver, 20, 0.5).until(EC.visibility_of_element_located(loc))
        msg = self.login.driver.find_element(*loc).text
        print(msg)
        assert msg == excpet
        self.login.driver.quit()

    # 添加景区成功
    def test_add_scenic_right(self):
        scen_name = '安徽黄山呈坎古镇'
        scen_detail = '呈坎（kǎn）位于世界自然和文化遗产——安徽省黄山风景区的南麓（北纬29°55′，东经118°15′；是国家5A级旅游景区古徽州文化旅游区组成部分，在徽州区通往黄山的公路佛子岭段折向东北五公里处），北距黄山40公里，南距徽州区政府驻地--岩寺镇15公里。呈坎地处青山翠竹之中，集自然景观、人文景观为一体。'
        scen_add = '黄山市徽州区黄山南面40公里处灵山和丰山之间'
        scen_phone = '暂无'
        excpet = '必填项'
        # 点击关闭弹框
        self.login.driver.find_element(By.XPATH, '//*[@id="driver-popover-item"]/div[4]/button').click()
        sleep(1)
        # 点击发布信息管理
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="menuNav"]/div[1]/app-side-nav/div/div[2]/app-nav-bar/ul/li[3]/div[1]/span[1]').click()
        sleep(2)
        # 点击景点管理
        self.login.driver.find_element(By.LINK_TEXT,
                                       '景点管理').click()

        sleep(2)
        # 获取列表数据总数
        # ！！！
        # #定位包含总数据条数信息的元素
        # total_records_element=self.login.driver.find_element(By.XPATH,'/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept/div/app-card-table-wrap/nz-card/div[2]/app-tree-table/nz-table/nz-spin/div/nz-pagination/ul/li[1]')
        # #获取元素文本信息
        # total_records_text=total_records_element.text
        # #使用正则表达式提取总数据条数
        # matches=re.search(r'共(\dt)条',total_records_text)
        # if matches:
        #     total_records=int(matches.group(1))
        #     print("总数居条数：",total_records)
        # else:
        #     print("无法提取总数居条数信息")
        # sleep(3)

        # 点击新建
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept/div/app-card-table-wrap/nz-card/div[1]/div/div[2]/div/div[1]/button/span').click()
        # 页面最大化
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/button/span/div/span[1]').click()
        # 定位分类选择框,点击展开
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[1]/nz-form-control/div/div/nz-select').click()

        options = WebDriverWait(self.login.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH,
                                                   '//*[@id="cdk-overlay-3"]/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item/div'))
        )

        # 定位并选择自己想要勾选的分类
        for option in options:
            if option.text == "古村古镇":
                option.click()
                break
        sleep(2)

        # 上传景点图片
        # upload_element = self.login.driver.find_element(By.XPATH,
        #                                                 '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[2]/nz-form-control/div/div/div[1]/nz-upload/div/div')
        # upload_element.send_keys(r"F:\picture\pic1.png")
        # upload_element.send_keys(Keys.RETURN)
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[2]/nz-form-control/div/div/div[1]/nz-upload/div/div/input').send_keys(
            r"F:\picture\pic2.png")

        # 上传景点缩略图
        upload_element = self.login.driver.find_element(By.XPATH,
                                                        '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[3]/nz-form-control/div/div/div[1]/nz-upload/div/div/input')
        upload_element.send_keys(r"F:\picture\pic3.png")
        # upload_element.send_keys(Keys.RETURN)

        # 填写景点名称
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[4]/nz-form-control/div/div/input[1]').send_keys(
            scen_name)
        # 填写风景介绍
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[5]/nz-form-control/div/div/textarea').send_keys(
            scen_detail)
        # 填写景点地址
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[6]/nz-form-control/div/div/input').send_keys(
            scen_add)
        # 填写联系电话
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[9]/nz-form-control/div/div/input').send_keys(
            scen_phone)
        sleep(5)
        # 选择开放起始时间
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[7]/nz-form-control/div/div/nz-time-picker/div/input').send_keys(
            "8:00")
        # 选择开放截至时间
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[8]/nz-form-control/div/div/nz-time-picker/div/input').send_keys(
            "20:00")
        sleep(5)
        # 点击确认按钮
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[3]/button[1]').click()

        # msg = self.login.driver.find_element(By.XPATH,
        #                                      '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[4]/nz-form-control/div[2]/div')
        # assert msg.text == excpet
        # print(msg.text)
        self.login.driver.quit()
