from lib.util.log_util import l

class DrcRoutes:
    id = None
    region = None
    ts = None
    select_column = "id,region,ts"

    def __eq__(self, other):
        result = True
        if other.id != self.id:
            l.debug("DrcRoutes-id-不一致，self({0}), other({1})".format(self.id, other.id))
            result = False
        if other.region != self.region:
            l.debug("DrcRoutes-region-不一致，self({0}), other({1})".format(self.region, other.region))
            result = False
        if other.ts != self.ts:
            l.debug("DrcRoutes-ts-不一致，self({0}), other({1})".format(self.ts, other.ts))
            result = False
        return result

    def __ne__(self, other):
        return not self.__eq__(other)


class MBKBikeInfo:
    id = None
    bike_id = None
    model_type = None
    longitude = None
    latitude = None
    location_accuracy = None
    location_data_type = None
    location_update_time = None
    fault_level = None
    lock_status = None
    locked_time = None
    unlocked_time = None
    active_status = None
    stolen_status = None
    place_status = None
    battery_voltage_status = None
    battery_voltage = None
    max_battery_voltage = None
    charging_current = None
    battery_voltage_update_time = None
    hub_battery_voltage = None
    hub_charging_current = None
    signal_quality = None
    mpl_template_id = None
    register_status = None
    create_time = None
    update_time = None
    select_column = "id,bike_id,model_type,longitude,latitude,location_accuracy,location_data_type,location_update_time,fault_level,lock_status,locked_time,unlocked_time,active_status,stolen_status,place_status,battery_voltage_status,battery_voltage,max_battery_voltage,charging_current,battery_voltage_update_time,hub_battery_voltage,hub_charging_current,signal_quality,mpl_template_id,register_status,create_time,update_time"

    def __eq__(self, other):
        result = True

        if other.id != self.id:
            l.debug("MBKBikeInfo-id-不一致，self({0}), other({1})".format(self.id, other.id))
            result = False
        if other.bike_id != self.bike_id:
            l.debug("MBKBikeInfo-bike_id-不一致，self({0}), other({1})".format(self.bike_id, other.bike_id))
            result = False
        if other.model_type != self.model_type:
            l.debug("MBKBikeInfo-model_type-不一致，self({0}), other({1})".format(self.model_type, other.model_type))
            result = False
        if other.longitude != self.longitude:
            l.debug("MBKBikeInfo-longitude-不一致，self({0}), other({1})".format(self.longitude, other.longitude))
            result = False
        if other.latitude != self.latitude:
            l.debug("MBKBikeInfo-latitude-不一致，self({0}), other({1})".format(self.latitude, other.latitude))
            result = False
        if other.location_accuracy != self.location_accuracy:
            l.debug("MBKBikeInfo-location_accuracy-不一致，self({0}), other({1})".format(self.location_accuracy, other.location_accuracy))
            result = False
        if other.location_data_type != self.location_data_type:
            l.debug("MBKBikeInfo-location_data_type-不一致，self({0}), other({1})".format(self.location_data_type, other.location_data_type))
            result = False
        if other.location_update_time != self.location_update_time:
            l.debug("MBKBikeInfo-location_update_time-不一致，self({0}), other({1})".format(self.location_update_time, other.location_update_time))
            result = False
        if other.fault_level != self.fault_level:
            l.debug("MBKBikeInfo-fault_level-不一致，self({0}), other({1})".format(self.fault_level, other.fault_level))
            result = False
        if other.lock_status != self.lock_status:
            l.debug("MBKBikeInfo-lock_status-不一致，self({0}), other({1})".format(self.lock_status, other.lock_status))
            result = False
        if other.locked_time != self.locked_time:
            l.debug("MBKBikeInfo-locked_time-不一致，self({0}), other({1})".format(self.locked_time, other.locked_time))
            result = False
        if other.unlocked_time != self.unlocked_time:
            l.debug("MBKBikeInfo-unlocked_time-不一致，self({0}), other({1})".format(self.unlocked_time, other.unlocked_time))
            result = False
        if other.active_status != self.active_status:
            l.debug("MBKBikeInfo-active_status-不一致，self({0}), other({1})".format(self.active_status, other.active_status))
            result = False
        if other.stolen_status != self.stolen_status:
            l.debug("MBKBikeInfo-stolen_status-不一致，self({0}), other({1})".format(self.stolen_status, other.stolen_status))
            result = False
        if other.place_status != self.place_status:
            l.debug("MBKBikeInfo-place_status-不一致，self({0}), other({1})".format(self.place_status, other.place_status))
            result = False
        if other.battery_voltage_status != self.battery_voltage_status:
            l.debug("MBKBikeInfo-battery_voltage_status-不一致，self({0}), other({1})".format(self.battery_voltage_status, other.battery_voltage_status))
            result = False
        if other.battery_voltage != self.battery_voltage:
            l.debug("MBKBikeInfo-battery_voltage-不一致，self({0}), other({1})".format(self.battery_voltage, other.battery_voltage))
            result = False
        if other.max_battery_voltage != self.max_battery_voltage:
            l.debug("MBKBikeInfo-max_battery_voltage-不一致，self({0}), other({1})".format(self.max_battery_voltage, other.max_battery_voltage))
            result = False
        if other.charging_current != self.charging_current:
            l.debug("MBKBikeInfo-charging_current-不一致，self({0}), other({1})".format(self.charging_current, other.charging_current))
            result = False
        if other.battery_voltage_update_time != self.battery_voltage_update_time:
            l.debug("MBKBikeInfo-battery_voltage_update_time-不一致，self({0}), other({1})".format(self.battery_voltage_update_time, other.battery_voltage_update_time))
            result = False
        if other.hub_battery_voltage != self.hub_battery_voltage:
            l.debug("MBKBikeInfo-hub_battery_voltage-不一致，self({0}), other({1})".format(self.hub_battery_voltage, other.hub_battery_voltage))
            result = False
        if other.hub_charging_current != self.hub_charging_current:
            l.debug("MBKBikeInfo-hub_charging_current-不一致，self({0}), other({1})".format(self.hub_charging_current, other.hub_charging_current))
            result = False
        if other.signal_quality != self.signal_quality:
            l.debug("MBKBikeInfo-signal_quality-不一致，self({0}), other({1})".format(self.signal_quality, other.signal_quality))
            result = False
        if other.mpl_template_id != self.mpl_template_id:
            l.debug("MBKBikeInfo-mpl_template_id-不一致，self({0}), other({1})".format(self.mpl_template_id, other.mpl_template_id))
            result = False
        if other.register_status != self.register_status:
            l.debug("MBKBikeInfo-register_status-不一致，self({0}), other({1})".format(self.register_status, other.register_status))
            result = False
        if other.create_time != self.create_time:
            l.debug("MBKBikeInfo-create_time-不一致，self({0}), other({1})".format(self.create_time, other.create_time))
            result = False
        if other.update_time != self.update_time:
            l.debug("MBKBikeInfo-update_time-不一致，self({0}), other({1})".format(self.update_time, other.update_time))
            result = False
        return result

    def __ne__(self, other):
        return not self.__eq__(other)


class MBKBikeRegion:
    id = None
    bike_id = None
    dc = None
    create_time = None
    update_time = None
    select_column = "id,bike_id,dc,create_time,update_time"

    def __eq__(self, other):
        result = True
        if other.id != self.id:
            l.debug("MBKBikeRegion-id-不一致，self({0}), other({1})".format(self.id, other.id))
            result = False
        if other.bike_id != self.bike_id:
            l.debug("MBKBikeRegion-bike_id-不一致，self({0}), other({1})".format(self.bike_id, other.bike_id))
            result = False
        if other.dc != self.dc:
            l.debug("MBKBikeRegion-dc-不一致，self({0}), other({1})".format(self.dc, other.dc))
            result = False
        if other.create_time != self.create_time:
            l.debug("MBKBikeRegion-create_time-不一致，self({0}), other({1})".format(self.create_time, other.create_time))
            result = False
        if other.update_time != self.update_time:
            l.debug("MBKBikeRegion-update_time-不一致，self({0}), other({1})".format(self.update_time, other.update_time))
            result = False
        return result

    def __ne__(self, other):
        return not self.__eq__(other)
