#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class OpenCityReq(BaseReq):
    def __init__(self):
        super(OpenCityReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def list(self , param_dict=None):
        '''
        获取电动车合作城市
        '''
        return self.request("POST", "opencity/list", params=param_dict)

