#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'yys'

from lib.mbmanage.requestmanage.base_req import BaseReq

class PersonalCenterReq(BaseReq):
    # 我的钱包_红包提现限制
    REDPACKET_DETAIL = "api/v2/redpacket/water/detail.do"
    # 小红点
    GET_REDPOINT = "api/v2/msg/getRedPoint.do"
    # 获得用户免费骑行信息
    GET_USER_RDFREEINFO = "api/v2/wx/getUserRDFreeInfo.do"
    # 获取用户帐户信息
    DOWNPAYMENTV2 = "api/v2/pay/downpaymentv2.do"
    # 用户可申请的免押金产品列表
    CAN_APPLY_PRODUCT_LIST = "api/v2/freeDeposit/canApplyProductList.do"
    # 骑行状态
    GET_RIDING = "api/v2/rentmgr/getriding.do"
    # 我的卡券
    COUPON_LIST = "api/v2/coupon/list.do"
    # 我的礼品卡
    CARD_LIST = "api/v2/card/list.do"
    # 我的贴纸
    USER_ACTIVITY_LIST = "api/v2/precious/v2/sticker/useractivitylist"
    # 删除用户的消息
    DELETE_MESSAGE = "api/v2/msg/deleteMessage.do"
    def __init__(self):
        super(PersonalCenterReq, self).__init__()

    def redpacket_detail(self, param_dict):
        '''
        我的钱包_红包提现限制
        :param param_dict:
        :return:
        '''

        return self.request("POST", PersonalCenterReq.REDPACKET_DETAIL, params=param_dict)

    def get_redpoint(self,header_dict=None, param_dict=None):
        '''
        小红点
        :param header_dict:
        :param param_dict:
        :return:
        '''

        return self.request("POST", PersonalCenterReq.GET_REDPOINT, params=param_dict, headers=header_dict)

    def get_user_rdfreeinfo(self,  param_dict=None):
        '''
        获得用户免费骑行信息
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", self.GET_USER_RDFREEINFO, params=param_dict)

    def downpaymentv2(self, param_dict=None):
        '''
        获取用户帐户信息

        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("GET", self.DOWNPAYMENTV2, params=param_dict)

    def can_apply_product_list(self,header_dict=None,param_dict=None):
        '''
        用户可申请的免押金产品列表
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST",PersonalCenterReq.CAN_APPLY_PRODUCT_LIST,headers=header_dict,params=param_dict)

    def get_riding(self,param_dict=None):
        '''
        骑行状态

        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST",PersonalCenterReq.GET_RIDING,params=param_dict)
    def coupon_list(self,param_dict=None):
        '''
        我的卡券
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("GET",PersonalCenterReq.COUPON_LIST,params=param_dict)
    def card_list(self,param_dict=None):
        '''
        我的礼品卡

        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("GET",PersonalCenterReq.CARD_LIST,params=param_dict)
    def user_activity_list(self,param_dict=None):
        '''
        我的贴纸

        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST",PersonalCenterReq.USER_ACTIVITY_LIST,params=param_dict)
    def delete_message(self,param_dict=None):
        '''
        删除用户的消息

        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST",PersonalCenterReq.DELETE_MESSAGE,params=param_dict)