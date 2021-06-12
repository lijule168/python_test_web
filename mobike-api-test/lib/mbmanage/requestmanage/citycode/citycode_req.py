#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName
from lib.util.log_util import l

class CityCodeReq(BaseReq):
    # 根据经纬度解析国家的功能(全球国家)
    CITYCODE_QUERYCOUNTRY = "citycode/queryCountry"
    # 根据citycode查询城市信息的接口
    CITYCODE_GETBUSINESSAREABYCODE = "citycode/getBusinessAreaByCode"
    CITYCODE_GETCITYCODEBYLAN = "citycode/query"
    CITYCODE_PARSERBUSINESSAREA = "citycode/parseBusinessArea"
    CITYCODE_PARSERDISTINCT = "citycode/parse"

    def __init__(self):
        super(CityCodeReq, self).__init__(micro_service_name=MicroServiceName.CITY_CODE)

    def getCityCodeByLag(self, json_dict):
        '''
        根据经纬度获取citycode
        :param json_dict: {"lan":[0.0,0], "precision":5}
        :return:
        '''
        l.info("根据经纬度获取citycode")
        header_dict = {"Content-Type": "application/json"}
        return self.request("POST", CityCodeReq.CITYCODE_GETCITYCODEBYLAN, json_data=json_dict, headers=header_dict)

    def parseBusinessArea(self, json_dict):
        '''
        根据经纬度获取business ares信息
        :param json_dict: {"lan":[0.0,0], "precision":5}
        :return:
        '''
        l.info("根据经纬度获取business ares信息")
        header_dict = {"Content-Type": "application/json"}
        return self.request("POST", CityCodeReq.CITYCODE_PARSERBUSINESSAREA, json_data=json_dict, headers=header_dict)

    def queryCountry(self, json_dict):
        '''
        根据经纬度解析国家的功能(全球国家)
        :param json_dict: {"longitude":-77.1197663, "latitude":38.9342795}
        :return:
        '''
        l.info("根据经纬度解析国家的功能(全球国家)")
        header_dict = {"Content-Type": "application/json"}
        return self.request("POST", CityCodeReq.CITYCODE_QUERYCOUNTRY, json_data=json_dict, headers=header_dict)

    def getBusinessAreaByCode(self, param_dict):
        '''
        根据citycode查询城市信息的接口
        :param param_dict: {"cityCode":""}
        :return:
        '''
        return self.request("GET", CityCodeReq.CITYCODE_GETBUSINESSAREABYCODE, params=param_dict)

    def parseDistrict(self, json_dict):
        '''
        根据经纬度获取不同维度的district信息(COUNTRY, PROVINCE, CITY, COUNTRY, STREET)
        :param json_dict: {"lan":[0.0,0.0], "districtLevelEnum":""}
            districtLevelEnum:值如下
            COUNTRY,
            PROVINCE,
            CITY,
            COUNTY,
            STREET
        :return:
        '''
        header_dict = {"Content-Type": "application/json"}
        return self.request("POST", CityCodeReq.CITYCODE_PARSERDISTINCT, json_data=json_dict, headers=header_dict)
