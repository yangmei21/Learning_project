import time

from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
from time import sleep

def test1():
    browser=webdriver.Chrome()
    browser.get("https://www.qb5.ch/login.php")
    browser.maximize_window()
    sleep(2)
    browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/form/fieldset/p[3]/img').click()
    sleep(3)

if __name__ == '__main__':
    test1()