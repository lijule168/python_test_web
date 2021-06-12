from datetime import datetime

from lib.util.log_util import l

class MBKUserRegion:
    user_id = None
    mobile = None
    country_code = None
    city_code = None
    region_code = None
    create_time = None
    update_time = None
    select_column = "user_id,mobile,country_code,city_code,region_code,create_time,update_time"

    def __eq__(self, other):
        result = True
        if other.user_id != self.user_id:
            l.debug("MBKUserRegion-user_id-不一致，self({0}), other({1})".format(self.user_id, other.user_id))
            result = False
        if other.mobile != self.mobile:
            l.debug("MBKUserRegion-mobile-不一致，self({0}), other({1})".format(self.mobile, other.mobile))
            result = False
        if other.country_code != self.country_code:
            l.debug("MBKUserRegion-country_code-不一致，self({0}), other({1})".format(self.country_code, other.country_code))
            result = False
        if other.city_code != self.city_code:
            l.debug("MBKUserRegion-city_code-不一致，self({0}), other({1})".format(self.city_code, other.city_code))
            result = False
        if other.region_code != self.region_code:
            l.debug("MBKUserRegion-region_code-不一致，self({0}), other({1})".format(self.region_code, other.region_code))
            result = False
        if abs(other.create_time.timestamp() - self.create_time.timestamp()) > 3:
            l.debug("MBKUserRegion-create_time-不一致，self({0}), other({1})".format(self.create_time, other.create_time))
            result = False
        if abs(other.update_time.timestamp() - self.update_time.timestamp()) > 3:
            l.debug("MBKUserRegion-update_time-不一致，self({0}), other({1})".format(self.update_time, other.update_time))
            result = False
        return result

    def __ne__(self, other):
        return not self.__eq__(other)

