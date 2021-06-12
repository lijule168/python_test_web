#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangjieran'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName

class UserMgrReq(BaseReq):
    def __init__(self):
        super(UserMgrReq, self).__init__(micro_service_name=MicroServiceName.PARTNER)

    def send_coupon(self, param_dict=None, header_dict=None):
        '''
        第三方发券接口
        :return:
        '''
        return self.request("POST", "/mobike-api/usermgr/sendCoupon.do", params=param_dict, headers=header_dict)

