#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 11:24 PM
# @Author  : Nikky
# @Site    :
# @File    : appium_chelun.py
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from configs.configs import Configs


class ChelunSpider():

    def __init__(self):
        self.configs = Configs('chelun')
        self.driver = webdriver.Remote(self.configs.get_server(), self.configs.get_desired_caps())
        self.driver.implicitly_wait(5)

    def query_violation(self):
        self.driver.find_element_by_id('cn.eclicks.wzsearch:id/into').click()
        self.driver.find_element_by_id('cn.eclicks.wzsearch:id/car_item_car_number').click()
        self.driver.find_element_by_id('cn.eclicks.wzsearch:id/textview_belong_province').click()
        self.driver.find_element_by_id('cn.eclicks.wzsearch:id/widget_belong_03').click()
        self.driver.find_element_by_id('cn.eclicks.wzsearch:id/edittext_car_plate').send_keys('CU87B3')
        self.driver.find_element_by_id('cn.eclicks.wzsearch:id/edittext_extra_info').send_keys('3930827')
        self.driver.find_element_by_id('cn.eclicks.wzsearch:id/checkbox_agree_protocol').click()
        self.driver.find_element_by_id('cn.eclicks.wzsearch:id/checkbox_privacy_agreement').click()
        self.driver.find_element_by_id('cn.eclicks.wzsearch:id/add_car_save').click()
        try:
            self.driver.find_element_by_id('cn.eclicks.wzsearch:id/common_dialog_negative_btn').click()
        except NoSuchElementException:
            pass


if __name__ == '__main__':
    chelun = ChelunSpider()
    chelun.query_violation()
