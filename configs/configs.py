#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 6:22 PM
# @Author  : Nikky
# @Site    : 
# @File    : configs.py
import yaml


class Configs:

    def __init__(self, name='taobao', dir='./configs/configs.yaml'):
        file = open(dir, 'r')
        self.data = yaml.load(file).get(name)

    def get_desired_caps(cls):
        '''
        获取 desired_caps
        :return:
        '''
        return cls.data.get('desired_caps')
        # return json.dumps(cls.data.get('desired_caps'))

    def get_username(cls):
        '''
        获取 get_username
        :return:
        '''
        return cls.data.get('username')

    def get_password(cls):
        '''
        获取 get_password
        :return:
        '''
        return cls.data.get('password')

    def get_server(cls):
        '''
        获取 get_server
        :return:
        '''
        return cls.data.get('server')


if __name__ == '__main__':
    configs = Configs('taobao', './configs.yaml')
    print(configs.get_desired_caps())
