#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 11:24 PM
# @Author  : Nikky
# @Site    :
# @File    : appium_taobao.py
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from configs.configs import Configs

class TaobaoSpider():

    def __init__(self):
        self.configs = Configs('taobao')
        self.driver = webdriver.Remote(self.configs.get_server(), self.configs.get_desired_caps())
        self.driver.implicitly_wait(5)

    def login(self):
        try:
            self.driver.find_element_by_id('com.taobao.taobao:id/yes').click()
        except NoSuchElementException:
            pass
        self.driver.find_element_by_xpath('//android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.FrameLayout[4]/android.widget.ImageView').click()
        self.driver.find_element_by_id('com.taobao.taobao:id/aliuser_login_switch_pwdlogin').click()
        self.driver.find_element_by_id('com.taobao.taobao:id/aliuser_login_account_et').clear()
        self.driver.find_element_by_id('com.taobao.taobao:id/aliuser_login_account_et').send_keys(self.configs.get_username())
        self.driver.find_element_by_id('com.taobao.taobao:id/aliuser_login_password_et').clear()
        self.driver.find_element_by_id('com.taobao.taobao:id/aliuser_login_password_et').send_keys(self.configs.get_password())
        self.driver.find_element_by_id('com.taobao.taobao:id/aliuser_login_login_btn').click()
        self.driver.find_element_by_xpath('//android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.FrameLayout[1]/android.widget.ImageView').click()
        try:
            self.driver.find_element_by_id('com.taobao.taobao:id/uik_mdButtonDefaultPositive').click()
        except NoSuchElementException:
            pass

    def search_shop(self, name):
        self.driver.find_element_by_id('com.taobao.taobao:id/home_searchedit').clear()


if __name__ == '__main__':
    taobao = TaobaoSpider()
    taobao.login()
    name = '发财树'
    taobao.search_shop(name)
