#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class CarParkingDetailReq(BaseReq):
    def __init__(self):
        super(CarParkingDetailReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def get(self , param_dict=None):
        '''
        根据车场id获取车场详情
        '''
        return self.request("POST", "parking/detail/get", params=param_dict)

