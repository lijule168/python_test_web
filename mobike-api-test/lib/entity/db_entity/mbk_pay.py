from lib.entity.db_entity.base_entity import BaseEntity
from lib.util.log_util import l

class MBKDepositInfo:
    DEPOSIT_ID = None
    USER_ID = None
    RMB = None
    TS = None
    CASH_SOURCE = None
    ISDELETE = None
    TIMELINESS = None
    CREATE_TIME = None
    UPDATE_TIME = None
    OPERATOR_ID = None
    STATUS = None
    ORDER_ID_FIRST = None
    ORDER_ID_SOURCE = None
    ORDER_ID_REFUND = None
    MOBILENO = None
    CURRENCY = None
    COUNTRY_CODE = None
    CITYCODE = None
    EXTEND1 = None
    EXTEND2 = None
    PAY_CHANNEL = None
    select_column = "DEPOSIT_ID,USER_ID,RMB,TS,CASH_SOURCE,ISDELETE,TIMELINESS,CREATE_TIME,UPDATE_TIME,OPERATOR_ID,STATUS,ORDER_ID_FIRST,ORDER_ID_SOURCE,ORDER_ID_REFUND,MOBILENO,CURRENCY,COUNTRY_CODE,CITYCODE,EXTEND1,EXTEND2,PAY_CHANNEL"

    def __eq__(self, other):
        result = True
        if other.DEPOSIT_ID != self.DEPOSIT_ID:
            l.debug("MBKDepositInfo-DEPOSIT_ID-不一致，self({0}), other({1})".format(self.DEPOSIT_ID, other.DEPOSIT_ID))
            #result = False
        if other.USER_ID != self.USER_ID:
            l.debug("MBKDepositInfo-USER_ID-不一致，self({0}), other({1})".format(self.USER_ID, other.USER_ID))
            result = False
        if other.RMB != self.RMB:
            l.debug("MBKDepositInfo-RMB-不一致，self({0}), other({1})".format(self.RMB, other.RMB))
            result = False
        if other.TS != self.TS:
            l.debug("MBKDepositInfo-TS-不一致，self({0}), other({1})".format(self.TS, other.TS))
            result = False
        if other.CASH_SOURCE != self.CASH_SOURCE:
            l.debug("MBKDepositInfo-CASH_SOURCE-不一致，self({0}), other({1})".format(self.CASH_SOURCE, other.CASH_SOURCE))
            result = False
        if other.ISDELETE != self.ISDELETE:
            l.debug("MBKDepositInfo-ISDELETE-不一致，self({0}), other({1})".format(self.ISDELETE, other.ISDELETE))
            result = False
        if other.TIMELINESS != self.TIMELINESS:
            l.debug("MBKDepositInfo-TIMELINESS-不一致，self({0}), other({1})".format(self.TIMELINESS, other.TIMELINESS))
            result = False
        if other.CREATE_TIME != self.CREATE_TIME:
            l.debug("MBKDepositInfo-CREATE_TIME-不一致，self({0}), other({1})".format(self.CREATE_TIME, other.CREATE_TIME))
            result = False
        if other.UPDATE_TIME != self.UPDATE_TIME:
            l.debug("MBKDepositInfo-UPDATE_TIME-不一致，self({0}), other({1})".format(self.UPDATE_TIME, other.UPDATE_TIME))
            result = False
        if other.OPERATOR_ID != self.OPERATOR_ID:
            l.debug("MBKDepositInfo-OPERATOR_ID-不一致，self({0}), other({1})".format(self.OPERATOR_ID, other.OPERATOR_ID))
            result = False
        if other.STATUS != self.STATUS:
            l.debug("MBKDepositInfo-STATUS-不一致，self({0}), other({1})".format(self.STATUS, other.STATUS))
            result = False
        if other.ORDER_ID_FIRST != self.ORDER_ID_FIRST:
            l.debug("MBKDepositInfo-ORDER_ID_FIRST-不一致，self({0}), other({1})".format(self.ORDER_ID_FIRST, other.ORDER_ID_FIRST))
            result = False
        if other.ORDER_ID_SOURCE != self.ORDER_ID_SOURCE:
            l.debug("MBKDepositInfo-ORDER_ID_SOURCE-不一致，self({0}), other({1})".format(self.ORDER_ID_SOURCE, other.ORDER_ID_SOURCE))
            result = False
        if other.ORDER_ID_REFUND != self.ORDER_ID_REFUND:
            l.debug("MBKDepositInfo-ORDER_ID_REFUND-不一致，self({0}), other({1})".format(self.ORDER_ID_REFUND, other.ORDER_ID_REFUND))
            result = False
        if other.MOBILENO != self.MOBILENO:
            l.debug("MBKDepositInfo-MOBILENO-不一致，self({0}), other({1})".format(self.MOBILENO, other.MOBILENO))
            result = False
        if other.CURRENCY != self.CURRENCY:
            l.debug("MBKDepositInfo-CURRENCY-不一致，self({0}), other({1})".format(self.CURRENCY, other.CURRENCY))
            result = False
        if other.COUNTRY_CODE != self.COUNTRY_CODE:
            l.debug("MBKDepositInfo-COUNTRY_CODE-不一致，self({0}), other({1})".format(self.COUNTRY_CODE, other.COUNTRY_CODE))
            result = False
        if other.CITYCODE != self.CITYCODE:
            l.debug("MBKDepositInfo-CITYCODE-不一致，self({0}), other({1})".format(self.CITYCODE, other.CITYCODE))
            result = False
        if other.EXTEND1 != self.EXTEND1:
            l.debug("MBKDepositInfo-EXTEND1-不一致，self({0}), other({1})".format(self.EXTEND1, other.EXTEND1))
            result = False
        if other.EXTEND2 != self.EXTEND2:
            l.debug("MBKDepositInfo-EXTEND2-不一致，self({0}), other({1})".format(self.EXTEND2, other.EXTEND2))
            result = False
        if other.PAY_CHANNEL != self.PAY_CHANNEL:
            l.debug("MBKDepositInfo-PAY_CHANNEL-不一致，self({0}), other({1})".format(self.PAY_CHANNEL, other.PAY_CHANNEL))
            result = False
        return result

    def __ne__(self, other):
        return not self.__eq__(other)


class MBKBalance(BaseEntity):
    USERID = None
    DEPOSIT = None
    BALANCE = None
    TS = None
    ISDELETE = None
    TIMELINESS = None
    MOBILENO = None
    COUNTRY_CODE = None
    CITYCODE = None
    CURRENCY = None
    EXTEND1 = None
    EXTEND2 = None
    select_column = "USERID,DEPOSIT,BALANCE,TS,ISDELETE,TIMELINESS,MOBILENO,COUNTRY_CODE,CITYCODE,CURRENCY,EXTEND1,EXTEND2"

    def __eq__(self, other):
        result = True
        if other.USERID != self.USERID:
            l.debug("MBKBalance-USERID-不一致，self({0}), other({1})".format(self.USERID, other.USERID))
            result = False
        if other.DEPOSIT != self.DEPOSIT:
            l.debug("MBKBalance-DEPOSIT-不一致，self({0}), other({1})".format(self.DEPOSIT, other.DEPOSIT))
            result = False
        if other.BALANCE != self.BALANCE:
            l.debug("MBKBalance-BALANCE-不一致，self({0}), other({1})".format(self.BALANCE, other.BALANCE))
            result = False
        if other.TS != self.TS:
            l.debug("MBKBalance-TS-不一致，self({0}), other({1})".format(self.TS, other.TS))
            result = False
        if other.ISDELETE != self.ISDELETE:
            l.debug("MBKBalance-ISDELETE-不一致，self({0}), other({1})".format(self.ISDELETE, other.ISDELETE))
            result = False
        if other.TIMELINESS != self.TIMELINESS:
            l.debug("MBKBalance-TIMELINESS-不一致，self({0}), other({1})".format(self.TIMELINESS, other.TIMELINESS))
            result = False
        if other.MOBILENO != self.MOBILENO:
            l.debug("MBKBalance-MOBILENO-不一致，self({0}), other({1})".format(self.MOBILENO, other.MOBILENO))
            result = False
        if other.COUNTRY_CODE != self.COUNTRY_CODE:
            l.debug("MBKBalance-COUNTRY_CODE-不一致，self({0}), other({1})".format(self.COUNTRY_CODE, other.COUNTRY_CODE))
            result = False
        if other.CITYCODE != self.CITYCODE:
            l.debug("MBKBalance-CITYCODE-不一致，self({0}), other({1})".format(self.CITYCODE, other.CITYCODE))
            result = False
        if other.CURRENCY != self.CURRENCY:
            l.debug("MBKBalance-CURRENCY-不一致，self({0}), other({1})".format(self.CURRENCY, other.CURRENCY))
            result = False
        if other.EXTEND1 != self.EXTEND1:
            l.debug("MBKBalance-EXTEND1-不一致，self({0}), other({1})".format(self.EXTEND1, other.EXTEND1))
            result = False
        if other.EXTEND2 != self.EXTEND2:
            l.debug("MBKBalance-EXTEND2-不一致，self({0}), other({1})".format(self.EXTEND2, other.EXTEND2))
            result = False
        return result

    def __ne__(self, other):
        return not self.__eq__(other)

