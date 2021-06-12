#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq

class ScheduleReq(BaseReq):
    #新预约接口 ： 取消预约确认前的状态
    SCHEDU_CONFIRM = "api/v2/schedu/confirmation.do"
    #预约蜂鸣
    SCHEDU_BEEP ="api/v2/schedu/beep.do"
    #预定激活
    SCHEDU_ACTIVE = "api/v2/schedu/active.do"
    #取消预定
    SCHEDU_CANCEL = "api/v2/schedu/stop.do"
    #取消用戶预约蜂鸣
    SCHEDU_CANCEL_BEEP = "api/v2/schedu/cancelUserBeep.do"
    # 获取预约取消限制总数和当前用户的预约取消次数
    SCHEDU_CANCELED_NUB = "api/v2/schedu/cancelednub.do"
    #更新蜂鸣相关配置的接口
    UPDATE_SCHEDU_CONFIG = "api/v2/schedu/updateBeepConfig"
    def __init__(self):
        super(ScheduleReq, self).__init__()

    def schedu_confirm(self, param_dict={},header_dict={}):
        '''
        新预约接口 ： 取消预约确认前的状态
        :param param_dict:{longitude:, latitude:, bikeIds:, isactive:0, biketype:, userid}
        :return:
        '''
        return self.request("POST", ScheduleReq.SCHEDU_CONFIRM, params=param_dict,headers=header_dict)

    def schedule_beep(self, param_dict={}):
        '''
        预约蜂鸣
        :param param_dict:{bikeId:, userid}
        :return:
        '''
        return self.request("POST", ScheduleReq.SCHEDU_BEEP, params=param_dict)

    def active(self, param_dict={}):
        '''
        预定激活
        :param param_dict:{bikeId:, userid}
        :return:
        '''
        return self.request("POST", ScheduleReq.SCHEDU_ACTIVE, params=param_dict)

    def schedule_cancel(self, param_dict={}, header_dict={}):
        '''
        取消预定
        :param param_dict:{bikeId:, userid}
        :return:
        '''
        return self.request("POST", ScheduleReq.SCHEDU_CANCEL, params=param_dict, headers=header_dict)

    def beep_cancel(self, param_dict={}):
        '''
        取消用戶预约蜂鸣
        :param param_dict:{userid}
        :return:
        '''
        return self.request("POST", ScheduleReq.SCHEDU_CANCEL_BEEP, params=param_dict)

    def schedule_canceled_nub(self, param_dict={}):
        '''
        获取预约取消限制总数和当前用户的预约取消次数
        :param param_dict:{userid}
        :return:
        '''
        return self.request("POST", ScheduleReq.SCHEDU_CANCELED_NUB, params=param_dict)

    def update_beep_config(self, param_dict={}):
        '''
        更新蜂鸣相关配置的接口
        :param param_dict:{beepAllCount, beepBikeCount}
        :return:
        '''
        return self.request("POST", ScheduleReq.UPDATE_SCHEDU_CONFIG, params=param_dict)