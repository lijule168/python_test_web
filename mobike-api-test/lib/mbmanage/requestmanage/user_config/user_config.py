#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.util.log_util import l


class UserConfigReq(BaseReq):
    USER_CONFIG_GET_MEDICIALADDRESS = "api/v2/api/user/medicinaladdress.do"
    USER_CONFIG_ADD_MEDICIALADDRESS = "api/v2/api/user/addmedicinaladdress.do"

    def __init__(self):
        super(UserConfigReq, self).__init__()

    def get_medicinaladdress(self, param_dict):
        '''
        获取用户地址信息
        :param param_dict: userid
        :return:
        '''
        l.info("获取用户地址信息")
        return self.request("GET", self.USER_CONFIG_GET_MEDICIALADDRESS, params=param_dict)

    def add_medicinaladdress(self, param_dict):
        '''
        添加用户地址信息
        :param param_dict:
            userid:
            position:1
            title:测试地址
            content:测试地址11111
            lat:
            lng:
        :return:
        '''
        l.info("添加用户地址信息")
        return self.request("GET", self.USER_CONFIG_ADD_MEDICIALADDRESS, params=param_dict)
