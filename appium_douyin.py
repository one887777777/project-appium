#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 11:24 PM
# @Author  : Nikky
# @Site    :
# @File    : appium_douyin.py
import time
from appium import webdriver
from configs.configs import Configs


class DouyinSpider():

    def __init__(self):
        self.configs = Configs('douyin')
        self.driver = webdriver.Remote(self.configs.get_server(), self.configs.get_desired_caps())
        self.driver.implicitly_wait(5)

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_up(self):
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)
        self.driver.swipe(x1, y1, x1, y2, 500)

    def swipe_down(self):
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, 500)

    def login(driver):
        pass


if __name__ == '__main__':
    douyin = DouyinSpider()
    douyin.login()
    while True:
        time.sleep(5)
        douyin.swipe_up()
