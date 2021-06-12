#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq
"""
--------------------------------------
    date:   2018/3/21
--------------------------------------
    Change Date: 2018/3/21
    
"""
__author__ = "wangsong@mobike.com"


class WxCashReq(BaseReq):
    '''
    微信补贴裂变红包相关接口
    '''

    def get_effective_wx_cash(self, header_dict, param_dict):
        '''
        获取指定用户的有效红包信息
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("GET", "api/wechat/wxcash/getEffectiveWxCash", headers=header_dict, params=param_dict)

    def marquee_wx_cash(self):
        '''
        获取 跑马灯大额红包展示接口
        :return:
        '''
        return self.request("GET", "api/wechat/wxcash/marqueeWxCash")

    def share_call_back(self, header_dict, param_dict):
        '''
        分享群回调（返回已经分享了几个群）
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", "api/wechat/wxcash/shareCallback", headers=header_dict, params=param_dict)

    def gen_wx_cash(self, header_dict, param_dict):
        '''
        生成裂变红包接口
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", "api/wechat/wxcash/genWxCash", headers=header_dict, params=param_dict)

    def receive_wx_cash(self, header_dict, param_dict):
        '''
        领取裂变红包接口
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", "api/wechat/wxcash/receiveWxCash", headers=header_dict, params=param_dict)

    def reward_wx_cash_on_the_way(self, header_dict, param_dict):
        '''
        在路上的红包接口
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("GET", "api/wechat/wxcash/rewardWxCashOntheWay", headers=header_dict, params=param_dict)

    def can_receive_wx_cash(self, header_dict, param_dict):
        '''
        可领取的红包接口
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("GET", "api/wechat/wxcash/canReceiveWxCash", headers=header_dict, params=param_dict)

    def get_receive_wx_cash_info(self, header_dict, param_dict):
        '''
        用户裂变红包收益接口
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("GET", "api/wechat/wxcash/getReceivedWxCashInfo", headers=header_dict, params=param_dict)

    def get_receive_wx_cash_detail(self, header_dict, param_dict):
        '''
        获取用户裂变红包收益明细接口
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("GET", "api/wechat/wxcash/getReceivedWxCashDetail", headers=header_dict, params=param_dict)

    def invite_html_combination(self, header_dict, param_dict):
        '''
        邀请好友页面组合接口
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("GET", "api/wechat/wxcash/inviteHtmlCombination", headers=header_dict, params=param_dict)
