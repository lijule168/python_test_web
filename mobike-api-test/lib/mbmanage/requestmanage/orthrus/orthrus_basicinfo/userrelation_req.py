#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class UserRelationReq(BaseReq):
    def __init__(self):
        super(UserRelationReq, self).__init__(micro_service_name=MicroServiceName.ORTHRUS_BASICINFO)

    def querydatafororder(self ):
        '''
        为订单提供查询接口
        '''
        return self.request("GET", "userRelation/queryDataForOrder")

    def adduserrelation(self, param_dict=None):
        '''
        添加用户关系线路
        '''
        header_dict = {}
        #header_dict["Content-Type"] = "application/json"
        return self.request("POST", "userRelation/addUserRelation", headers=header_dict, params=param_dict)

