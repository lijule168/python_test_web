#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangjieran'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName
from lib.util.log_util import l

class NearbyReq(BaseReq):

    NEARBYBIKESINFOV2 = "api/nearby/v2/nearbyBikeInfo"
    NEARBYBIKESINFOV3 = "api/nearby/v3/nearbyBikeInfo"

    def __init__(self):
        super(NearbyReq, self).__init__()

    def Nearby_Bikes_Info_req(self, param_dict, header_dict={}):
        '''
        获取附近车辆信息
        :param
        @RequestParam(value = "longitude", defaultValue = "0") double longitude,
                                          @RequestParam(value = "latitude", defaultValue = "0") double latitude,
                                          @RequestParam(value = "scope", defaultValue = "300") int scope,
                                          @RequestParam(value = "areacode", defaultValue = "") String areacode,
                                          @RequestParam(value = "biketype", defaultValue = "0") int biketype,
                                          @RequestParam(value = "coordinate", defaultValue = "") String coordinate,
                                          @RequestParam(value = "userid", defaultValue = "0") String userid
        :return:
        {
            "code": 0,
            "message": "",
           "biketype": 0,
           "object": [{
                "distId": "0109997198",
                "distX": 116.146819932726,
                "distY": 39.594865749783,
                "distNum": 1,
                "distance": "7",
                "bikeIds": "0109997198#",
                "biketype": 999,
                "type": 0,
                "boundary": null}
            ]
        }
        '''
        l.info("获取附近车辆信息")
        return self.request("POST", self.NEARBYBIKESINFOV3, params=param_dict, headers=header_dict)


