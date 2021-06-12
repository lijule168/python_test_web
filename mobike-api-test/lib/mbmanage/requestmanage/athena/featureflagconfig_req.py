# /usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'zhangjiangtao@mobike.com'

from lib.mbmanage.requestmanage.base_req import BaseReq

class FeatureFlagConfigReq(BaseReq):
    # 创建FeatureFlag
    FEATUREFLAGCREATE = "athena/featureflag/create.json"
    # FeatureFlag 列表
    FEATUREFLAG_LIST = "athena/featureflag/search.json"
    # FeatureFlag 详情
    FEATUREFLAGDETAIL = "athena/featureflag/details.json"
    # 打开FeatureFlag
    FEATUREFLAGREACTIVE = "athena/featureflag/reactive.json"



    def __init__(self):
        super(FeatureFlagConfigReq,self).__init__()

    def create_feature_flag(self,param_dict=None, header_dict=None):
        '''
        创建新的FeatureFlag
        '''
        return  self.request("POST", "athena/featureflag/create.json",params=param_dict, headers=header_dict)

    def featureflaglist(self,param_dict=None, header_dict=None):
        '''
        获取 FeatureFlag 列表
        '''
        return  self.request("GET",FeatureFlagConfigReq.FEATUREFLAG_LIST,params=param_dict, headers=header_dict)

    def feature_flag_detail(self,param_dict=None, header_dict=None):
        '''
        获取 FeatureFlag 详情
        '''
        return  self.request("GET","athena/featureflag/details.json",params=param_dict, headers=header_dict)

    def pause_feature_flag(self,param_dict=None, header_dict=None):
        '''
        暂停指定 FeatureFlag
        '''
        return  self.request("POST","athena/featureflag/pause.json",params=param_dict, headers=header_dict)

    def reactive_feature_flag(self,param_dict=None, header_dict=None):
        '''
        激活指定 FeatureFlag
        '''
        return  self.request("POST","athena/featureflag/reactive.json",params=param_dict, headers=header_dict)

    def update_ratio_feature_flag(self,param_dict=None, header_dict=None):
        '''
        调整指定 FeatureFlag 生效百分比
        '''
        return  self.request("POST","athena/featureflag/newLogic/updateFlowRatio.json",params=param_dict, headers=header_dict)

