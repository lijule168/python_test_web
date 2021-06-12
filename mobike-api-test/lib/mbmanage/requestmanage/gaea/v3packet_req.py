#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName
from lib.util.log_util import l

class V3PackageReq(BaseReq):
    #根据用户可信度,过滤红包缓存
    FILER_REDPACKETV3WITHUSERID = "gaea/filterRedPacketV3WithUserId"
    #批量获取红包类型
    BATCH_GETREDPACKETTYPE = "gaea/batchGetRedPacketType"
    #根据用户来获取红包类型
    BATCH_GETREDPACKETTYPE_WITH_USERID = "gaea/batchGetRedPacketTypeWithUserId"
    #获取红包金额
    GET_REDPACKET = "gaea/giveRedPacket"
    #获取红包车类型接口
    GET_REDPACKET_TYPE = "gaea/getRedPacketType"
    # 根查询附近的停车点
    SERARCH_NEARBY_PARKINGPLACE = "gaea/nearbyRedPacketParkingPlace"
    #清除停车点缓存
    CLEAR_PARKINGPLACERECORDS_CACHE_WITH_USERID = "gaea/delShowedParkingPlaceRecords"
    #根据场景获取红包金额
    GIVE_REDPACKETWITH_SCENE = "gaea/giveRedPacketWithScene"

    def __init__(self):
        super(V3PackageReq, self).__init__(micro_service_name=MicroServiceName.GAEA)

    def filter_redpacketv3_with_userid(self, param_dict, json_dict):
        '''
        根据用户可信度,过滤红包缓存
        :param param_dict: key:cityCode, userId, longitude, latitude, radius, platform, version
        :param json_dict: bikes
        :return:
        '''
        header_dict = {"Content-Type":"application/json"}
        api_path = V3PackageReq.FILER_REDPACKETV3WITHUSERID + "?" + self._format_jsonreq_path(param_dict=param_dict)
        return self.request("POST", api_path=api_path, headers=header_dict, json_data=json_dict)

    def batch_getredpackettype(self, param_dict, json_dict):
        '''
        批量获取红包类型
        :param param_dict: key:cityCode, platform, longitude, latitude, radius, version
        :param json_dict: bikes
        :return:
        '''
        header_dict = {"Content-Type": "application/json"}
        api_path = V3PackageReq.BATCH_GETREDPACKETTYPE + "?" + self._format_jsonreq_path(param_dict=param_dict)
        return self.request("POST", api_path=api_path, headers=header_dict, json_data=json_dict)

    def batch_getredpackettype_with_userid(self, param_dict, json_dict):
        '''
        根据用户来获取红包类型
        :param param_dict: key:cityCode, userId, platform, longitude, latitude, version
        :param json_dict: bikes
        :return:
        '''
        header_dict = {"Content-Type": "application/json"}
        api_path = V3PackageReq.BATCH_GETREDPACKETTYPE_WITH_USERID + "?" + self._format_jsonreq_path(param_dict=param_dict)
        return self.request("POST", api_path=api_path, headers=header_dict, json_data=json_dict)

    def get_redpackettype(self, param_dict, json_dict):
        '''
        获取红包车类型接口
        :param param_dict: key:cityCode, userId, platform, longitude, latitude, version
        :param json_dict: bikes
        :return:
        '''
        header_dict = {"Content-Type": "application/json"}
        api_path = V3PackageReq.GET_REDPACKET_TYPE + "?" + self._format_jsonreq_path(param_dict=param_dict)
        return self.request("POST", api_path=api_path, headers=header_dict, json_data=json_dict)

    def give_redpacket(self, param_dict):
        '''
        获取红包金额
        :param param_dict: key:cityCode, userId, userLongitude, userLatitude, bikeLongitude, bikeLatitude
        :return:
        '''
        return self.request("POST", V3PackageReq.GET_REDPACKET,params=param_dict)

    def nearby_parkingplace(self, param_dict=None):
        '''
        根查询附近的停车点
        :param param_dict: key:userId, longitude, latitude, radius, type
        :return:
        '''
        return self.request("GET", api_path=V3PackageReq.SERARCH_NEARBY_PARKINGPLACE, params=param_dict)

    def delShowedParkingPlaceRecords(self, param_dict={}):
        '''
        清除停车点缓存
        :param param_dict:
        :return:
        '''
        return self.request("GET", api_path=V3PackageReq.CLEAR_PARKINGPLACERECORDS_CACHE_WITH_USERID, params=param_dict)

    def giveRedPacketWithScene(self, param_dict):
        '''
        获取红包金额
        :param param_dict: key:cityCode, userId, userLongitude, userLatitude, bikeLongitude, bikeLatitude, orderId, orderEndTime, scene
        :return:
        '''
        return self.request("POST", V3PackageReq.GIVE_REDPACKETWITH_SCENE,params=param_dict)
