#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com


class TripTaxiReq(BaseReq):
    def __init__(self):
        super(TripTaxiReq, self).__init__()

    def taxi_create(self, param_dict={}, header_dict={}):
        '''
        下单
        '''
        return self.request("POST", "api/chariot/trip/taxi/create", params=param_dict, headers=header_dict)

    def taxi_feedback(self, param_dict=None):
        '''
        评价司机
        '''
        return self.request("POST", "api/chariot/trip/taxi/feedback", params=param_dict)

    def taxi_pay(self, param_dict=None):
        '''
        支付
        '''
        return self.request("POST", "api/chariot/trip/taxi/pay", params=param_dict)

    def taxi_pay4pickup(self, param_dict=None, header_dict={}):
        '''
        打表来接
        '''
        return self.request("POST", "api/chariot/trip/taxi/pay4pickup", params=param_dict, headers=header_dict)

    def taxi_price(self, param_dict=None, header_dict=None):
        '''
        估价
        '''
        return self.request("POST", "api/chariot/trip/taxi/price", params=param_dict, headers=header_dict)

    def taxi_thanksfee(self, param_dict=None, header_dict=None):
        '''
        增加调度费
        '''
        return self.request("POST", "api/chariot/trip/taxi/thanksfee", params=param_dict, headers=header_dict)

