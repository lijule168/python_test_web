#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.entity.db_entity.base_entity import BaseEntity
from lib.util.log_util import l


class MBKGlobalUser(BaseEntity):
    userId = None
    agreeMarketing = None
    meetLegalAge = None
    stripeCountry = None
    agree_to_sms = None
    agree_to_push = None
    agree_to_email = None
    create_time = None
    update_time = None
    agree_to_required_consent = None
    select_column = "userId,agreeMarketing,meetLegalAge,stripeCountry,agree_to_sms,agree_to_push,agree_to_email,create_time,update_time,agree_to_required_consent"

    def __eq__(self, other):
        result = True
        if other.agree_to_required_consent != self.agree_to_required_consent:
            l.debug("MBKGlobalUser-agree_to_required_consent-不一致，self({0}), other({1})".format(self.agree_to_required_consent, other.agree_to_required_consent))
            result = False
        if other.update_time != self.update_time:
            l.debug("MBKGlobalUser-update_time-不一致，self({0}), other({1})".format(self.update_time, other.update_time))
            result = False
        if other.create_time != self.create_time:
            l.debug("MBKGlobalUser-create_time-不一致，self({0}), other({1})".format(self.create_time, other.create_time))
            result = False
        if other.agree_to_email != self.agree_to_email:
            l.debug("MBKGlobalUser-agree_to_email-不一致，self({0}), other({1})".format(self.agree_to_email, other.agree_to_email))
            result = False
        if other.agree_to_push != self.agree_to_push:
            l.debug("MBKGlobalUser-agree_to_push-不一致，self({0}), other({1})".format(self.agree_to_push, other.agree_to_push))
            result = False
        if other.agree_to_sms != self.agree_to_sms:
            l.debug("MBKGlobalUser-agree_to_sms-不一致，self({0}), other({1})".format(self.agree_to_sms, other.agree_to_sms))
            result = False
        if other.stripeCountry != self.stripeCountry:
            l.debug("MBKGlobalUser-stripeCountry-不一致，self({0}), other({1})".format(self.stripeCountry, other.stripeCountry))
            result = False
        if other.meetLegalAge != self.meetLegalAge:
            l.debug("MBKGlobalUser-meetLegalAge-不一致，self({0}), other({1})".format(self.meetLegalAge, other.meetLegalAge))
            result = False
        if other.agreeMarketing != self.agreeMarketing:
            l.debug("MBKGlobalUser-agreeMarketing-不一致，self({0}), other({1})".format(self.agreeMarketing, other.agreeMarketing))
            result = False
        if other.userId != self.userId:
            l.debug("MBKGlobalUser-userId-不一致，self({0}), other({1})".format(self.userId, other.userId))
            result = False
        return result

    def __ne__(self, other):
        return not self.__eq__(other)

class MBKUsers(BaseEntity):
    USERID = None
    USERNAME = None
    USERPWD = None
    MOBILENO = None
    EMAIL = None
    REGISTERTIME = None
    USERIMAGE = None
    GENDER = None
    ADDR = None
    AGE = None
    FAILEDTIMES = None
    LOCKEDTIME = None
    PUSHKEY = None
    AUTHTOKEN = None
    LASTACTIVETIME = None
    TS = None
    ISDELETE = None
    TIMELINESS = None
    PLATFORM = None
    ID_CODE = None
    TAG = None
    PROGRESS = None
    IMG = None
    NATION = None
    status = None
    bz = None
    CITYCODE = None
    AREACODE = None
    SCHOOLCODE = None
    STRIPE_ID = None
    COUNTRY_CODE = None
    OS_PLATFORM = None
    SOURCE = None
    SUB_SOURCE = None
    EXTEND1 = None
    EXTEND2 = None
    select_column = "COUNTRY_CODE,OS_PLATFORM,SOURCE,SUB_SOURCE,EXTEND1,USERID,USERNAME,USERPWD,MOBILENO,EMAIL," \
                    "REGISTERTIME,USERIMAGE,GENDER,ADDR,AGE,FAILEDTIMES,LOCKEDTIME,PUSHKEY,AUTHTOKEN,LASTACTIVETIME," \
                    "TS,ISDELETE,TIMELINESS,PLATFORM,ID_CODE,TAG,PROGRESS,IMG,NATION,status,bz,CITYCODE,AREACODE,SCHOOLCODE,STRIPE_ID,EXTEND2"

    def __eq__(self, other):
        result = True
        if other.STRIPE_ID != self.STRIPE_ID:
            l.debug("MBKUSER对象-STRIPE_ID-不一致，self({0}), other({1})".format(self.STRIPE_ID, other.STRIPE_ID))
            result = False
        if other.SCHOOLCODE != self.SCHOOLCODE:
            l.debug("MBKUSER对象-SCHOOLCODE-不一致，self({0}), other({1})".format(self.SCHOOLCODE, other.SCHOOLCODE))
            result = False
        if other.AREACODE != self.AREACODE:
            l.debug("MBKUSER对象-AREACODE-不一致，self({0}), other({1})".format(self.AREACODE, other.AREACODE))
            result = False
        if other.CITYCODE != self.CITYCODE:
            l.debug("MBKUSER对象-CITYCODE-不一致，self({0}), other({1})".format(self.CITYCODE, other.CITYCODE))
            result = False
        if other.bz != self.bz:
            l.debug("MBKUSER对象-bz-不一致，self({0}), other({1})".format(self.bz, other.bz))
            result = False
        if other.status != self.status:
            l.debug("MBKUSER对象-status-不一致，self({0}), other({1})".format(self.status, other.status))
            result = False
        if other.NATION != self.NATION:
            l.debug("MBKUSER对象-NATION-不一致，self({0}), other({1})".format(self.NATION, other.NATION))
            result = False
        if other.IMG != self.IMG:
            l.debug("MBKUSER对象-IMG-不一致，self({0}), other({1})".format(self.IMG, other.IMG))
            result = False
        if other.PROGRESS != self.PROGRESS:
            l.debug("MBKUSER对象-PROGRESS-不一致，self({0}), other({1})".format(self.PROGRESS, other.PROGRESS))
            result = False
        if other.TAG != self.TAG:
            l.debug("MBKUSER对象-TAG-不一致，self({0}), other({1})".format(self.TAG, other.TAG))
            result = False
        if other.ID_CODE != self.ID_CODE:
            l.debug("MBKUSER对象-ID_CODE-不一致，self({0}), other({1})".format(self.ID_CODE, other.ID_CODE))
            result = False
        if other.PLATFORM != self.PLATFORM:
            l.debug("MBKUSER对象-PLATFORM-不一致，self({0}), other({1})".format(self.PLATFORM, other.PLATFORM))
            result = False
        if other.TIMELINESS != self.TIMELINESS:
            l.debug("MBKUSER对象-TIMELINESS-不一致，self({0}), other({1})".format(self.TIMELINESS, other.TIMELINESS))
            result = False
        if other.ISDELETE != self.ISDELETE:
            l.debug("MBKUSER对象-ISDELETE-不一致，self({0}), other({1})".format(self.ISDELETE, other.ISDELETE))
            result = False
        if other.TS != self.TS:
            l.debug("MBKUSER对象-TS-不一致，self({0}), other({1})".format(self.TS, other.TS))
            result = False
        if other.LASTACTIVETIME != self.LASTACTIVETIME:
            l.debug("MBKUSER对象-LASTACTIVETIME-不一致，self({0}), other({1})".format(self.LASTACTIVETIME, other.LASTACTIVETIME))
            result = False
        if other.AUTHTOKEN != self.AUTHTOKEN:
            l.debug("MBKUSER对象-AUTHTOKEN-不一致，self({0}), other({1})".format(self.AUTHTOKEN, other.AUTHTOKEN))
            result = False
        if other.PUSHKEY != self.PUSHKEY:
            l.debug("MBKUSER对象-PUSHKEY-不一致，self({0}), other({1})".format(self.PUSHKEY, other.PUSHKEY))
            result = False
        if other.LOCKEDTIME != self.LOCKEDTIME:
            l.debug("MBKUSER对象-LOCKEDTIME-不一致，self({0}), other({1})".format(self.LOCKEDTIME, other.LOCKEDTIME))
            result = False
        if other.FAILEDTIMES != self.FAILEDTIMES:
            l.debug("MBKUSER对象-FAILEDTIMES-不一致，self({0}), other({1})".format(self.FAILEDTIMES, other.FAILEDTIMES))
            result = False
        if other.AGE != self.AGE:
            l.debug("MBKUSER对象-AGE-不一致，self({0}), other({1})".format(self.AGE, other.AGE))
            result = False
        if other.ADDR != self.ADDR:
            l.debug("MBKUSER对象-ADDR-不一致，self({0}), other({1})".format(self.ADDR, other.ADDR))
            result = False
        if other.GENDER != self.GENDER:
            l.debug("MBKUSER对象-GENDER-不一致，self({0}), other({1})".format(self.GENDER, other.GENDER))
            result =  False
        if other.USERIMAGE != self.USERIMAGE:
            l.debug("MBKUSER对象-USERIMAGE-不一致，self({0}), other({1})".format(self.USERIMAGE, other.USERIMAGE))
            result =  False
        if other.REGISTERTIME != self.REGISTERTIME:
            l.debug("MBKUSER对象-REGISTERTIME-不一致，self({0}), other({1})".format(self.REGISTERTIME, other.REGISTERTIME))
            result =  False
        if other.EMAIL != self.EMAIL:
            l.debug("MBKUSER对象-EMAIL-不一致，self({0}), other({1})".format(self.EMAIL, other.EMAIL))
            result =  False
        if other.MOBILENO != self.MOBILENO:
            l.debug("MBKUSER对象-MOBILENO-不一致，self({0}), other({1})".format(self.MOBILENO, other.MOBILENO))
            result =  False
        if other.USERPWD != self.USERPWD:
            l.debug("MBKUSER对象-USERPWD-不一致，self({0}), other({1})".format(self.USERPWD, other.USERPWD))
            result =  False
        if other.USERNAME != self.USERNAME:
            l.debug("MBKUSER对象-USERNAME-不一致，self({0}), other({1})".format(self.USERNAME, other.USERNAME))
            result =  False
        if other.USERID != self.USERID:
            l.debug("MBKUSER对象-USERID-不一致，self({0}), other({1})".format(self.USERID, other.USERID))
            result =  False
        if other.SUB_SOURCE != self.SUB_SOURCE:
            l.debug("MBKUSER对象-SUB_SOURCE-不一致，self({0}), other({1})".format(self.SUB_SOURCE, other.SUB_SOURCE))
            result =  False
        if other.SOURCE != self.SOURCE:
            l.debug("MBKUSER对象-SOURCE-不一致，self({0}), other({1})".format(self.SOURCE, other.SOURCE))
            result =  False
        if other.OS_PLATFORM != self.OS_PLATFORM:
            l.debug("MBKUSER对象-OS_PLATFORM-不一致，self({0}), other({1})".format(self.OS_PLATFORM, other.OS_PLATFORM))
            result =  False
        if other.COUNTRY_CODE != self.COUNTRY_CODE:
            l.debug("MBKUSER对象-COUNTRY_CODE-不一致，self({0}), other({1})".format(self.COUNTRY_CODE, other.COUNTRY_CODE))
            result =  False
        if other.EXTEND2 != self.EXTEND2:
            l.debug("MBKUSER对象-EXTEND2-不一致，self({0}), other({1})".format(self.EXTEND2, other.EXTEND2))
            result =  False
        if other.EXTEND1 != self.EXTEND1:
            l.debug("MBKUSER对象-EXTEND1-不一致，self({0}), other({1})".format(self.EXTEND1, other.EXTEND1))
            result =  False
        return result

    def __ne__(self, other):
        return not self.__eq__(other)