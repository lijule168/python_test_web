#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class TrialPeriodReq(BaseReq):
    def __init__(self):
        super(TrialPeriodReq, self).__init__(micro_service_name=MicroServiceName.TRIALPERIOD)

    def usertrialqualification(self , param_dict=None):
        '''
        Check UserTrialQualification
        '''
        return self.request("POST", "trialperiod/check/userTrialQualification", params=param_dict)

    def get_usertrialrecordinfo(self, param_dict=None):
        '''
        Get UserTrialRecordInfo
        '''
        return self.request("POST", "trialperiod/get/userTrialRecordInfo", params=param_dict)

    def save_usertrialrecordinfo(self , param_dict=None):
        '''
        Save UserTrialRecordInfo
        '''
        return self.request("POST", "trialperiod/save/userTrialRecordInfo", params=param_dict)

    def usertrialrecordpaiddepositinfo(self , param_dict=None):
        '''
        Update UserTrialRecordPaidDepositInfo
        '''
        return self.request("POST", "trialperiod/update/userTrialRecordPaidDepositInfo", params=param_dict)

    def refreshswitch(self, param_dict=None):
        '''
        每次修改开关信息后需要调用该接口刷新缓存，否则需要5分钟才能生效
        :param param_dict:
        :return:
        '''
        return self.request("POST", "trialperiod/refreshSwitch", params=param_dict)

class TrialPeriodApiReq(BaseReq):
    def __init__(self):
        super(TrialPeriodApiReq, self).__init__()

    def get_i18nconfiginfo(self , param_dict=None, header_dict=None):
        '''
        Check UserTrialQualification
        '''
        return self.request("POST", "api/v2/i18nConfig/info", params=param_dict, headers=header_dict)

    def get_i18nob_deposit(self, param_dict=None, header_dict=None):
        '''
        Get UserTrialRecordInfo
        '''
        return self.request("POST", "api/v2/i18nOB/deposit", params=param_dict, headers=header_dict)

    def save_trialrecord(self , param_dict=None, header_dict=None):
        '''
        Save UserTrialRecordInfo
        '''
        return self.request("POST", "api/v2/i18nOB/saveTrialRecord", params=param_dict, headers=header_dict)

    def update_trialrecordnotify_info(self , param_dict=None, header_dict=None):
        '''
        Update UserTrialRecordPaidDepositInfo
        '''
        return self.request("POST", "api/v2/i18n/update/trialRecordNotifyInfo", params=param_dict, headers=header_dict)

    def get_i18nconfig_paidsuggestinfo(self , param_dict=None, header_dict=None):
        '''
        Update UserTrialRecordPaidDepositInfo
        '''
        return self.request("POST", "api/v2/i18nConfig/paidSuggestInfo", params=param_dict, headers=header_dict)

    def athena_createnewrules(self,param_dict=None, header_dict=None,json_data=None):
        '''
        雅典娜增加免押金试骑国家
        :param param_dict:
        :param header_dict:
        :param json_data:
        :return:
        '''
        return self.request("POST", "athena/featureSwitch/createNewRules",params=param_dict, headers=header_dict, json_data=json_data)

    def athena_addConfigByType(self,param_dict=None, header_dict=None,json_data=None):
        '''
        雅典娜增加试骑时长athena/featureSwitch/getFeatureSwitch?featureId=5
        :param param_dict:
        :param header_dict:
        :param json_data:
        :return:
        '''
        return self.request("POST", "athena/opsconfig/addConfigByType.do",params=param_dict, headers=header_dict, json_data=json_data)

    def athena_editConfigByType(self,param_dict=None, header_dict=None,json_data=None):
        '''
        雅典娜编辑魔币数量控制
        :param param_dict:
        :param header_dict:
        :param json_data:
        :return:
        '''
        return self.request("POST", "athena/opsconfig/edit.do",params=param_dict, headers=header_dict, json_data=json_data)

    def athena_getrules(self,param_dict=None, header_dict=None,json_data=None):
        '''
        雅典娜获取免押金试骑国家athena/featureSwitch/deleteRules
        :param param_dict:
        :param header_dict:
        :param json_data:
        :return:
        '''
        return self.request("GET", "athena/featureSwitch/getFeatureSwitch",params=param_dict, headers=header_dict)

    def athena_deleterules(self,param_dict=None, header_dict=None,json_data=None):
        '''
        雅典娜删除免押金试骑国家
        :param param_dict:
        :param header_dict:
        :param json_data:
        :return:
        '''
        return self.request("POST", "athena/featureSwitch/deleteRules",params=param_dict, headers=header_dict, json_data=json_data)