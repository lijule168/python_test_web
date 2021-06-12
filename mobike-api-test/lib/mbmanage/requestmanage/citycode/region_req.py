__author__ = 'dingbaixia@mobike.com'

from lib.mbmanage.requestmanage.base_req import BaseReq
from lib.entity.microservice_name import MicroServiceName

class RegionReq(BaseReq):
    def __init__(self):
        super(RegionReq, self).__init__(micro_service_name=MicroServiceName.CITY_CODE)

    def getRegionByGC(self, param_dict):
        """
        通过经纬度获取region信息
        :param param_dict:
        :return:
        """
        return self.request("GET", "region/getRegionByGC", params=param_dict)

    def getRegionCodeByCountryCode(self, param_dict):
        """
        通过国家代码获取region代码
        :param param_dict:
        :return:
        """
        return self.request("GET", "region/getRegionCodeByCountryCode", params=param_dict)