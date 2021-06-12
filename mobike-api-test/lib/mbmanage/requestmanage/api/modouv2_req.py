#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class ModouV2Req(BaseReq):
    def __init__(self):
        super(ModouV2Req, self).__init__()

    def modouv2_applylastweekcoins(self, param_dict=None):
        '''
        领取用户最近一周未领取积分
        '''
        return self.request("POST", "api/v2/modouv2/applyLastweekCoins", params=param_dict)

    def modouv2_applymocoinbyorder(self, param_dict=None):
        '''
        领取指定订单魔币
        '''
        return self.request("POST", "api/v2/modouv2/applyMoCoinByOrder", params=param_dict)

    def modouv2_getlastweeknotapplycoins(self, param_dict=None):
        '''
        获取用户最近一周未领取积分总分
        '''
        return self.request("GET", "api/v2/modouv2/getLastweekNotApplyCoins", params=param_dict)

    def modouv2_mocointotal(self, param_dict=None):
        '''
        获取用户积分
        '''
        return self.request("GET", "api/v2/modouv2/mocoinTotal", params=param_dict)

    def modouv2_modoulist(self, param_dict=None):
        '''
        获取用户摩豆明细-分页
        '''
        return self.request("POST", "api/v2/modouv2/modouList", params=param_dict)

    def modouv2_modoulistandtotalmocoin(self, param_dict=None):
        '''
        获取用户摩豆明细-分页和一周未领取总分
        '''
        return self.request("GET", "api/v2/modouv2/modouListAndTotalMoCoin", params=param_dict)

    def modouv2_prizemocoin(self, param_dict=None):
        '''
        活动/分享/报障添加积分明细（修改总分）
        '''
        return self.request("POST", "api/v2/modouv2/prizeMoCoin", params=param_dict)

