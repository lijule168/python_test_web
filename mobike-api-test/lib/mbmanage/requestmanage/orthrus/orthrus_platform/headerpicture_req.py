#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class HeaderPictureReq(BaseReq):
    def __init__(self):
        super(HeaderPictureReq, self).__init__(micro_service_name=MicroServiceName.ORTHRUS_PLATFORM)

    def getpicture(self, header_dict=None):
        '''
        Get Picture
        '''
        return self.request("GET", "picture/getPicture", headers=header_dict)

    def addpicture(self, json_dict=None):
        '''
        Add Picture
        '''
        return self.request("POST", "picture/addPicture", json_data=json_dict)

    def updatepicturestatus(self, json_dict=None):
        '''
        Update Picture Status
        '''
        return self.request("POST", "picture/updatePictureStatus", json_data=json_dict)

