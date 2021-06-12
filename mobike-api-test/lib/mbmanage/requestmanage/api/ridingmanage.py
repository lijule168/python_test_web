#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq

class RidingManageReq(BaseReq):
    #骑行经纬度记录上传
    UPLOAD_RIDINGBACK = "api/v2/rentmgr/ridingtrack.do"
    UNLOCK_BIKE = "api/v2/rentmgr/unlockBike.do"

    # 微信开锁接口
    WX_UNLOCK_BIKE = "api/v2/rentmgr/wxunlockBike.do"
    #骑行详情
    RIDINGDETAIL = "api/v2/rentmgr/ridingdetailForWebForHtml.do"

    #电单车开锁
    UNLOCK_SPOCK = "api/v2/rentmgr/unlockSpock.do"

    #骑行状态查询
    GET_RIDE_STATE = "api/v2/rentmgr/getridestate.do"

    #电单车 我的行程记录查询
    SPOCK_RIDING_HISTORY = "api/v2/rentmgr/spockridinghistory.do"

    #结费页查询
    ORDER_INFO = "api/v2/rentmgr/endorderinfo.do"

    # 订单详情接口
    ORDER_INFO_detail = "api/v2/rentmgr/orderinfo.do"

    # 发送开锁短信
    SEND_UNLOCK_COMMAND = "api/v2/rentmgr/sendunlockcommand.do"

    # 电单车关锁接口
    LOCK_SPOCK = "api/windmill/rentmgr/lockSpock.do"

    # 开锁状态查询
    LOCK_STATUS = "api/v2/rentmgr/lockstatusv2.do"
    # 关锁未结费
    LOCK_KEEP_FEE = "api/v2/pay/problem.do"

    def __init__(self):
        super(RidingManageReq, self).__init__()

    def lock_spock_req(self,  header_dict={}, param_dict={}):
        '''
        电单车关锁接口
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", RidingManageReq.LOCK_SPOCK, params=param_dict, headers=header_dict)

    def order_info_detail(self, header_dict={}, param_dict={}):
        '''
        订单详情接口
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", RidingManageReq.ORDER_INFO_detail, params=param_dict, headers=header_dict)

    def order_info_req(self, header_dict={}, param_dict={}):
        '''
        结费页查询
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", RidingManageReq.ORDER_INFO, params=param_dict, headers=header_dict)

    def spock_riding_history_req(self, header_dict={}, param_dick={}):
        '''
        电单车 我的行程记录查询
        :param header_dict:
        :param param_dick:
        :return:
        '''
        return self.request("POST", RidingManageReq.SPOCK_RIDING_HISTORY, params=param_dick, headers=header_dict)

    def get_riding_state_req(self, header_dict={}, param_dict={}):
        '''
        查询骑行状态
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", RidingManageReq.GET_RIDE_STATE, params=param_dict, headers=header_dict)

    def unlock_spock_req(self, header_dict={}, param_dict={}):
        '''
        电单车开锁
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", RidingManageReq.UNLOCK_SPOCK, params=param_dict, headers=header_dict)

    def ridingtrack(self, param_dict={}, header_dict={}):
        '''
        骑行经纬度记录上传
        :param param_dict:{userid:, orderid:, track:, platform:0, distance:}
        :param header_dict:{platform:, mobileNo:}
        :return:
        '''
        return self.request("POST", RidingManageReq.UPLOAD_RIDINGBACK, params=param_dict, headers=header_dict)

    def unlock_bike(self, param_dict={}, header_dict={}):
        '''
        解锁
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST", RidingManageReq.UNLOCK_BIKE, params=param_dict, headers=header_dict)

    def send_unlock_command(self, param_dict={}, header_dict={}):
        '''
        发送开锁短信
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST", RidingManageReq.SEND_UNLOCK_COMMAND, params=param_dict, headers=header_dict)


    def riding_detail(self, param_dict={}):
        '''
        骑行详细信息
        :param param_dict:{userid, orderid}
        :return:
        '''
        return self.request("POST", RidingManageReq.RIDINGDETAIL, params=param_dict)

    def get_lockopen_status(self,  header_dict={}, param_dict={}):
        '''
        开锁状态查询
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", RidingManageReq.LOCK_STATUS, params=param_dict, headers=header_dict)

    def wxunlock_bike(self, param_dict={}, header_dict={}):
        '''
        微信小程序开锁
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST", RidingManageReq.WX_UNLOCK_BIKE, params=param_dict, headers=header_dict)

    def lock_keep_fee(self, param_dict={}, header_dict={}):
        '''
        关锁未结费
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST", RidingManageReq.LOCK_KEEP_FEE, params=param_dict, headers=header_dict)