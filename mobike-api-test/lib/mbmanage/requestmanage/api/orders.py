#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq

class OrdersReq(BaseReq):
    #骑行记录列表
    GET_RIDING_HISTORY = "api/v2/rentmgr/ridinghistory.do"

    def __init__(self):
        super(OrdersReq, self).__init__()

    def get_riding(self, param_dict={}, header_dict={}):
        '''
        骑行数据汇总
        :param param_dict:{userid:, times:timestamp}
        :return:
        '''
        return self.request("POST", "api/v2/rentmgr/getriding.do", params=param_dict, headers=header_dict)

    def get_ridinghistory(self, param_dict={}):
        '''
        骑行记录列表
        :param param_dict:{userid}
        :return:
        '''
        return self.request("POST", OrdersReq.GET_RIDING_HISTORY, params=param_dict)

    def query_riding_data(self, param_dict={}, header_dict={}):
        '''
        获取用户骑行相关基础信息
        :param param_dict:{userid}
        :return:
        '''
        return self.request("POST", "api/v2/rentmgr/queryridingdata.do", params=param_dict, headers=header_dict)