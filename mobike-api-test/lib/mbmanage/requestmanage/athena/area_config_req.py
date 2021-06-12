#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangjieran'

from lib.mbmanage.requestmanage.base_req import BaseReq

class AreaConfigReq(BaseReq):
    #城市相关配置
    OPENDAREA = "api/v2/api/opendarea.do"
    #添加开城信息
    ADDOPENDAREA = "api/v2/api/addopendarea.do"

    def __init__(self):
        super(AreaConfigReq, self).__init__()

    def opendarea(self, param_dict=None):
        '''
        获取开城列表
        :param json_data:
        :return:
        '''
        return self.request("GET", AreaConfigReq.OPENDAREA, params=param_dict)

    def addopendarea(self, param_dict=None):
        '''
        在开城列表中添加城市
        :param json_data:
        :return:
        '''
        return self.request("GET", AreaConfigReq.ADDOPENDAREA, params=param_dict)

