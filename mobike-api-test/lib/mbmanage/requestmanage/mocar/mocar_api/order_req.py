#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class OrderReq(BaseReq):
    def __init__(self):
        super(OrderReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def current(self , param_dict=None):
        '''
        当前进行中订单-客户端轮询 code40007订单不存在
        '''
        return self.request("POST", "order/current", params=param_dict)

    def lockandendorder(self , param_dict=None):
        '''
        结束订单 40007订单不存在 40015订单状态错误 40016不允许锁车 40017定位附近没有还车点
        '''
        return self.request("POST", "order/lockAndEndOrder", params=param_dict)

    def createorder(self , param_dict=None, header_dict=None):
        '''
        用户开锁创建订单
        '''
        return self.request("POST", "order/createOrder", params=param_dict, headers=header_dict)

    def list(self , param_dict=None):
        '''
        用户订单列表
        '''
        return self.request("POST", "order/list", params=param_dict)

    def islockable(self , param_dict=None,header_dict=None):
        '''
        是否可以锁车 40007订单不存在 40015订单状态错误 40017定位附近没有还车点
        '''
        return self.request("POST", "order/isLockable", params=param_dict,headers=header_dict)

    def detail(self, param_dict=None):
        '''
        订单详情 code40007订单不存在
        '''
        return self.request("POST", "order/detail", params=param_dict)

