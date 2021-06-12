#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class IafcReq(BaseReq):
    def __init__(self):
        super(IafcReq, self).__init__(micro_service_name=MicroServiceName.ORTHRUS_BASICINFO)

    def login(self , param_dict=None):
        '''
        do login
        '''
        return self.request("GET", "iafc/login", params=param_dict)

    def getapplications(self , param_dict=None):
        '''
        Get Applications
        '''
        return self.request("GET", "iafc/getApplications", params=param_dict)

