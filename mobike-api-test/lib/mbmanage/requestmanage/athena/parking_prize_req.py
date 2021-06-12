# /usr/bin/python
# -*- coding:utf-8 -*-

from lib.mbmanage.requestmanage.base_req import BaseReq

__author__ = 'wenzhiguo'


class ParkingPrizeReq(BaseReq):
    # POI组新建
    ADD_POIGROUP_PARKINGPRIZE = "athena/hermes/config/poigroup/add"
    # POI组查询
    LIST_POIGTOUP_PARKINGPRIZE = "athena/hermes/config/poigroup/list"
    # POI子集新建
    ADD_POI_PARKINGPRIZE = "athena/hermes/config/poi/add"
    # POI组删除
    DELETE_POIGROUP_PARKINGPRIZE = "athena/hermes/config/poigroup/delete"
    # poi子集点亮
    LIGHTING_POI_PARKINGPRIZE = "athena/hermes/config/activity/add"

    def __init__(self):
        # 停车有奖
        super(ParkingPrizeReq, self).__init__()

    def add_poigroup_parking_prize_req(self, json_data=None):
        '''
        POI组新建
        :param header_dict:
        :param param_diact:
        :return:
        '''
        header_dict = {"Content-Type": "application/json;charset=UTF-8"}
        return self.request("POST", self.__class__.ADD_POIGROUP_PARKINGPRIZE, headers=header_dict, json_data=json_data)

    def list_poigroup_parking_prize_req(self, header_dict=None, param_diact=None):
        '''
        POI组查询
        :param header_dict:
        :param param_diact:
        :return:
        '''
        return self.request("GET", self.__class__.LIST_POIGTOUP_PARKINGPRIZE, headers=header_dict, params=param_diact)

    def add_poi_parking_prize_req(self, json_data=None):
        '''
        POI子集新建
        :param header_dict:
        :param param_diact:
        :return:
        '''
        header_dict = {"Content-Type": "application/json;charset=UTF-8"}
        return self.request("POST", self.__class__.ADD_POI_PARKINGPRIZE, headers=header_dict, json_data=json_data)

    def delete_poigroup_parking_prize_req(self, header_dict=None, param_diact=None):
        '''
        POI组删除
        :param header_dict:
        :param param_diact:
        :return:
        '''
        return self.request("POST", self.__class__.DELETE_POIGROUP_PARKINGPRIZE, headers=header_dict, params=param_diact)

    def lighting_poi_parking_prize_req(self, json_data=None, param_dict=None):
        '''
        POI子集点亮
        :param header_dict:
        :param param_diact:
        :return:
        '''
        header_dict = {"Content-Type": "application/json;charset=UTF-8"}
        return self.request("POST", self.__class__.LIGHTING_POI_PARKINGPRIZE, headers=header_dict, json_data=json_data,params=param_dict)
