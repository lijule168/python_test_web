#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class BookingReq(BaseReq):
    def __init__(self):
        super(BookingReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def current(self , param_dict=None):
        '''
        当前预约 code:40011用户没有未完成预约
        '''
        return self.request("POST", "booking/current", params=param_dict)

    def todaycancelcount(self , param_dict=None):
        '''
        今天取消预约次数
        '''
        return self.request("POST", "booking/todayCancelCount", params=param_dict)

    def create(self , param_dict=None, header_dict=None):
        '''
        创建预约 code:40002车未运营,40011用户没有未完成预约40003用户有未完成预约,40006用户有未完成预约,40008用户未通过验证,40009用户未付押金40010车在行驶中,40012用户有未完成的订单
        '''
        return self.request("POST", "booking/create", params=param_dict, headers=header_dict)

    def cancel(self, param_dict=None):
        '''
        取消预约
        '''
        return self.request("POST", "booking/cancel", params=param_dict)

