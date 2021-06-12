#!/usr/bin/python
#-*- coding:utf-8 -*-

from lib.mbmanage.requestmanage.base_req import BaseReq

__author__ = 'wangsong@mobike.com'


class GeoFencingConfigReq(BaseReq):

    # 添加地理围栏
    ADD_GEO_FENCING = "athena/config/geofencing/addGeoFencing.do"
    # 删除地理围栏
    DEL_GEO_FENCING = "athena/config/geofencing/delGeoFencing.do"
    # 编辑某个地理围栏
    UPDATE_GEO_FENCING = "athena/config/geofencing/updateGeoFencing.do"
    # 查询城市中图层的所有围栏（按照城市和类型查询）
    QUERY_GEO_FENCING = "athena/config/geofencing/queryGeoFencing.do"
    # 用户附近电子围栏显示接口
    QUERY = "api/v2/fencing/query.do"
    # 导入电子围栏
    COPY = "/athena/config/geofencing/copyGeoFencingInOneType.do"


    def __init__(self):
        super(GeoFencingConfigReq, self).__init__()
        self.header_dict = {"Content-Type": "application/json;charset=UTF-8"}

    def query_geo_fencing_req(self, json_data):
        '''
        查询城市中图层的所有围栏（按照城市和类型查询）
        :param json_data:
        :return:
        '''
        return self.request("POST", self.__class__.QUERY_GEO_FENCING, json_data=json_data, headers=self.header_dict)

    def update_geo_fencing_req(self, json_data):
        '''
        编辑地理围栏
        :param json_data:
        :return:
        '''
        return self.request("POST", self.__class__.UPDATE_GEO_FENCING, json_data=json_data, headers=self.header_dict)

    def add_geo_fencing_req(self, json_data):
        '''
        添加地理围栏
        :param json_data:
        :return:
        '''
        header_dict = {"Content-Type": "application/json;charset=UTF-8"}
        return self.request("POST", self.__class__.ADD_GEO_FENCING, json_data=json_data, headers=header_dict)

    def del_geo_fencing_req(self, json_data):
        '''
        删除地理围栏
        :param json_data:
        :return:
        '''
        header_dict = {"Content-Type": "application/json;charset=UTF-8"}
        return self.request("POST", self.__class__.DEL_GEO_FENCING, json_data=json_data, headers=header_dict)

    def query_req(self, header={}, params={}):
        '''
        用户附近电子围栏
        :param header:
        :param params:
        :return:
        '''
        return self.request("POST", self.__class__.QUERY, headers=header, params=params)