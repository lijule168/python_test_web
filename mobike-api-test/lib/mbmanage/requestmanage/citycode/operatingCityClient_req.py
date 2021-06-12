#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'i-dingliu@mobike.com'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName
# from lib.util.log_util import l

class OperatingCityClientReq(BaseReq):
    OperatingCityClient_getAll = "operatingcity/getall"
    OperatingCityClient_getByCountryCode = "operatingcity/getbycountrycode"
    OperatingCityClient_getByCityCode = "operatingcity/getbycitycode"
    OperatingCityUpdateClient_insert = "operatingcity/insert"
    OperatingCityUpdateClient_updateById = "operatingcity/update"
    OperatingCityUpdateClient_deleteByCityCode = "operatingcity/delete"

    def __init__(self):
        super(OperatingCityClientReq, self).__init__(micro_service_name=MicroServiceName.CITY_CODE)

    def getAll(self, param_dict=None):
        '''
        获取所有城市信息
        :return:
        '''
        # l.info("获取所有城市信息")
        return self.request("GET", OperatingCityClientReq.OperatingCityClient_getAll, params=param_dict)

    def getByCountryCode(self, param_dict=None):
        '''
        根据countryCode获取对应的所有城市信息
        :param :countryCode
        :return:所有符合要求的城市信息
        '''
        # l.info("根据countryCode获取对应的所有城市信息")
        return self.request("GET", OperatingCityClientReq.OperatingCityClient_getByCountryCode, params=param_dict)

    def getByCityCode(self, param_dict=None):
        '''
        根据cityCode获取对应的城市信息
        :param :cityCode
        :return:对应的城市信息
        '''
        # l.info("根据countryCode获取对应的城市信息")
        return self.request("GET", OperatingCityClientReq.OperatingCityClient_getByCityCode, params=param_dict)

    def insert(self, json_dict):
        '''
        新增城市
        :param json_dict: {
                            "cityCode": "",
                            "cityName": "",
                            "provinceName": "",
                            "countryCode": ,
                            "countryName": "",
                            "status": ,
                            "operator": "",
                            "createTime": ,
                            "updateTime": ,
                            "bikeids": ""
                            }
        :return:boolean
        '''
        header_dict = {"Content-Type": "application/json"}
        return self.request("POST", OperatingCityClientReq.OperatingCityUpdateClient_insert, json_data=json_dict, headers=header_dict)

    def updateById(self, json_dict):
        '''
        根据id修改城市信息
        :param json_dict: {
                            "id":"",
                            "cityCode": "",
                            "cityName": "",
                            "provinceName": "",
                            "countryCode": ,
                            "countryName": "",
                            "status": ,
                            "operator": "",
                            "createTime": ,
                            "updateTime": ,
                            "bikeids": ""
                            }
        :return:boolean
        '''
        header_dict = {"Content-Type": "application/json"}
        return self.request("POST", OperatingCityClientReq.OperatingCityUpdateClient_updateById, json_data=json_dict,
                            headers=header_dict)

    def deleteByCityCode(self, param_dict=None):
        '''
        根据countryCode删除对应的城市信息
        :param :cityCode
        :return:boolean
        '''
        return self.request("GET", OperatingCityClientReq.OperatingCityUpdateClient_deleteByCityCode, params=param_dict)


