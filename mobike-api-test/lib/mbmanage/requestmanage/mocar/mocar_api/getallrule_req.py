#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class GetAllRuleReq(BaseReq):
    def __init__(self):
        super(GetAllRuleReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def GetAllRule(self , param_dict=None):
        '''
        查看当前城市GetAllRule
        '''
        return self.request("POST", "chargingRule/getAllRule", params=param_dict)

