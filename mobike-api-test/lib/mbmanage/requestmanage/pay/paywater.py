#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'pengdingguo'

from lib.mbmanage.requestmanage.base_req import BaseReq

class PayWaterReq(BaseReq):
    #微信支付调用的后台接口
    WEIXIN_PAYWATER = "api/v2/pay/weixin.do"
    #绑定微信并提现
    BIND_WXPAY = "api/v2/pay/bindwxpayinfo.do"
    #解除微信绑定
    UNBIND_WXPAY = "api/v2/pay/unbindwxpayinfo.do"

    def __init__(self):
        super(PayWaterReq, self).__init__()

    def pay_water(self, param_dict={}):
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
    def bind_wxpay(self, param_dict={}, header_dict= {}):
        '''
        绑定微信并提现
        :param parm_dict:
        :return:
        '''
        return  self.request("POST", PayWaterReq.BIND_WXPAY, params=param_dict, headers= header_dict)

    def unbind_wxpay(self, param_dict={}):
        '''
        解除绑定微信
        :param parm_dict:
        :return:
        '''
        return self.request("POST", PayWaterReq.UNBIND_WXPAY, params=param_dict)
