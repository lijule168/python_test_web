from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

__author__ = "dingbaixia@mobike.com"

class MusTangReq(BaseReq):
    def __init__(self):
        #super(MusTangReq, self).__init__(micro_service_name=MicroServiceName.MUSHTANG)
        super(MusTangReq, self).__init__()

    def roamingstart(self, header_dict, param_dict):
        """
        开始路由数据
        :param json_dict:
        :return:
        """
        return self.request("POST", "api/mustang/roamingstart", headers=header_dict, json_data=param_dict)

    def checkroaming(self, header_dict, param_dict):
        """
        检查是否为跨区域用户
        :param json_dict:
        :return:
        """
        return self.request("POST", "api/mustang/checkroaming", headers=header_dict, json_data=param_dict)

    def transfer(self, param_dict):
        """
        检查是否为跨区域用户
        :param json_dict:
        :return:
        """
        return self.request("POST", "transfer", json_data=param_dict)

    def transferByService(self, param_dict):
        """
        检查是否为跨区域用户
        :param json_dict:
        :return:
        """
        return self.request("POST", "transferByService", json_data=param_dict)