from lib.entity.microservice_name import MicroServiceName
from lib.mbmanage.requestmanage.base_req import BaseReq

__author__ = "dingbaixia@mobike.com"

class HttpDNSReq(BaseReq):
    def __init__(self):
        super(HttpDNSReq, self).__init__(micro_service_name=MicroServiceName.HTTPDNS)

    def httpdns_lac(self, param_dict={}):
        """
        根据经纬度，解析给定的域名，并返回解析后的结果，如果参数错误，返回原始域名
        :param param_dict:
        :return:
        """
        return self.request("GET", "domainmap/loc", params=param_dict)

    def httpdns_refresh(self):
        """
        刷新缓存，用于快速更新配置
        :return:
        """
        return self.request("GET", "domainmap/refresh")