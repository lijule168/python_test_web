#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq

class ClockInReq(BaseReq):

    #获取骑行打卡配置
    CLOCK_IN_CONFIG = "api/v2/clock-in/config.do"
    #获取骑行打卡记录
    CLOCK_IN_RECORD = "api/v2/clock-in/record.do"
    #查看福袋详情
    CLOCK_IN_PACKETDETAIL = "api/v2/clock-in/packetDetail.do"
    #上传收货人信息
    CLOCK_IN_UPLOAD_RECEIVER_INFO = "api/v2/clock-in/uploadReceiverInfo.do"

    def __init__(self):
        super(ClockInReq, self).__init__()

    def get_clockin_config(self):
        '''
        获取骑行打卡配置
        :return:
        '''
        return self.request("GET", ClockInReq.CLOCK_IN_CONFIG)

    def get_clockin_record(self, header_dict={}):
        '''
        获取骑行打卡记录
        :param header_dict:{accesstoken:用户token}
        :return:
        '''
        return self.request("GET", ClockInReq.CLOCK_IN_RECORD, headers=header_dict)

    def get_clockin_packetdetail(self, param_dict={}, header_dict={}):
        '''
        查看福袋详情
        :param header_dict:{accesstoken:用户token}
        :param param_dict:{
        packetId:福袋ID,
        isOpen:是否已打开
        }
        :return:
        '''
        return self.request("POST", ClockInReq.CLOCK_IN_PACKETDETAIL, params=param_dict, headers=header_dict)

    def get_clockin_uploadreceiverinfo(self, param_dict={}, header_dict={}):
        '''
        上传收货人信息
        :param header_dict:{accesstoken:用户token}
        :param param_dict: {userCouponId:对应礼品发放的记录id,
        mobile:收货电话,
        address:收货地址,
        name:收货人}
        :return:
        '''
        return self.request("POST", ClockInReq.CLOCK_IN_UPLOAD_RECEIVER_INFO, params=param_dict, headers=header_dict)
