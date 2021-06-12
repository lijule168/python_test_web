#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.mbmanage.requestmanage.base_req import BaseReq

#code generate by tools, any problem please contact dingbaixia@mobike.com

class FaultsReq(BaseReq):
    def __init__(self):
        super(FaultsReq, self).__init__()

    def faults_getbiketype(self, param_dict=None, header_dict=None):
        '''
        根据自行车编号获取自行车类型
        '''
        return self.request("GET", "api/v2/faults/getBikeType.do", params=param_dict, headers=header_dict)

    def faults_report(self, param_dict=None, header_dict=None):
        '''
        上报异常
        '''
        return self.request("GET", "api/v2/faults/report.do", params=param_dict, headers=header_dict)

    def faults_reportfault(self, param_dict=None, header_dict=None):
        '''
        上报异常多图片
        '''
        return self.request("POST", "api/v2/faults/reportFault.do", params=param_dict, headers=header_dict)

    def faults_getopencityfaultconfig(self, param_dict=None, header_dict=None):
        '''
        获取是否新旧城市和故障配置
        '''
        return self.request("POST", "api/v2/faults/getOpenCityFaultConfig.do", params=param_dict, headers=header_dict)
