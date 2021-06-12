#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName
class UserMemberInfo(BaseReq):
    #获取用户会员信息APP接口
    GET_USER_MEMBER_INFO = "api/v2/pay/getUserMemberInfo.do"
    #获取用户会员信息接口小程序
    DOWN_PAYMENT = "api/v2/pay/downpaymentv2.do"

    def get_user_member_info_req(self, param_header={}, param_dict={}):
        '''
        获取用户会员信息APP
        :param param_header:
        :param param_dict:
        :return:
        '''
        return self.request("POST", UserMemberInfo.GET_USER_MEMBER_INFO, headers=param_header, params=param_dict)

    def down_payment_req(self, param_header={}, param_dict={}):
        '''
        获取用户会员信息，小程序
        :param param_header:
        :param param_dict:
        :return:
        '''
        return self.request("POST", UserMemberInfo.DOWN_PAYMENT, headers=param_header, params=param_dict)

class PayWaterReq(BaseReq):
    #微信支付
    WEIXIN_PAYWATER = "api/v2/pay/weixin.do"
    DEPOSIT_INFO = "api/v2/pay/depositinfo.do"
    #退款押金接口
    REFUND = "api/v2/pay/refund.do"
    #获取可用付款渠道接口
    GLOBAL_CHANNELS = "api/v2/pay/global/channels.do"
    #iDEAL付款准备接口
    PREPARE_ADYEN_LOCAL_PAYMENT = "api/v2/pay/global/prepareadyenlocalpayment.do"
    #获取付款状态接口
    PAY_STATUS = "api/v2/pay/paystatus.do"
    # Adyen支付完成回调接口
    ADYEN_CALLBACK = "api/v2/pay/global/adyencallback.do"
    # iDEAL付款最终状态确认接口
    RECEIVE_ADYEN_PAY_NOTIFY = "api/v2/pay/global/receiveAdyenPayNotify.do"

    def __init__(self):
        super(PayWaterReq, self).__init__()

    def weixin_paywater(self, param_dict={}):
        '''
        微信支付
        :param param_dict:
        * @param index    配置钱对应的编号
         * @param userid   : 用户编号
         * @param paytype  ： 支付类型 ：押金
         * @param totalfee ：钱（分）
        :return:
        '''
        return self.request("POST", PayWaterReq.WEIXIN_PAYWATER, params=param_dict)

    def deposit_info(self, param_dict={}):
        '''
        获取用户押金信息
        :param param_dict:
         * @param userid   : 用户编号
        :return:
        '''
        return self.request("POST", PayWaterReq.DEPOSIT_INFO, params=param_dict)

    def refund(self, param_dict={}):
        '''
        用户押金退款
        :param param_dict:
         * @param userid   : 用户编号
        :return:
        '''
        return self.request("POST", PayWaterReq.REFUND, params=param_dict)

    def global_channels(self, header_dict=None, param_dict=None):
        '''
        获取可用付款渠道
        :return:
        '''
        return self.request("POST", PayWaterReq.GLOBAL_CHANNELS, headers=header_dict, params=param_dict)

    def prepare_adyen_local_payment(self, header_dict=None, param_dict=None):
        '''
        准备iDEAL付款信息
        :return:
        '''
        return self.request("POST", PayWaterReq.PREPARE_ADYEN_LOCAL_PAYMENT, headers=header_dict, params=param_dict)

    def adyen_callback(self, header_dict=None, param_dict=None):
        '''
        iDEAL付款完成回调
        :return:
        '''
        return self.request("GET", PayWaterReq.ADYEN_CALLBACK, headers=header_dict, params=param_dict)

    def receive_adyen_pay_notify(self, header_dict=None, param_dict=None):
        '''
        iDEAL付款最终状态确认
        :return:
        '''
        return self.request("GET", PayWaterReq.RECEIVE_ADYEN_PAY_NOTIFY, headers=header_dict, params=param_dict)

    def pay_status(self, header_dict=None, param_dict=None):
        '''
        获取付款状态
        :return:
        '''
        return self.request("GET", PayWaterReq.PAY_STATUS, params=param_dict, headers=header_dict)

class DepositInfoReq(BaseReq):
    # 获取押金接口
    GET_USER_DEPOSIT_INFO = "payment/query/getUserDepositInfo"

    def __init__(self):
        super(DepositInfoReq, self).__init__(micro_service_name=MicroServiceName.PAY_MENT)

    def get_user_deposit_info_req(self, param={}):
        '''获取用户押金接口
            param：userid
        '''
        return self.request("POST", DepositInfoReq.GET_USER_DEPOSIT_INFO, params=param)

class FreeDepositCard(BaseReq):
    # 免押金体验卡激活
    ACTIVATE_FREE_DEPOSIT = "api/v2/pay/activateFreeDepositCard.do"
    # 小程序免押金卡查询接口
    QUERY_FREE_CARD = "api/v2/pay/queryFreeDepositCard.do"

    def __init__(self):
        super(FreeDepositCard, self).__init__()

    def activate_free_deposit_card(self, param_dict={}):
        '''
        免押金体验卡激活
        :param param_dict: userid
        :return:
        '''
        return self.request("POST", FreeDepositCard.ACTIVATE_FREE_DEPOSIT, params=param_dict)

    def query_free_deposit_card(self, param_dict={}):
        '''
        小程序免押金卡查询
        :param param_dict: userid
        :return:
        '''
        return self.request("POST", FreeDepositCard.QUERY_FREE_CARD, params=param_dict)

class EndRide(BaseReq):
    '''
    结束行程相关接口
    '''
    def end_ride_without_confirm(self, param, header):
        '''
        是否可以直接结费
        :param param:POST
        :return:
        '''
        return self.request("POST", "api/v2/pay/canEndRideWithoutLockConfirm.do", params=param, headers=header)

    def end_ride_with_fixed_pay(self, param, header):
        '''
        结费接口
        :param param:
        :return:
        '''
        return self.request("POST", "api/v2/pay/endRideWithFixedPayIfAbove.do", params=param, headers=header)