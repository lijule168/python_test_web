#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class CarCommandReq(BaseReq):
    def __init__(self):
        super(CarCommandReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def doubleflash(self , param_dict=None):
        '''
        双闪 code4004不可以控制车
        '''
        return self.request("POST", "command/doubleFlash", params=param_dict)

    def lock(self , param_dict=None):
        '''
        临时停车-锁车 code4004不可以控制车
        '''
        return self.request("POST", "command/lock", params=param_dict)

    def unlock(self , param_dict=None):
        '''
        临时停车-开锁 code4004不可以控制车
        '''
        return self.request("POST", "command/unlock", params=param_dict)

    def ringbell(self , param_dict=None):
        '''
        响铃 code4004不可以控制车
        '''
        return self.request("POST", "command/ringBell", params=param_dict)

