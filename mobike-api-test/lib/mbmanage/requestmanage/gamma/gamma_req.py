#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'wangsong'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName
import json
from lib.entity.testdata_struct import TestKey
from script.base_testcase import BaseTestCase

class UpgradeVersionReq(BaseReq):
    def __init__(self):
        super(UpgradeVersionReq, self).__init__()

    # 查询用户是否需要升级
    UPDATE_VERSION = "api/v2/upgrade/version.do"

    def update_version_req(self, param_dict={}, headers={}):
        '''
        查询用户是否需要升级
        :param param_dict:
        :param headers:
        :return:
        '''
        return self.request("POST", UpgradeVersionReq.UPDATE_VERSION, params=param_dict, headers=headers)



class AppConfigGammaReq(BaseReq):
    '''
    灰度服务
    '''
    def __init__(self):
        super(AppConfigGammaReq, self).__init__(micro_service_name=MicroServiceName.APPCONFIG_GAMMA)

    # 查询APP版本列表接口
    APPS = "/gamma/apps"
    RULES = "/gamma/rules"
    PAGED_RULES = "/gamma/pagedrules"
    RULES_DELETE = "/gamma/rules/delete"
    RULES_UPDATE = "/gamma/rules/update"

    def apps_req(self, param_dict={}):
        '''
        查询app版本列表
        :param param_dict:
        :return:
        '''
        return self.request("GET", AppConfigGammaReq.APPS)

    def rules_req(self, param_dick={}, headers={}):
        '''
        创建新的灰度规则
        :param param_dick:name, appVersion, description, gammaType, detail
        :return:
        '''
        # header = {'Content-Type': "application/json"}
        return self.request("POST", AppConfigGammaReq.RULES, params=param_dick, headers=headers)

    def paged_rules_req(self, param_dict={}):
        '''
        查询灰度规则列表
        :param param_dict:
        :return:
        '''
        return self.request("GET", AppConfigGammaReq.PAGED_RULES, params=param_dict)

    def rules_delte_req(self, param_dict={}, headers={}):
        '''
        删除某个灰度规则
        :param param_dict:
        :return:
        '''
        return self.request("POST", AppConfigGammaReq.RULES_DELETE, params=param_dict, headers=headers)

    def get_rules_req(self, param_dict={}):
        '''
        通过ID获取灰度规则详情
        :param param_dict:
        :return:
        '''
        return self.request("GET", AppConfigGammaReq.RULES, params=param_dict)

    def rules_update_req(self, param_dict={}, headers={}):
        '''
        更新灰度规则
        :param param_dict:
        :param headers:
        :return:
        '''
        return self.request("POST", AppConfigGammaReq.RULES_UPDATE, params=param_dict, headers=headers)


