#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia@mobike.com'

from lib.mbmanage.requestmanage.base_req import BaseReq

class ApiConfigReq(BaseReq):
    #拉取配置
    V1_CONFIG = "api/v2/api/config/v1.do"


    def __init__(self):
        super(ApiConfigReq, self).__init__()

    def v1(self, param_dict={}):
        '''
        读取配置信息
        :param param_dict:
        :return:
        '''
        return self.request("GET", self.__class__.V1_CONFIG, params=param_dict)
