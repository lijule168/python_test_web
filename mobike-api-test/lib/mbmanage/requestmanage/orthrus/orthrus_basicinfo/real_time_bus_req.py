#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

"""
--------------------------------------
    date:   2018/3/20
--------------------------------------
    Change Date: 2018/3/20
    
"""
__author__ = "wangsong@mobike.com"


class RealTimeBusReq(BaseReq):
    '''
    实时公交
    '''
    def __init__(self):
        super(RealTimeBusReq, self).__init__()

    def get_line_info(self, param_dict, header_dict):
        '''
        通过applicationId、线路id、经纬度获取线路的详细信息
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST", "api/orthrus/orthrus-basicinfo/realTimeBus/getLineInfo", params=param_dict,
                            headers=header_dict)

    def search_lines_by_station(self, param_dict, header_dict):
        '''
        通过applicationId、站点id、关键字搜索该站点下的线路信息。
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST", "api/orthrus/orthrus-basicinfo/realTimeBus/searchLinesByStation", params=param_dict,
                            headers=header_dict)

    def get_station_info(self, param_dict, header_dict):
        '''
        通过applicationId、站点id获取站点信息，包含该站点的相关线路信息。
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST", "api/orthrus/orthrus-basicinfo/realTimeBus/getStationInfo", params=param_dict,
                            headers=header_dict)

    def search_nearby_stations(self, param_dict, header_dict):
        '''
        通过关键字搜索附近的站点信息，包含该站点的相关线路信息
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST", "api/orthrus/orthrus-basicinfo/realTimeBus/searchNearbyStations", params=param_dict,
                            headers=header_dict)

    def get_nearby_station(self, param_dict, header_dict):
        '''
        查询附近站点及线路情况
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST", "api/orthrus/orthrus-basicinfo/realTimeBus/getNearbyStation", params=param_dict,
                            headers=header_dict)

    def query_all_nearby_stations(self, param_dict, header_dict):
        '''
        通过applicationId、经纬度坐标查询附近的站点信息，包含该站点的相关线路信息。如果3KM内无附近站点，则显示该城市所有站点信息。
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST", "api/orthrus/orthrus-basicinfo/realTimeBus/queryAllNearbyStations", params=param_dict,
                            headers=header_dict)

