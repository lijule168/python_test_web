#!/usr/bin/python
# -*- coding:utf-8 -*-

class MBKFaultCountryConf:
    id = None
    country_code = None
    bike_type = None
    item_id = None
    conf_status = None
    create_time = None
    update_time = None
    operator_id = None

    select_column = "id, country_code, bike_type, item_id, conf_status, create_time, update_time"

class MBKFaultTypeItem:
    id = None
    sub_type = None
    item_name = None
    icon_normal = None
    create_time = None
    sort = None
    update_time = None
    operator_id = None
    platform = None
    resolution = None
    icon_selected = None

    select_column = "id, sub_type, item_name, icon_normal, sort, platform, resolution, icon_selected, create_time, update_time"
class MBKCustomerTicket:
    id = None
    ticket_id = None
    main_type = None
    sub_type = None
    country_code = None
    city_code = None
    user_id = None
    bike_id = None
    order_id = None
    pay_id = None
    handle_type = None
    verify_state = None
    reference_id = None
    source = None
    description = None
    operator_id = None
    status = None
    is_read = None
    longitude = None
    latitude = None
    create_time = None
    update_time = None
