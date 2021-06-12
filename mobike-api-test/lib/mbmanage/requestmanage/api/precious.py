#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangsong'

from lib.mbmanage.requestmanage.base_req import BaseReq

class UserActivityReq(BaseReq):

    def __init__(self):
        super(UserActivityReq, self).__init__()

    # 获取贴纸活动详情列表
    USER_ACTIVITY_LIST = 'api/v2/precious/v2/sticker/useractivitylist'
    # 获取贴纸活动详情
    USER_ACTIVITY = 'api/v2/precious/v2/sticker/activity'

    def user_activity_list(self, param_dict={}):
        '''
        获取贴纸活动详情列表
        :param param_dict: activityId， userid， war
        :return:
        '''
        return self.request("POST", UserActivityReq.USER_ACTIVITY_LIST, params=param_dict)

    def user_activity(self, param_dict={}):
        '''
        获取贴纸活动详情
        :param param_dict:activityId， war
        :return:
        '''
        return self.request("POST", UserActivityReq.USER_ACTIVITY, params=param_dict)