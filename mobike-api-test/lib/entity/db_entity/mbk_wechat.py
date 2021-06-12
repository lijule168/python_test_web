from lib.util.log_util import l

class MBKCardCityConfig:
    id = None
    city_code = None
    riding_count = None
    card_money = None
    status = None
    create_time = None
    update_time = None
    select_column = "id,city_code,riding_count,card_money,status,create_time,update_time"

    def __eq__(self, other):
        result = True
        if other.id != self.id:
            l.debug("MBKCardCityConfig-id-不一致，self({0}), other({1})".format(self.id, other.id))
            result = False
        if other.city_code != self.city_code:
            l.debug("MBKCardCityConfig-city_code-不一致，self({0}), other({1})".format(self.city_code, other.city_code))
            result = False
        if other.riding_count != self.riding_count:
            l.debug("MBKCardCityConfig-riding_count-不一致，self({0}), other({1})".format(self.riding_count, other.riding_count))
            result = False
        if other.card_money != self.card_money:
            l.debug("MBKCardCityConfig-card_money-不一致，self({0}), other({1})".format(self.card_money, other.card_money))
            result = False
        if other.status != self.status:
            l.debug("MBKCardCityConfig-status-不一致，self({0}), other({1})".format(self.status, other.status))
            result = False
        if other.create_time != self.create_time:
            l.debug("MBKCardCityConfig-create_time-不一致，self({0}), other({1})".format(self.create_time, other.create_time))
            result = False
        if other.update_time != self.update_time:
            l.debug("MBKCardCityConfig-update_time-不一致，self({0}), other({1})".format(self.update_time, other.update_time))
            result = False
        return result

    def __ne__(self, other):
        return not self.__eq__(other)

