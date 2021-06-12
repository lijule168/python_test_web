#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class InitStateReq(BaseReq):
    def __init__(self):
        super(InitStateReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def current(self , param_dict=None):
        '''
        当前状态未完成的订单预约
        '''
        return self.request("POST", "initState/current", params=param_dict)

