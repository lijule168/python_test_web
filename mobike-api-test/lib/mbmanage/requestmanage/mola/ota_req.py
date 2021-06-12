__author__ = 'dingbaixia@mobike.com'

from lib.mbmanage.requestmanage.base_req import BaseReq


class OtaReq(BaseReq):

    def __init__(self):
        super(OtaReq, self).__init__()

    def auth(self, param_dict=None):
        """
        权鉴
        :param param_dict:
        :return:
        """

        return self.request("GET", "mola/ota/auth.do", params=param_dict)

    def getOtaInfo(self, param_dict=None):
        """
        获取ota信息
        :param param_dict:
        :return:
        """

        return self.request("GET", "mola/ota/getOtaInfo.do", params=param_dict)

    def otaKey(self, param_dict=None):
        """
        根据otakey获取rom
        :param param_dict:
        :return:
        """
        return self.request("GET", "mola/ota/otaKey.do", params=param_dict)