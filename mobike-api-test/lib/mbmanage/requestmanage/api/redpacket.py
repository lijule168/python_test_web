# /usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'zhangjiangtao@mobike.com'

from lib.mbmanage.requestmanage.base_req import BaseReq

class RedPacketReq(BaseReq):
    # 我的红包
    MYREDPACKET     = "api/v2/redpacket/water/detail.do"
    # 红包明细列表
    REDPACKETDETAIL = "api/v2/redpacket/water/list.do"
    # 红包
    TRANSFERREDPACKETTOWALLET = "api/v2/pay/transferRedpacketToWallet.do"

    def __init__(self):
        super(RedPacketReq,self).__init__()

    def myredpacket_info(self,param_dict={}):
        '''
        获取 我的红包 信息
        :param param_dict:
        * @param userid   : 用户编号
        :return:
        '''
        return  self.request("POST",RedPacketReq.MYREDPACKET,params=param_dict)
    def redpacket_detail(self,param_dict = {} ):
        '''
        红包明细 信息
        :param param_dict:
        * @param userid   : 用户编号
        :return:
        '''
        return self.request("POST",RedPacketReq.REDPACKETDETAIL,params=param_dict)
    def transfer_redpacket_to_wallet(self,param_dict = {} ):
        '''
        红包充值到余额
        :param param_dict:
        :return:
        '''
        return self.request("POST", RedPacketReq.TRANSFERREDPACKETTOWALLET, params=param_dict)

    def retrieve_rp(self, param_dick, header_dict):
        '''
        红包领取
        :param param_dick:
        :param header_dict:
        :return:
        '''
        return self.request("GET", "api/v2/redpacket/rfm/retrieveRp.do", params=param_dick, headers=header_dict)

