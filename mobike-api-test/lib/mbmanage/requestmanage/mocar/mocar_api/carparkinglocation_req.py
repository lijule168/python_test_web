#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class CarParkingLocationReq(BaseReq):
    def __init__(self):
        super(CarParkingLocationReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def list(self , param_dict=None):
        '''
        根据国家码和城市码获取停车场列表
        '''
        return self.request("POST", "parking/location/list", params=param_dict)

