#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class PlatformReq(BaseReq):
    def __init__(self):
        super(PlatformReq, self).__init__(micro_service_name=MicroServiceName.ORTHRUS_PLATFORM)

    def getopencities(self , param_dict=None):
        '''
        Get open cities in this country by cityCode or location (longitude, latitude)
        '''
        return self.request("GET", "platform/getOpenCities", params=param_dict)

    def getapplications(self , param_dict=None):
        '''
        Get applications by cityCode or location (longitude, latitude)
        '''
        return self.request("GET", "platform/v2/getApplications", params=param_dict)

