#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class RidingOrderReq(BaseReq):
    # 骑行订单信息
    ORDERINFO = "api/v2/rentmgr/orderinfo.do"
    # 查看结束的订单信息
    ENDORDERINFO = "api/v2/rentmgr/endorderinfo.do"
    #  骑行订单支付信息
    ORDERPAYINFO = "api/v2/rentmgr/orderpayinfo.do"
    # 锁状态轮训
    LOCKSTATUS = "api/v2/rentmgr/lockstatus.do"
    # 骑行状态轮训
    RIDESTATE = "api/v2/rentmgr/getridestate.do"

    def __init__(self):
        super(RidingOrderReq, self).__init__()

    def rentmgr_orderinfo(self, param_dict=None, header_dict=None):
        '''
        骑行订单信息
        '''
        return self.request("GET",RidingOrderReq.ORDERINFO , params=param_dict, headers=header_dict)

    def rentmgr_endorderinfo(self, param_dict=None, header_dict=None):
        '''
        查看结束的订单信息
        '''
        return self.request("GET", RidingOrderReq.ENDORDERINFO, params=param_dict, headers=header_dict)

    def rentmgr_orderpayinfo(self, param_dict=None, header_dict=None):
        '''
        骑行订单支付信息
        '''
        return self.request("POST",RidingOrderReq.ORDERPAYINFO , params=param_dict, headers=header_dict)

    def rentmgr_lockstatus(self, param_dict=None, header_dict=None):
        '''
       锁状态轮训接口
        '''
        return self.request("POST", RidingOrderReq.LOCKSTATUS, params=param_dict, headers=header_dict)

    def rentmgr_getridestate(self, param_dict=None, header_dict=None):
        '''
       骑行状态轮训接口
        '''
        return self.request("POST", RidingOrderReq.RIDESTATE, params=param_dict, headers=header_dict)
