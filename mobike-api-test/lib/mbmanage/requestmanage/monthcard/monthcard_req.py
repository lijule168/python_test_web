# /usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'zhangjiangtao@mobike.com'

from lib.mbmanage.requestmanage.base_req import BaseReq

class MonthCardReq(BaseReq):
    #获取售卖月卡详情接口
    SELLING_DETAIL = "api/v2/monthcard/getSellingDetail.do"
    #获取月卡列表
    SELLING_LIST   = "api/v2/monthcard/getSellingList.do"
    #购买月卡
    PURCHASE_MONTHCARD = "api/v2/pay/balancepay.do"
    #新建国际化免押金月卡
    CREATE_I18N_MONTHCARD = "athena/opsconfig/addConfigByType.do"
    #国际化免押金月卡配置列表
    QUERY_I18N_MONTHCARD_CONFIGLIST = "athena/opsconfig/queryConfigList.do"
    #更新国际化免押金月卡
    UPDATE_I18N_MONTHCARD = "athena/opsconfig/updateConfig.do"
    #删除国际化免押金月卡
    DELETE_I18N_MONTHCARD = "athena/opsconfig/deleteConfig.do"
    # 获取月卡列表
    I18N_SELLING_LIST = "api/v2/monthcard/i18nGetSellingList"
    # 添加月卡原价
    ADD_ORIGIN_PRICE = "athena/monthCards/addOriginPriceCard"

    def __init__(self):
        super(MonthCardReq,self).__init__()

    def get_selling_detail(self,header_dict=None,param_dict=None):
        '''
        获取售卖月卡详情
        :param param_dict:
        :return:
        '''
        return  self.request("POST",MonthCardReq.SELLING_DETAIL,headers=header_dict,params=param_dict)

    def get_selling_list(self,header_dict=None,param_dict=None):
        '''
        获取月卡列表
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return  self.request("POST",MonthCardReq.SELLING_LIST,headers=header_dict,params=param_dict)

    def monthcard_getmonthcarddiscount(self, param_dict=None):
        '''
        获取月卡抽奖折扣
        '''
        return self.request("POST", "api/v2/monthcard/getMonthCardDiscount", params=param_dict)

    def monthcard_getsellinglist(self, param_dict=None, header_dict=None):
        '''
        获取以购买的月卡信息
        '''
        return self.request("POST", "api/v2/monthcard/getSellingList", params=param_dict, headers=header_dict)

    def monthcard_getdiscountinfo(self, param_dict=None, header_dict=None):
        '''
        获取月卡折扣Banner相关信息
        '''
        return self.request("POST", "api/v2/monthcard/getDiscountInfo", params=param_dict, headers=header_dict)

    def purchase_monthcard(self,  param_dict=None, header_dict=None):
        '''
        购买月卡
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return  self.request("POST",MonthCardReq.PURCHASE_MONTHCARD,headers=header_dict,params=param_dict)
    def create_i18n_monthcard(self, param_dict=None, header_dict=None,json_dict=None):
        '''
        雅典娜 - 月卡配置 - 国际化免押金月卡配置，新建国际化月卡
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST",MonthCardReq.CREATE_I18N_MONTHCARD,headers=header_dict,params=param_dict,json_data=json_dict)

    def query_i18n_configlist(self, param_dict=None, header_dict=None,json_dict=None):
        '''
        雅典娜 - 月卡配置 - 国际化免押金月卡配置，国际化月卡配置列表
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST",MonthCardReq.QUERY_I18N_MONTHCARD_CONFIGLIST,headers=header_dict,params=param_dict,json_data=json_dict)

    def update_i18n_monthcard(self, param_dict=None, header_dict=None,json_dict=None):
        '''
        雅典娜 - 月卡配置 - 国际化免押金月卡配置，更新国际化月卡配置
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST",MonthCardReq.UPDATE_I18N_MONTHCARD,headers=header_dict,params=param_dict,json_data=json_dict)

    def delete_i18n_monthcard(self, param_dict=None, header_dict=None,json_dict=None):
        '''
        雅典娜 - 月卡配置 - 国际化免押金月卡配置，删除国际化月卡配置
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST",MonthCardReq.DELETE_I18N_MONTHCARD,headers=header_dict,params=param_dict,json_data=json_dict)

    def get_i18n_selling_list(self,header_dict=None,param_dict=None):
        '''
        获取国际化售卖月卡详情
        :param param_dict:
        :return:
        '''
        return  self.request("POST",MonthCardReq.I18N_SELLING_LIST,headers=header_dict,params=param_dict)

    def add_origin_price(self, param_dict=None, header_dict=None, json_dict=None):
        '''
        雅典娜 - 月卡配置 - 新建月卡原价
        :param param_dict:
        :param header_dict:
        :return:
        '''
        return self.request("POST", MonthCardReq.ADD_ORIGIN_PRICE, headers=header_dict, params=param_dict, json_data=json_dict)