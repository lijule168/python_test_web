#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class LineReq(BaseReq):
    def __init__(self):
        super(LineReq, self).__init__(micro_service_name=MicroServiceName.ORTHRUS_BASICINFO)

    def updateline(self , param_dict=None):
        '''
        修改线路
        '''
        return self.request("POST", "line/updateLine", params=param_dict)

    def addline(self , param_dict=None):
        '''
        添加线路
        '''
        return self.request("POST", "line/addLine", params=param_dict)

    def queryallline(self ):
        '''
        获取线路
        '''
        return self.request("GET", "line/queryAllLine")


    def deleteline(self, param_dict=None):
        '''
        删除线路
        '''
        return self.request("GET", "line/deleteLine/{id}", params=param_dict)

