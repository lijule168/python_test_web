#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

# code generate by tools, any problem please contact dingbaixia@mobike.com


class DriverTripReq(BaseReq):
    def __init__(self):
        super(DriverTripReq, self).__init__()

    def trip_arrived(self, param_dict=None, header_dict=None):
        '''
        到达终点
        '''
        return self.request("POST", "api/chariot-nfs/trip/arrived", params=param_dict, headers=header_dict)

    def trip_pay(self, param_dict=None, header_dict=None):
        '''
        司机发起收款
        '''
        return self.request("POST", "api/chariot-nfs/trip/pay", params=param_dict, headers=header_dict)

    def pay_offline(self, param_dict=None, header_dict=None):
        '''
        司机线下收款
        '''
        return self.request("POST", "api/chariot-nfs/trip/pay/offline", params=param_dict, headers=header_dict)

    def trip_ready(self, param_dict=None, header_dict=None):
        '''
        司机到达乘客位置
        '''
        return self.request("POST", "api/chariot-nfs/trip/ready", params=param_dict, headers=header_dict)

    def trip_setoff(self, param_dict=None, header_dict=None):
        '''
        司机出发
        '''
        return self.request("POST", "api/chariot-nfs/trip/setoff", params=param_dict, headers=header_dict)

    def trip_start(self, param_dict=None, header_dict=None):
        '''
        行程开始
        '''
        return self.request("POST", "api/chariot-nfs/trip/start", params=param_dict, headers=header_dict)

    def trip_track(self, param_dict=None):
        '''
        行程上报
        '''
        return self.request("POST", "api/chariot-nfs/trip/track", params=param_dict)

