#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class DriverOrderReq(BaseReq):
    def __init__(self):
        super(DriverOrderReq, self).__init__()

    def _order(self, param_dict=None, header_dict=None):
        '''
        查询订单详情
        '''
        return self.request("GET", "api/chariot-nfs/order", params=param_dict, headers=header_dict)

    def order_cancel(self, param_dict=None, header_dict=None):
        '''
        司机取消订单
        '''
        return self.request("POST", "api/chariot-nfs/order/cancel", params=param_dict, headers=header_dict)

    def order_dispatch(self, param_dict=None, header_dict=None):
        '''
        获取司机派单
        '''
        return self.request("GET", "api/chariot-nfs/order/dispatch", params=param_dict, headers=header_dict)

    def order_fight(self, param_dict=None, header_dict=None):
        '''
        司机抢单
        '''
        return self.request("POST", "api/chariot-nfs/order/fight", params=param_dict, headers=header_dict)

    def order_list(self, param_dict=None, header_dict=None):
        '''
        查询司机订单列表
        '''
        return self.request("GET", "api/chariot-nfs/order/list", params=param_dict, headers=header_dict)

    def order_status(self, param_dict=None, header_dict=None):
        '''
        查询订单状态
        '''
        return self.request("GET", "api/chariot-nfs/order/status", params=param_dict, headers=header_dict)

