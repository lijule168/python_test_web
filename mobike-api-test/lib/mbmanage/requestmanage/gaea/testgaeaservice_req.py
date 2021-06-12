#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName
from lib.util.log_util import l

class TestGaeaServiceReq(BaseReq):
    #添加用户参与活动
    TEST_SHINING_ADD = "test/shining/add"
    #删除用户的活动信息
    TEST_SHINING_DEL = "test/shining/del"
    #获取用户的活动信息
    TEST_SHINING_GET = "test/shining/get"
    #活动次数减一
    TEST_SHINING_DECREASE = "test/shining/decrease"
    # 修改coolDown时间
    COOL_DOWN = "red3Test/redPacket/changeCoolDownTime"
    # 触发coolDownJob
    COOL_DOWN_JOB = "red3Test/redPacket/coolDownJob"
    def __init__(self):
        super(TestGaeaServiceReq, self).__init__(micro_service_name=MicroServiceName.GAEA)

    def cool_down(self, param_dict):
        '''
        修改coolDown时间
        :param param_dict:
        :return:
        '''
        return self.request("GET", api_path=self.__class__.COOL_DOWN, params=param_dict)

    def cool_down_job(self, param_dict):
        '''
        触发cooldownjob
        :param param_dict:
        :return:
        '''
        return self.request("GET", api_path=self.__class__.COOL_DOWN_JOB, params=param_dict)

    def add_shining(self, param_dict):
        '''
        添加骑行白名单用户
        :param param_dict:userId， count，secondExpire,promotionName
        :return:
        '''
        return self.request("GET", api_path=self.__class__.TEST_SHINING_ADD, params=param_dict)


    def del_shining(self, param_dict):
        '''
        删除白名单用户
        :param param_dict:userId
        :return:
        '''
        return self.request("GET", api_path=self.__class__.TEST_SHINING_DEL, params=param_dict)

    def get_shining(self, param_dict):
        '''
        获取白名单用户
        :param param_dict:userId
        :return:
        '''
        return self.request("GET", api_path=self.__class__.TEST_SHINING_GET, params=param_dict)


