#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class QualificationReq(BaseReq):
    def __init__(self):
        super(QualificationReq, self).__init__(micro_service_name=MicroServiceName.MOCAR_INTERNAL_API)

    def hasqualifications(self, param_dict=None):
        '''
        查看用户是否能够满足资格 - 各项认证结果
        '''
        return self.request("GET", "qualification/user/hasQualifications.do", params=param_dict)

    def disapproveddrivinglicense(self, param_dict=None):
        '''
        用户驾驶证审核不通过
        '''
        return self.request("POST", "qualification/user/disapprovedDrivingLicense.do", params=param_dict)

    def passidcard(self, param_dict=None):
        '''
        用户身份证审核通过
        '''
        return self.request("POST", "qualification/user/passIdCard.do", params=param_dict)

    def idcard(self, param_dict=None):
        '''
        查看用户身份证
        '''
        return self.request("GET", "qualification/user/idCard.do", params=param_dict)

    def passdrivinglicense(self, param_dict=None):
        '''
        用户驾驶证审核通过
        '''
        return self.request("POST", "qualification/user/passDrivingLicense.do", params=param_dict)

    def drivinglicense(self, param_dict=None):
        '''
        查看用户驾驶证
        '''
        return self.request("GET", "qualification/user/drivingLicense.do", params=param_dict)

    def listwait4audit(self, param_dict=None):
        '''
        *查看待审核用户
        '''
        return self.request("GET", "qualification/user/listWait4Audit.do", params=param_dict)

    def auditfailurereason(self, param_dict=None):
        '''
        *审核失败原因
        '''
        return self.request("GET", "qualification/user/auditFailureReason.do", params=param_dict)

    def disapprovedidcard(self, param_dict=None):
        '''
        用户身份证审核不通过
        '''
        return self.request("POST", "qualification/user/disapprovedIdCard.do", params=param_dict)

    def auditworkorderlist(self, param_dict=None):
        '''
        *审核工单列表 - 已处理
        '''
        return self.request("GET", "qualification/user/auditWorkOrderList.do", params=param_dict)

    def certificateinfo(self, param_dict=None):
        '''
        *查看用户证件
        '''
        return self.request("GET", "qualification/user/certificateInfo.do", params=param_dict)

    def hasactive(self, param_dict=None):
        '''
        *查看已开放城市
        '''
        return self.request("GET", "qualification/city/hasActive.do", params=param_dict)

    def auditcertificate(self, param_dict=None):
        '''
        *审核用户证件
        '''
        return self.request("POST", "qualification/user/auditCertificate.do", params=param_dict)

    def workorderinfo(self, param_dict=None):
        '''
        *查看已处理证件详情
        '''
        return self.request("GET", "qualification/user/workOrderInfo.do", params=param_dict)

    def newactive(self, param_dict=None):
        '''
        新增开放城市
        '''
        return self.request("POST", "qualification/city/newActive.do", params=param_dict)

