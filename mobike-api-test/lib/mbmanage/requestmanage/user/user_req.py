#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'dingbaixia'

from lib.mbmanage.requestmanage.base_req import BaseReq

class UserReq(BaseReq):
    # 获取验证码接口
    GET_CAPTCHA = "athena/tools/setmoblieverifycode.do"
    # 登录注册接口
    LOGIN = "api/v2/usermgr/login.do"
    # 登出接口
    LOGOUT = "api/v2/usermgr/logout.do"
    # 实名认证接口
    IDCODE = "api/v2/usermgr/idcode.do"
    # 修改用户昵称、头像接口
    SAVE = "api/v2/usermgr/save.do"
    # 生成、修改、使用邀请码接口
    INVITATION = "api/v2/usermgr/invitaion.do"
    # 修改手机号码接口
    CHANGEMOBILE = "api/v2/usermgr/changemobile.do"
    #个人钱包信息
    WALLET_INFO = "api/v2/pay/downpaymentv2.do"
    # 语音验证码接口
    VOICE_CAPTCHA = "api/v2/usermgr/getverifycode.do"
    # 确认为合法年龄接口
    UPDATE_LEGAL_AGE = "api/v2/globaluserextendinfo/updatelegalage"
    # 获取当前开城国家列表接口
    GET_COUNTRY_LIST = "api/v2/userregion/getcountrylist"
    # 用户选择所属国家接口
    SELECT_COUNTRY_REGION = "api/v2/userregion/selectcountryregion"
    #注册免押金
    REGIST_FREE_DEPOSIT = "api/v2/usermgr/regFreeDeposit"
    # 修改手机号检查
    CHANGE_MOBILE_CHECK = "api/v2/usermgr/changemobilecheck.do"
    #设备绑定
    DEVICE_BIND = "api/v2/usermgr/binddeviceinfo.do"
    # UUID设备绑定
    UUID_BIND = "api/v2/usermgr/bindinguid.do"
    # 新信用分体系 获取用户信用分
    USER_CREDIT = "api/v2/creditsystem/userCredit"
    #修改用户信息
    CHANGE_EXTENDINFO = "api/user/usermgr/changeExtendInfo.do"
    #校验用户密码
    CHECK_PASSWORD = "api/user/usermgr/checkPassword.do"
    #校验用户验证码
    CHECK_VERIFYCODE = "api/user/usermgr/checkVerifyCode.do"

    def __init__(self):
        super(UserReq, self).__init__()

    def get_captcha(self, param_dict):
        '''
        获取验证码
        :param param_dict:
        :return:
        '''

        return self.request("GET", UserReq.GET_CAPTCHA, params=param_dict)

    def get_user_credit(self, param):
        '''
        新信用分体系-获取用户信用分
        :param param:
        :return:
        '''
        return self.request("GET", UserReq.USER_CREDIT, params=param)

    def login(self, header_dict=None, param_dict=None):
        '''
        手机号登录
        :param header_dict:
        :param param_dict:
        :return:
        '''

        return self.request("POST", UserReq.LOGIN, params=param_dict, headers=header_dict)

    def idcode(self, header_dict=None, param_dict=None):
        '''
        实名认证操作
        :param param_dict:
        :return:
        '''
        return self.request("POST", self.IDCODE, headers=header_dict, params=param_dict)

    def save(self, param_dict=None, header_dict=None):
        '''
        修改用户昵称、头像操作

        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", self.SAVE, params=param_dict, headers=header_dict)

    def logout(self,header_dict=None,param_dict=None):
        '''
        用户ID登出

        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST",UserReq.LOGOUT,headers=header_dict,params=param_dict)

    def invitation(self,header_dict=None,param_dict=None):
        '''
        邀请码

        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST",UserReq.INVITATION,headers=header_dict,params=param_dict)

    def changemobile(self,header_dict=None,param_dict=None):
        '''
        修改手机号
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST",UserReq.CHANGEMOBILE,headers=header_dict,params=param_dict)

    def change_mobike_check(self, header_dict = None, param_diact = None):
        '''
        修改手机号检查
        :param header_dict:
        :param param_diact:
        :return:
        '''
        return self.request("GET", UserReq.CHANGE_MOBILE_CHECK, headers = header_dict, params = param_diact)

    def get_voice_captcha(self,header_dict=None,param_dict=None):
        '''
        语音验证码
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST",UserReq.VOICE_CAPTCHA,headers=header_dict,params=param_dict)

    def get_wallet_info(self,header_dict=None,param_dict=None):
        '''
        钱包信息
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return  self.request("POST",UserReq.WALLET_INFO,headers=header_dict,params=param_dict)

    def update_legal_age(self,header_dict=None,param_dict=None):
        '''
        确认为合法年龄
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST",UserReq.UPDATE_LEGAL_AGE,headers=header_dict,params=param_dict)

    def get_country_list(self,header_dict=None,param_dict=None):
        '''
        获取当前开城国家列表
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("GET",UserReq.GET_COUNTRY_LIST,headers=header_dict,params=param_dict)

    def select_country_region(self,header_dict=None,param_dict=None):
        '''
        用户选择所属国家
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST",UserReq.SELECT_COUNTRY_REGION,headers=header_dict,params=param_dict)

    def regist_free_deposit(self,header_dict=None,param_dict=None):
        '''
        注册免押金
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST",UserReq.REGIST_FREE_DEPOSIT,headers=header_dict,params=param_dict)

    def device_bind(self,header_dict=None,param_dict=None):
        '''
        设备绑定
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return  self.request("POST",UserReq.DEVICE_BIND,headers=header_dict,params=param_dict)

    def global_getinfo(self, header_dict=None, param_dict=None):
        '''
        获取海外用户扩展信息
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", "api/v2/globaluserextendinfo/getinfo.do", headers=header_dict, params=param_dict)

    def global_confirm_consent(self, header_dict=None, param_dict=None):
        '''
        海外用户确认免责条款
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", "api/v2/globaluserextendinfo/confirmconsent.do", headers=header_dict, params=param_dict)


    def uuid_bind(self, header_dict=None, param_dict=None):
        '''
        uuid绑定
        :param header_dict:
        :param param_dict:
        :return:
        '''
        return self.request("POST", UserReq.UUID_BIND, headers=header_dict, params=param_dict)

    def usermgr_changeextendinfo(self, param_dict=None, header_dict=None):
        '''
        修改用户信息
        '''
        return self.request("POST", UserReq.CHANGE_EXTENDINFO, params=param_dict, headers=header_dict)

    def usermgr_checkpassword(self, param_dict=None, header_dict=None):
        '''
        校验用户密码
        '''
        return self.request("POST", UserReq.CHECK_PASSWORD, params=param_dict, headers=header_dict)

    def usermgr_checkverifycode(self, param_dict=None, header_dict=None):
        '''
        校验用户验证码
        '''
        return self.request("POST", UserReq.CHECK_VERIFYCODE, params=param_dict, headers=header_dict)
