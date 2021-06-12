#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangsong'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName

class GroupMemberReq(BaseReq):
    '''
    微信小程序骑行排行相关操作
    '''
    def __init__(self):
        super(GroupMemberReq, self).__init__(micro_service_name=MicroServiceName.WECHAT)

    # 查看微信骑行排行内容
    RANKING_DETAIL = "wechat/groupRankingDetail"

    # 查看我上周的骑行记录
    LAST_WEEK_INFO = "wechat/groupMemberLastWeekInfo"

    # 添加用户的骑行记录信息
    ADD_USER_RIDING_DATA = "wechat/addGroupUserRidingData"

    # 加入排行榜
    ADD_GROUP_MEMBER_INFO = "wechat/addGroupMemberInfo"

    def last_week_info(self, param_dict={}):
        '''
        查看我上周的骑行记录
        :param param_dict:userId
        :return:
        '''
        return self.request("GET", GroupMemberReq.LAST_WEEK_INFO, params=param_dict)

    def add_group_member_info(self, param_dict={}):
        '''
        加入排行榜
        :param param_dict:groupId，群ID，userId：用户ID
        wechatNickname：微信名称，wechatAvatar：微信头像，formId=2323， wechatOpenId：微信openid
        :return:
        '''
        return self.request("GET", GroupMemberReq.ADD_GROUP_MEMBER_INFO, params=param_dict)

    def ranking_detail(self, param_dict={}):
        '''
        查看微信小程序骑行排行内容
        :param param_dict:groupId:群ID，userId: 用户ID，wechatOpenId
        :return:
        '''
        return self.request("GET", GroupMemberReq.RANKING_DETAIL, params=param_dict)

    def add_user_riding_data(self, param_dict={}):
        '''
        添加用户骑行记录
        :param param_dict:totalRidingTime，用户骑行时间；totalDistance，用户骑行数据；totalFee，用户花费金额；userId=
        :return:返回1成功， 0 不成功
        '''
        return self.request("GET", GroupMemberReq.ADD_USER_RIDING_DATA, params=param_dict)

if __name__ == "__main__":
    ws = GroupMemberReq()
    ws.last_week_info()