#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class GatewayReq(BaseReq):
    def __init__(self):
        super(GatewayReq, self).__init__()

    def submitorder(self , header_dict=None, param_dict=None):
        '''
        创建订单
        '''
        if header_dict is None:
            header_dict = {}
        #header_dict["Content-Type"] = "application/json"
        return self.request("POST", "api/orthrus/orthrus-order/order/submitOrder", headers=header_dict, params=param_dict)

    def getPrice(self , header_dict=None, param_dict=None):
        '''
        获取价格
        '''
        if header_dict is None:
            header_dict = {}
        #header_dict["Content-Type"] = "application/json"
        return self.request("GET", "api/orthrus/orthrus-basicinfo/price/getPrice.do", headers=header_dict, params=param_dict)