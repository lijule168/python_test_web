from lib.util.log_util import l

class MBKI18nDepositFreeCard:
    id = None
    user_id = None
    start_timestamp = None
    end_timestamp = None
    type = None
    idempotency_key = None
    is_valid = None
    create_time = None
    update_time = None
    select_column = "id,user_id,start_timestamp,end_timestamp,type,idempotency_key,is_valid,create_time,update_time"

    def __eq__(self, other):
        result = True
        if other.id != self.id:
            l.debug("MBKI18nDepositFreeCard-id-不一致，self({0}), other({1})".format(self.id, other.id))
            result = False
        if other.user_id != self.user_id:
            l.debug("MBKI18nDepositFreeCard-user_id-不一致，self({0}), other({1})".format(self.user_id, other.user_id))
            result = False
        if other.start_timestamp != self.start_timestamp:
            l.debug("MBKI18nDepositFreeCard-start_timestamp-不一致，self({0}), other({1})".format(self.start_timestamp, other.start_timestamp))
            result = False
        if other.end_timestamp != self.end_timestamp:
            l.debug("MBKI18nDepositFreeCard-end_timestamp-不一致，self({0}), other({1})".format(self.end_timestamp, other.end_timestamp))
            result = False
        if other.type != self.type:
            l.debug("MBKI18nDepositFreeCard-type-不一致，self({0}), other({1})".format(self.type, other.type))
            result = False
        if other.idempotency_key != self.idempotency_key:
            l.debug("MBKI18nDepositFreeCard-idempotency_key-不一致，self({0}), other({1})".format(self.idempotency_key, other.idempotency_key))
            result = False
        if other.is_valid != self.is_valid:
            l.debug("MBKI18nDepositFreeCard-is_valid-不一致，self({0}), other({1})".format(self.is_valid, other.is_valid))
            result = False
        if other.create_time != self.create_time:
            l.debug("MBKI18nDepositFreeCard-create_time-不一致，self({0}), other({1})".format(self.create_time, other.create_time))
            result = False
        if other.update_time != self.update_time:
            l.debug("MBKI18nDepositFreeCard-update_time-不一致，self({0}), other({1})".format(self.update_time, other.update_time))
            result = False
        return result

    def __ne__(self, other):
        return not self.__eq__(other)

