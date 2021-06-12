#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'yys'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName
from lib.util.log_util import l

class ChariotReq(BaseReq):


    #H5界面投诉行程费用
    TRIP_ADDCOMPLAINT = "api/chariot/trip/addComplaint"
    #取消订单
    TRIP_CANCEL = "api/chariot/trip/cancel"
    #取消订单费用查询
    TRIP_CANCEL_QUERY = "api/chariot/trip/cancel/query"
    #创建订单
    TRIP_CREATION = "api/chariot/trip/creation"
    #订单详情轮询
    TRIP_DETAIL = "api/chariot/trip/detail"
    #司机位置查询
    TRIP_DRIVER_LOCATION = "api/chariot/trip/driver/location"
    #估价
    TRIP_ESTIMATION = "api/chariot/trip/estimation"
    #获取专车行程列表
    TRIP_LIST = "api/chariot/trip/list"
    #订单状态查询
    TRIP_STATUS = "api/chariot/trip/status"
    #获取行程中的订单
    TRIP_TRAVELLING =  "api/chariot/trip/travelling"

    def __init__(self):
        super(ChariotReq, self).__init__()

    def get_trip_addcomplaim(self, param_dict={}):
        '''
        H5界面投诉行程费用
        @RequestParam("orderId") String orderId,
        @RequestParam("complaintContent") int complaintContent,
        @RequestParam(value = "remarks",defaultValue = ""
        '''
        return self.request("POST", ChariotReq.TRIP_ADDCOMPLAINT, params=param_dict)
    def trip_cancel(self, param_dict = {}, header_dict ={}):
        '''
        取消订单
        :param header_dict: orderId
        :param param_dict:key:accesstoken
        :return:
        '''
        return self.request("POST", ChariotReq.TRIP_CANCEL, params=param_dict, headers=header_dict)

    def trip_cancel_query(self, param_dict={},header_dict={}):
        '''
        取消订单查询
        :param header_dict: 
        :param param_dict:key:orderId
        :return:
        '''
        return self.request("POST", ChariotReq.TRIP_CANCEL_QUERY, params=param_dict,headers=header_dict)
    def trip_creation(self, param_dict={}, header_dict={}):
        '''
        创建订单
        :param header_dict: citycode,version,os,platform
        :param param_dict:key:
        :return:
        '''
        return self.request("POST", ChariotReq.TRIP_CREATION, params=param_dict, headers=header_dict)
    def get_trip_detail(self, param_dict={}, header_dict={}):
        """
        #订单详情轮询
        :param param_dict: 
        :type header_dict: key;userId
        :return:
        """
        return self.request("POST", ChariotReq.TRIP_DETAIL, params=param_dict, headers=header_dict)
    def trip_driver_location(self,param_dict={}, header_dict={}):
        """
            #司机位置查询
            :param param_dict: 
            :type header_dict: key;userId
            :return:
        """
        return self.request("POST", ChariotReq.TRIP_DRIVER_LOCATION, params=param_dict, headers=header_dict)
    def trip_estimation(self,param_dict={},header_dict={}):
        """
            #估价
            :param param_dict: 
            :type header_dict: key;userId
            :return:
        """
        return self.request("POST", ChariotReq.TRIP_ESTIMATION, params=param_dict,headers=header_dict)
    def get_trip_list(self, param_dict={}):
        '''
        获取专车行程列表
          @ApiParam("userId") @RequestParam("userId") String userId,
          @ApiParam("offset") @RequestParam("offset") int offset,
          @ApiParam("limit") @RequestParam("limit") int limit) 
        '''
        return self.request("GET", ChariotReq.TRIP_LIST, params=param_dict)
    def get_trip_status(self, param_dict={}, header_dict={}):
        """
        #订单状态轮询

        :param param_dict: 
        :type header_dict: key;userId
        :return:
        """
        return self.request("POST", ChariotReq.TRIP_STATUS, params=param_dict, headers=header_dict)
    def get_trip_travelling(self, param_dict={}, header_dict={}):
        '''
        #获取行程中的订单
        :param header_dict: header_dict
        :param param_dict:key:accesstoken
        :return:
        '''
        return self.request("POST", ChariotReq.TRIP_TRAVELLING, params=param_dict, headers=header_dict)

