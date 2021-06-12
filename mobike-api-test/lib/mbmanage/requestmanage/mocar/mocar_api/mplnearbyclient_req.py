#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class MplNearbyClientReq(BaseReq):
    def __init__(self):
        super(MplNearbyClientReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def nearbympllist(self , param_dict=None):
        '''
        nearbyMPLList
        '''
        return self.request("POST", "nearby/nearbyMPLList", params=param_dict)

