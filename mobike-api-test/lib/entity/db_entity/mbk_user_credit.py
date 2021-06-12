from lib.util.log_util import l


class MBKMembership:
    user_id = None
    user_name = None
    city_code = None
    country_code = None
    mobile_no = None
    level = None
    crt_time = None
    free_time = None
    member_time = None
    quit_time = None
    super_time = None
    upd_time = None
    is_delete = None
    select_column = "user_id,user_name,city_code,country_code,mobile_no,level,crt_time,free_time,member_time,quit_time,super_time,upd_time,is_delete"
    
    def __eq__(self, other):
        result = True
        if other.user_id != self.user_id:
            l.debug("MBKMembership-user_id-不一致，self({0}), other({1})".format(self.user_id, other.user_id))
            result = False
        if other.city_code != self.city_code:
            l.debug("MBKMembership-city_code-不一致，self({0}), other({1})".format(self.city_code, other.city_code))
            result = False
        if other.user_name != self.user_name:
            l.debug("MBKMembership-user_name-不一致，self({0}), other({1})".format(self.user_name, other.user_name))
            result = False
        if other.country_code != self.country_code:
            l.debug("MBKMembership-country_code-不一致，self({0}), other({1})".format(self.country_code, other.country_code))
            result = False
        if other.mobile_no != self.mobile_no:
            l.debug("MBKMembership-mobile_no-不一致，self({0}), other({1})".format(self.mobile_no, other.mobile_no))
            result = False
        if other.level != self.level:
            l.debug("MBKMembership-level-不一致，self({0}), other({1})".format(self.level, other.level))
            result = False
        if other.crt_time != self.crt_time:
            l.debug("MBKMembership-crt_time-不一致，self({0}), other({1})".format(self.crt_time, other.crt_time))
            result = False
        if other.free_time != self.free_time:
            l.debug("MBKMembership-free_time-不一致，self({0}), other({1})".format(self.free_time, other.free_time))
            result = False
        if other.member_time != self.member_time:
            l.debug("MBKMembership-member_time-不一致，self({0}), other({1})".format(self.member_time, other.member_time))
            result = False
        if other.super_time != self.super_time:
            l.debug("MBKMembership-super_time-不一致，self({0}), other({1})".format(self.super_time, other.super_time))
            result = False
        if other.quit_time != self.quit_time:
            l.debug("MBKMembership-quit_time-不一致，self({0}), other({1})".format(self.quit_time, other.quit_time))
            result = False
        if other.upd_time != self.upd_time:
            l.debug("MBKMembership-upd_time-不一致，self({0}), other({1})".format(self.upd_time, other.upd_time))
            result = False
        if other.is_delete != self.is_delete:
            l.debug("MBKMembership-is_delete-不一致，self({0}), other({1})".format(self.is_delete, other.is_delete))
            result = False
        return result
    
    def __ne__(self, other):
        return not self.__eq__(other)