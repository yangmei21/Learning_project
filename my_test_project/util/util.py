import pickle
import random
import string
import time
from PIL import Image
import os

from pytesseract import pytesseract
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# 获取验证码
def get_code(driver, id):
    t = time.time()
    path = os.path.dirname(os.path.dirname(__file__)) + '\\screenshots'
    picture_name1 = path + '\\' + str(t) + '.png'
    WebDriverWait(driver, 10, 0.5).until(
        lambda el: driver.find_element(By.XPATH, id))
    driver.find_element(By.XPATH, id).screenshot(picture_name1)
    imagel = Image.open(picture_name1)
    str1 = pytesseract.image_to_string(imagel)
    code = int(str1)
    return code


# 随机生成字符串
def gen_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str


# 保存cookie
def save_coolie(driver, path):
    with open(path, 'wb') as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump(cookies, filehandler)

# 加载cookie
def load_cookie(driver,path):
    with open(path,'rb')as cookiesfile:
        cookies=pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)
