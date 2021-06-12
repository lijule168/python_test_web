#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

# code generate by tools, any problem please contact dingbaixia@mobike.com


class DriverServiceReq(BaseReq):
    def __init__(self):
        super(DriverServiceReq, self).__init__()

    def driver_report(self, param_dict=None, header_dict=None):
        '''
        司机状态上报，需先调用/service/await接口
        '''
        return self.request("POST", "api/chariot-nfs/driver/report", params=param_dict, headers=header_dict)

    def service_await(self, param_dict=None, header_dict=None):
        '''
        司机出车，开始听单
        '''
        return self.request("POST", "api/chariot-nfs/service/await", params=param_dict, headers=header_dict)

    def service_config(self, param_dict=None, header_dict=None):
        '''
        司机听单配置
        '''
        return self.request("POST", "api/chariot-nfs/service/config", params=param_dict, headers=header_dict)

    def service_rest(self, param_dict=None, header_dict=None):
        '''
        司机停止听单
        '''
        return self.request("POST", "api/chariot-nfs/service/rest", params=param_dict, headers=header_dict)

    def service_status(self, param_dict=None, header_dict=None):
        '''
        查询司机服务状态
        '''
        return self.request("GET", "api/chariot-nfs/service/status", params=param_dict, headers=header_dict)

