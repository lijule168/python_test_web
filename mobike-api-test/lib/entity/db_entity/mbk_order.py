from lib.util.log_util import l

class MBKOrders:
    ORDERID = None
    USERID = None
    BIKEID = None
    STARTPOSITIONX = None
    STARTPOSITIONY = None
    STARTTIME = None
    TOTALDISTANCE = None
    CALORIE = None
    TOTALDURATION = None
    ENDTIME = None
    ENDPOSITIONX = None
    ENDPOSITIONY = None
    TOTALFEE = None
    RENTSTATUS = None
    LOCKMILISECONDS = None
    TS = None
    ISDELETE = None
    TIMELINESS = None
    PROGRESS = None
    CITYCODE = None
    AREACODE = None
    BIKETYPE = None
    COUNTRY_CODE = None
    CURRENCY = None
    OS_PLATFORM = None
    OS_VERSION = None
    SOURCE = None
    SUB_SOURCE = None
    APP_VERSION = None
    DEDUCTION_FEE = None
    EXTEND1 = None
    EXTEND2 = None
    select_column = "ORDERID,USERID,BIKEID,STARTPOSITIONX,STARTPOSITIONY,STARTTIME,TOTALDISTANCE,CALORIE,TOTALDURATION,ENDTIME,ENDPOSITIONX,ENDPOSITIONY,TOTALFEE,RENTSTATUS,LOCKMILISECONDS,TS,ISDELETE,TIMELINESS,PROGRESS,CITYCODE,AREACODE,BIKETYPE,COUNTRY_CODE,CURRENCY,OS_PLATFORM,OS_VERSION,SOURCE,SUB_SOURCE,APP_VERSION,DEDUCTION_FEE,EXTEND1,EXTEND2"

    def __eq__(self, other):
        result = True
        if other.ORDERID != self.ORDERID:
            l.debug("MBKOrders-ORDERID-不一致，self({0}), other({1})".format(self.ORDERID, other.ORDERID))
            result = False
        if other.USERID != self.USERID:
            l.debug("MBKOrders-USERID-不一致，self({0}), other({1})".format(self.USERID, other.USERID))
            result = False
        if other.BIKEID != self.BIKEID:
            l.debug("MBKOrders-BIKEID-不一致，self({0}), other({1})".format(self.BIKEID, other.BIKEID))
            result = False
        if other.STARTPOSITIONX != self.STARTPOSITIONX:
            l.debug("MBKOrders-STARTPOSITIONX-不一致，self({0}), other({1})".format(self.STARTPOSITIONX, other.STARTPOSITIONX))
            result = False
        if other.STARTPOSITIONY != self.STARTPOSITIONY:
            l.debug("MBKOrders-STARTPOSITIONY-不一致，self({0}), other({1})".format(self.STARTPOSITIONY, other.STARTPOSITIONY))
            result = False
        if other.STARTTIME != self.STARTTIME:
            l.debug("MBKOrders-STARTTIME-不一致，self({0}), other({1})".format(self.STARTTIME, other.STARTTIME))
            result = False
        if other.TOTALDISTANCE != self.TOTALDISTANCE:
            l.debug("MBKOrders-TOTALDISTANCE-不一致，self({0}), other({1})".format(self.TOTALDISTANCE, other.TOTALDISTANCE))
            result = False
        if other.CALORIE != self.CALORIE:
            l.debug("MBKOrders-CALORIE-不一致，self({0}), other({1})".format(self.CALORIE, other.CALORIE))
            result = False
        if other.TOTALDURATION != self.TOTALDURATION:
            l.debug("MBKOrders-TOTALDURATION-不一致，self({0}), other({1})".format(self.TOTALDURATION, other.TOTALDURATION))
            result = False
        if other.ENDTIME != self.ENDTIME:
            l.debug("MBKOrders-ENDTIME-不一致，self({0}), other({1})".format(self.ENDTIME, other.ENDTIME))
            result = False
        if other.ENDPOSITIONX != self.ENDPOSITIONX:
            l.debug("MBKOrders-ENDPOSITIONX-不一致，self({0}), other({1})".format(self.ENDPOSITIONX, other.ENDPOSITIONX))
            result = False
        if other.ENDPOSITIONY != self.ENDPOSITIONY:
            l.debug("MBKOrders-ENDPOSITIONY-不一致，self({0}), other({1})".format(self.ENDPOSITIONY, other.ENDPOSITIONY))
            result = False
        if other.TOTALFEE != self.TOTALFEE:
            l.debug("MBKOrders-TOTALFEE-不一致，self({0}), other({1})".format(self.TOTALFEE, other.TOTALFEE))
            result = False
        if other.RENTSTATUS != self.RENTSTATUS:
            l.debug("MBKOrders-RENTSTATUS-不一致，self({0}), other({1})".format(self.RENTSTATUS, other.RENTSTATUS))
            result = False
        if other.LOCKMILISECONDS != self.LOCKMILISECONDS:
            l.debug("MBKOrders-LOCKMILISECONDS-不一致，self({0}), other({1})".format(self.LOCKMILISECONDS, other.LOCKMILISECONDS))
            result = False
        if other.TS != self.TS:
            l.debug("MBKOrders-TS-不一致，self({0}), other({1})".format(self.TS, other.TS))
            result = False
        if other.ISDELETE != self.ISDELETE:
            l.debug("MBKOrders-ISDELETE-不一致，self({0}), other({1})".format(self.ISDELETE, other.ISDELETE))
            result = False
        if other.TIMELINESS != self.TIMELINESS:
            l.debug("MBKOrders-TIMELINESS-不一致，self({0}), other({1})".format(self.TIMELINESS, other.TIMELINESS))
            result = False
        if other.PROGRESS != self.PROGRESS:
            l.debug("MBKOrders-PROGRESS-不一致，self({0}), other({1})".format(self.PROGRESS, other.PROGRESS))
            result = False
        if other.CITYCODE != self.CITYCODE:
            l.debug("MBKOrders-CITYCODE-不一致，self({0}), other({1})".format(self.CITYCODE, other.CITYCODE))
            result = False
        if other.AREACODE != self.AREACODE:
            l.debug("MBKOrders-AREACODE-不一致，self({0}), other({1})".format(self.AREACODE, other.AREACODE))
            result = False
        if other.BIKETYPE != self.BIKETYPE:
            l.debug("MBKOrders-BIKETYPE-不一致，self({0}), other({1})".format(self.BIKETYPE, other.BIKETYPE))
            result = False
        if other.COUNTRY_CODE != self.COUNTRY_CODE:
            l.debug("MBKOrders-COUNTRY_CODE-不一致，self({0}), other({1})".format(self.COUNTRY_CODE, other.COUNTRY_CODE))
            result = False
        if other.CURRENCY != self.CURRENCY:
            l.debug("MBKOrders-CURRENCY-不一致，self({0}), other({1})".format(self.CURRENCY, other.CURRENCY))
            result = False
        if other.OS_PLATFORM != self.OS_PLATFORM:
            l.debug("MBKOrders-OS_PLATFORM-不一致，self({0}), other({1})".format(self.OS_PLATFORM, other.OS_PLATFORM))
            result = False
        if other.OS_VERSION != self.OS_VERSION:
            l.debug("MBKOrders-OS_VERSION-不一致，self({0}), other({1})".format(self.OS_VERSION, other.OS_VERSION))
            result = False
        if other.SOURCE != self.SOURCE:
            l.debug("MBKOrders-SOURCE-不一致，self({0}), other({1})".format(self.SOURCE, other.SOURCE))
            result = False
        if other.SUB_SOURCE != self.SUB_SOURCE:
            l.debug("MBKOrders-SUB_SOURCE-不一致，self({0}), other({1})".format(self.SUB_SOURCE, other.SUB_SOURCE))
            result = False
        if other.APP_VERSION != self.APP_VERSION:
            l.debug("MBKOrders-APP_VERSION-不一致，self({0}), other({1})".format(self.APP_VERSION, other.APP_VERSION))
            result = False
        if other.DEDUCTION_FEE != self.DEDUCTION_FEE:
            l.debug("MBKOrders-DEDUCTION_FEE-不一致，self({0}), other({1})".format(self.DEDUCTION_FEE, other.DEDUCTION_FEE))
            result = False
        if other.EXTEND1 != self.EXTEND1:
            l.debug("MBKOrders-EXTEND1-不一致，self({0}), other({1})".format(self.EXTEND1, other.EXTEND1))
            result = False
        if other.EXTEND2 != self.EXTEND2:
            l.debug("MBKOrders-EXTEND2-不一致，self({0}), other({1})".format(self.EXTEND2, other.EXTEND2))
            result = False
        return result

    def __ne__(self, other):
        return not self.__eq__(other)

