#!/usr/bin/python
# -*- coding:utf-8 -*-
from lib.util.log_util import l


class MBKTask:
    taskid = None
    userid = None
    region_dc_code = None
    region_country_code = None
    roaming_dc_code = None
    roaming_country_code = None
    previous_dc_code = None
    previous_country_code = None
    transfer_status = None
    task_type = None
    status = None
    remark = None
    lat = None
    lon = None
    roamingid = None
    new_token = None
    ext = None
    id = None
    updated_at = None
    created_at = None
    select_column = "taskid,userid,region_dc_code,region_country_code,roaming_dc_code,roaming_country_code,previous_dc_code,previous_country_code,transfer_status,task_type,status,remark,lat,lon,roamingid,new_token,ext,id,updated_at,created_at"

    def __eq__(self, other):
        result = True
        if other.taskid != self.taskid:
            l.debug("MBKTask-taskid-不一致，self({0}), other({1})".format(self.taskid, other.taskid))
            result = False
        if other.userid != self.userid:
            l.debug("MBKTask-userid-不一致，self({0}), other({1})".format(self.userid, other.userid))
            result = False
        if other.region_dc_code != self.region_dc_code:
            l.debug("MBKTask-region_dc_code-不一致，self({0}), other({1})".format(self.region_dc_code, other.region_dc_code))
            result = False
        if other.region_country_code != self.region_country_code:
            l.debug("MBKTask-region_country_code-不一致，self({0}), other({1})".format(self.region_country_code, other.region_country_code))
            result = False
        if other.roaming_dc_code != self.roaming_dc_code:
            l.debug("MBKTask-roaming_dc_code-不一致，self({0}), other({1})".format(self.roaming_dc_code, other.roaming_dc_code))
            result = False
        if other.roaming_country_code != self.roaming_country_code:
            l.debug("MBKTask-roaming_country_code-不一致，self({0}), other({1})".format(self.roaming_country_code, other.roaming_country_code))
            result = False
        if other.previous_dc_code != self.previous_dc_code:
            l.debug("MBKTask-previous_dc_code-不一致，self({0}), other({1})".format(self.previous_dc_code, other.previous_dc_code))
            result = False
        if other.previous_country_code != self.previous_country_code:
            l.debug("MBKTask-previous_country_code-不一致，self({0}), other({1})".format(self.previous_country_code, other.previous_country_code))
            result = False
        if other.transfer_status != self.transfer_status:
            l.debug("MBKTask-transfer_status-不一致，self({0}), other({1})".format(self.transfer_status, other.transfer_status))
            result = False
        if other.task_type != self.task_type:
            l.debug("MBKTask-task_type-不一致，self({0}), other({1})".format(self.task_type, other.task_type))
            result = False
        if other.status != self.status:
            l.debug("MBKTask-status-不一致，self({0}), other({1})".format(self.status, other.status))
            result = False
        if other.remark != self.remark:
            l.debug("MBKTask-remark-不一致，self({0}), other({1})".format(self.remark, other.remark))
            result = False
        if other.lat != self.lat:
            l.debug("MBKTask-lat-不一致，self({0}), other({1})".format(self.lat, other.lat))
            result = False
        if other.lon != self.lon:
            l.debug("MBKTask-lon-不一致，self({0}), other({1})".format(self.lon, other.lon))
            result = False
        if other.roamingid != self.roamingid:
            l.debug("MBKTask-roamingid-不一致，self({0}), other({1})".format(self.roamingid, other.roamingid))
            result = False
        if other.new_token != self.new_token:
            l.debug("MBKTask-new_token-不一致，self({0}), other({1})".format(self.new_token, other.new_token))
            result = False
        if other.ext != self.ext:
            l.debug("MBKTask-ext-不一致，self({0}), other({1})".format(self.ext, other.ext))
            result = False
        if other.id != self.id:
            l.debug("MBKTask-id-不一致，self({0}), other({1})".format(self.id, other.id))
            result = False
        if other.updated_at != self.updated_at:
            l.debug("MBKTask-updated_at-不一致，self({0}), other({1})".format(self.updated_at, other.updated_at))
            result = False
        if other.created_at != self.created_at:
            l.debug("MBKTask-created_at-不一致，self({0}), other({1})".format(self.created_at, other.created_at))
            result = False
        return result

    def __ne__(self, other):
        return not self.__eq__(other)

