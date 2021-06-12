from lib.util.log_util import l


class MBKUserRoaming:
    id = None
    roaming_id = None
    user_id = None
    mobile = None
    region_country_code = None
    region_city_code = None
    region_dc_code = None
    roaming_country_code = None
    roaming_city_code = None
    roaming_dc_code = None
    roaming_state = None
    roaming_result = None
    create_time = None
    finish_time = None
    clear_time = None
    remark = None
    args = None
    ext = None
    select_column = "id,roaming_id,user_id,mobile,region_country_code,region_city_code,region_dc_code,roaming_country_code,roaming_city_code,roaming_dc_code,roaming_state,roaming_result,create_time,finish_time,clear_time,remark,args,ext"

    def __eq__(self, other):
        result = True
        if other.id != self.id:
            l.debug("MBKUserRoaming-id-不一致，self({0}), other({1})".format(self.id, other.id))
            result = False
        if other.roaming_id != self.roaming_id:
            l.debug("MBKUserRoaming-roaming_id-不一致，self({0}), other({1})".format(self.roaming_id, other.roaming_id))
            result = False
        if other.user_id != self.user_id:
            l.debug("MBKUserRoaming-user_id-不一致，self({0}), other({1})".format(self.user_id, other.user_id))
            result = False
        if other.mobile != self.mobile:
            l.debug("MBKUserRoaming-mobile-不一致，self({0}), other({1})".format(self.mobile, other.mobile))
            result = False
        if other.region_country_code != self.region_country_code:
            l.debug("MBKUserRoaming-region_country_code-不一致，self({0}), other({1})".format(self.region_country_code, other.region_country_code))
            result = False
        if other.region_city_code != self.region_city_code:
            l.debug("MBKUserRoaming-region_city_code-不一致，self({0}), other({1})".format(self.region_city_code, other.region_city_code))
            result = False
        if other.region_dc_code != self.region_dc_code:
            l.debug("MBKUserRoaming-region_dc_code-不一致，self({0}), other({1})".format(self.region_dc_code, other.region_dc_code))
            result = False
        if other.roaming_country_code != self.roaming_country_code:
            l.debug("MBKUserRoaming-roaming_country_code-不一致，self({0}), other({1})".format(self.roaming_country_code, other.roaming_country_code))
            result = False
        if other.roaming_city_code != self.roaming_city_code:
            l.debug("MBKUserRoaming-roaming_city_code-不一致，self({0}), other({1})".format(self.roaming_city_code, other.roaming_city_code))
            result = False
        if other.roaming_dc_code != self.roaming_dc_code:
            l.debug("MBKUserRoaming-roaming_dc_code-不一致，self({0}), other({1})".format(self.roaming_dc_code, other.roaming_dc_code))
            result = False
        if other.roaming_state != self.roaming_state:
            l.debug("MBKUserRoaming-roaming_state-不一致，self({0}), other({1})".format(self.roaming_state, other.roaming_state))
            result = False
        if other.roaming_result != self.roaming_result:
            l.debug("MBKUserRoaming-roaming_result-不一致，self({0}), other({1})".format(self.roaming_result, other.roaming_result))
            result = False
        if other.create_time != self.create_time:
            l.debug("MBKUserRoaming-create_time-不一致，self({0}), other({1})".format(self.create_time, other.create_time))
            result = False
        if other.finish_time != self.finish_time:
            l.debug("MBKUserRoaming-finish_time-不一致，self({0}), other({1})".format(self.finish_time, other.finish_time))
            result = False
        if other.clear_time != self.clear_time:
            l.debug("MBKUserRoaming-clear_time-不一致，self({0}), other({1})".format(self.clear_time, other.clear_time))
            result = False
        if other.remark != self.remark:
            l.debug("MBKUserRoaming-remark-不一致，self({0}), other({1})".format(self.remark, other.remark))
            result = False
        if other.args != self.args:
            l.debug("MBKUserRoaming-args-不一致，self({0}), other({1})".format(self.args, other.args))
            result = False
        if other.ext != self.ext:
            l.debug("MBKUserRoaming-ext-不一致，self({0}), other({1})".format(self.ext, other.ext))
            result = False
        return result

    def __ne__(self, other):
        return not self.__eq__(other)

