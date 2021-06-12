#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class CarUserReq(BaseReq):
    def __init__(self):
        super(CarUserReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_API)

    def getuserauditinfo(self , param_dict=None):
        '''
        获取用户资质信息  code=> 0:成功
  500:内部异常
 250:用户未登录
 41000:用户不存在 41005:用户缺少必填信息
        '''
        return self.request("POST", "user/getUserAuditInfo", params=param_dict)

    def submitideninfo(self , param_dict=None):
        '''
        提交身份证信息   code=> 0:成功
          500:内部异常
         250:用户未登录
         41000:用户不存在 41001:用户身份证状态不能提交审核  41003:新上传填写的姓名&身份证号和原有信息不一致 41005:用户缺少必填信息
                '''
        return self.request("POST", "user/submitIdenInfo", params=param_dict)

    def submitdrivinginfo(self , param_dict=None):
        '''
        提交驾照信息 code=> 0:成功
  500:内部异常
 250:用户未登录
 41000:用户不存在 41002:用户驾照状态不能提交审核 41005:用户缺少必填信息 41011:档案号已被他人占用
        '''
        return self.request("POST", "user/submitDrivingInfo", params=param_dict)

