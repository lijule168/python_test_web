from lib.mbmanage.requestmanage.base_req import BaseReq

class I18nObReq(BaseReq):
    def __init__(self):
        super(I18nObReq, self).__init__()

    def i18nob_deposit(self, header_dict=None):
        '''
        国外OB流程押金页面
        '''
        return self.request("POST", "api/v2/i18nOB/deposit", headers=header_dict)

    def saveTrialRecord(self, header_dict=None):
        '''
        saveTrialRecord
        '''
        return self.request("POST", "api/v2/i18nOB/saveTrialRecord", headers=header_dict)

