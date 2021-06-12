#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class OrderReq(BaseReq):
    def __init__(self):
        super(OrderReq, self).__init__(micro_service_name=MicroServiceName.ORTHRUS_ORDER)

    def submitorder(self, header_dict=None, param_dict=None):
        '''
        创建订单
        '''
        if header_dict is None:
            header_dict = {}
        #header_dict["Content-Type"] = "application/json"
        return self.request("POST", "order/submitOrder", headers=header_dict, params=param_dict)

    def getticketcode(self, header_dict=None, param_dict=None):
        '''
        查询取票码
        '''
        return self.request("GET", "order/getTicketCode", headers=header_dict, params=param_dict)

    def getorderinfo(self, header_dict=None, param_dict=None):
        '''
        查询订单详细信息
        '''
        return self.request("GET", "order/getOrderInfo", headers=header_dict, params=param_dict)

    def notifyusecallback(self , param_dict=None):
        '''
        接收取票码被使用通知
        '''
        return self.request("GET", "order/notifyUseCallback", params=param_dict)

    def submitactivity(self , param_dict=None):
        '''
        创建订单活动
        '''
        return self.request("POST", "order/submitActivity", params=param_dict)

    def querystartstationhistory(self, header_dict=None, param_dict=None):
        '''
        获取首站历史记录接口
        '''
        return self.request("GET", "order/queryStartStationHistory", headers=header_dict, params=param_dict)

    def refund(self, param_dict=None, header_dict=None):
        '''
        取消订单
        '''
        return self.request("POST", "order/refund", params=param_dict, headers=header_dict)

    def queryorderinfo(self,header_dict=None, param_dict=None):
        '''
        获取订单分页接口
        '''
        return self.request("GET", "order/queryOrderInfo", headers=header_dict, params=param_dict)

    def queryendstationhistory(self, header_dict=None, param_dict=None):
        '''
        获取末站历史记录接口
        '''
        return self.request("GET", "order/queryEndStationHistory", headers=header_dict, params=param_dict)

    def getactivity(self , param_dict=None):
        '''
        活动查询接口
        '''
        return self.request("GET", "order/getActivity", params=param_dict)

    def getorderstatus(self,header_dict=None, param_dict=None):
        '''
        获取订单状态
        '''
        return self.request("GET", "order/getOrderStatus", headers=header_dict, params=param_dict)

    def use_pay_callback(self, header_dict=None, json_date=None):
        '''
        第三方回调接口，供第三方回调通知取票码状态
        :param header_dict:
        :param param_dict:
        :return:
        '''
        header_dict['Content-Type'] = "application/json"
        return self.request("POST", "order/zhanjuan/usePayCallBack", headers=header_dict, json_data=json_date)
