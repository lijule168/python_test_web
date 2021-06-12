#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class StationReq(BaseReq):
    def __init__(self):
        super(StationReq, self).__init__(micro_service_name=MicroServiceName.ORTHRUS_BASICINFO)

    def querystations(self, header_dict, param_dict):
        '''
        查询站点信息
        '''
        return self.request("GET", "station/queryStations", headers=header_dict, params=param_dict)

    def deletestation(self ):
        '''
        删除站点
        '''
        return self.request("GET", "station/deleteStation/{id}")

    def querystationcondition(self , param_dict=None):
        '''
        获取站点
        '''
        return self.request("POST", "station/queryStationCondition", params=param_dict)

    def addstation(self , param_dict=None):
        '''
        添加站点
        '''
        header_dict = {"Content-Type": "application/json"}
        return self.request("POST", "station/addStation", json_data=param_dict, headers=header_dict)

    def checkstartstation(self, header_dict=None, param_dict=None):
        '''
        订单验证是否作为起始站点
        '''
        return self.request("GET", "station/checkStartStation", params=param_dict, headers=header_dict)

    def v2_querystationsbyname(self, param_dict=None, header_dict=None):
        '''
        模糊搜索
        '''
        return self.request("GET", "station/v2/queryStationsByName", params=param_dict, headers=header_dict)

    def checkStationByCode(self, header_dict=None, param_dict=None):
        '''
        根据百度station_code查询摩拜对应站点ID
        '''
        return self.request("POST", "station/checkStationByCode", params=param_dict, headers=header_dict)

