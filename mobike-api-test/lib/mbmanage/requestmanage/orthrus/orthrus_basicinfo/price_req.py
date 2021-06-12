#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class PriceReq(BaseReq):
    def __init__(self):
        super(PriceReq, self).__init__(micro_service_name=MicroServiceName.ORTHRUS_BASICINFO)

    def querypricecondition(self , param_dict=None):
        '''
        根据条件获取票价
        '''
        return self.request("POST", "price/queryPriceCondition", params=param_dict)

    def getprice(self, header_dict, param_dict):
        '''
        获取票价
        '''
        return self.request("GET", "price/getPrice", params=param_dict, headers=header_dict)

    def addprice(self , param_dict=None):
        '''
        添加票价
        '''
        header_dict = {}
        header_dict["Content-Type"] = "application/json"
        return self.request("POST", "price/addPrice", headers=header_dict, json_data=param_dict)

    def updateprice(self , param_dict=None):
        '''
        修改票价
        '''
        return self.request("POST", "price/updatePrice", params=param_dict)

