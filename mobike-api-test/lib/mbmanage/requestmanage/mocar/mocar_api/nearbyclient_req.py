#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class NearbyClientReq(BaseReq):
    def __init__(self):
        super(NearbyClientReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def nearbyonriding(self , param_dict=None):
        '''
        nearbyOnRiding
        '''
        return self.request("POST", "nearby/nearbyOnRiding", params=param_dict)

    def mutiple(self , param_dict=None):
        '''
        store
        '''
        return self.request("POST", "nearby/store/mutiple", params=param_dict)

    def simple(self , param_dict=None):
        '''
        store
        '''
        return self.request("POST", "nearby/store/simple", params=param_dict)

    def nearbybikeinfo(self , param_dict=None):
        '''
        nearbyBikesInfoAndMPL
        '''
        return self.request("POST", "nearby/v2/nearbyBikeInfo", params=param_dict)

