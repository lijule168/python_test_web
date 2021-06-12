#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class Softlockreq(BaseReq):
    def __init__(self):
        super(Softlockreq, self).__init__(micro_service_name=MicroServiceName.MOCAR_INTERNAL_API)

    def unlock(self , param_dict=None):
        '''
        解锁
        '''
        return self.request("POST", "vlock/unlock", params=param_dict)

    def lock(self, param_dict=None):
        '''
        关锁
        '''
        return self.request("POST", "vlock/lock", params=param_dict)