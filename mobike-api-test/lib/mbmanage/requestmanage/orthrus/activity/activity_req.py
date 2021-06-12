#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
--------------------------------------
    date:   2018/3/19
--------------------------------------
    Change Date: 2018/3/19
    
"""
__author__ = "wangsong@mobike.com"

from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq


class ActivityReq(BaseReq):
    def __init__(self):
        super(ActivityReq, self).__init__()

    def get_discount(self, param_dict=None, header_dict=None):
        '''
        公交优惠信息获取接口
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("GET", "api/orthrus/orthrus-order/activity/getDiscount", params=param_dict, headers=header_dict)