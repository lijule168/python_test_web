#!/usr/bin/python
# -*- coding:utf-8 -*-

class MBKAbnormalOrder:
    abnormal_order_id = None
    order_id = None
    order_no = None
    status = None
    wx_order_id = None
    wx_amount = None
    retry_count = None
    mobike_uid = None
    thirdparty_uid = None
    application_id = None
    create_time = None
    update_time = None


class MBKActivity:
    activity_id = None
    activity_no = None
    activity_name = None
    activity_desc = None
    application_id = None
    status = None
    policy_id = None
    start_time = None
    end_time = None
    create_time = None
    update_time = None


class MBKActivityOrderMapping:
    activity_mapping_id = None
    order_id = None
    activity_id = None
    application_id = None
    status = None
    type = None
    create_time = None
    update_time = None


class MBKActivityThirdparty:
    activity_thirdparty_id = None
    application_id = None
    activity_content = None
    order_id = None
    create_time = None


class MBKHeaderPicture:
    header_picture_id = None
    url = None
    redirect = None
    enabled = None
    city_code = None
    application_id = None
    created_time = None
    updated_time = None
    select_columns = "header_picture_id, url, redirect, enabled, city_code, application_id, created_time, updated_time"


class MBKLine:
    line_id = None
    line_code = None
    line_name = None
    line_name_en = None
    line_name_short = None
    line_color = None
    line_type = None
    status = None
    application_id = None
    server_version = None
    create_time = None
    update_time = None


class MBKLineStationMapping:
    line_station_mapping_id = None
    line_id = None
    station_id = None
    is_start_station = None
    application_id = None
    status = None
    create_time = None
    update_time = None


class MBKLineStationMappingV1:
    line_station_mapping_id = None
    line_id = None
    station_id = None
    is_start_station = None
    application_id = None
    status = None
    create_time = None
    update_time = None


class MBKLineV1:
    line_id = None
    line_code = None
    line_name = None
    line_name_en = None
    line_type = None
    status = None
    application_id = None
    server_version = None
    create_time = None
    update_time = None


class MBKOrder:
    order_id = None
    order_no = None
    relation_id = None
    application_id = None
    status = None
    price_snapshot_id = None
    ticket_total = None
    amount = None
    real_amount = None
    ticket_code = None
    pay_channel = None
    order_type = None
    create_time = None
    update_time = None


class MBKOrderCopy:
    order_id = None
    order_no = None
    relation_id = None
    application_id = None
    status = None
    price_snapshot_id = None
    ticket_total = None
    amount = None
    real_amount = None
    ticket_code = None
    pay_channel = None
    order_type = None
    create_time = None
    update_time = None


class MBKOrderCopy2:
    order_id = None
    order_no = None
    relation_id = None
    application_id = None
    status = None
    price_snapshot_id = None
    ticket_total = None
    amount = None
    real_amount = None
    ticket_code = None
    pay_channel = None
    order_type = None
    create_time = None
    update_time = None


class MBKOrderDetail:
    order_detail_id = None
    order_id = None
    order_no = None
    relation_id = None
    mobike_uid = None
    thirdparty_uid = None
    application_id = None
    start_line_id = None
    start_line_name = None
    start_station_id = None
    start_station_name = None
    end_line_id = None
    end_line_name = None
    end_station_id = None
    end_station_name = None
    price_snapshot_id = None
    price = None
    status = None
    ticket_total = None
    ticket_real = None
    amount = None
    real_amount = None
    ticket_code = None
    activity_id = None
    pay_channel = None
    order_type = None
    create_time = None
    update_time = None
    shared_order_no = None
    source = None
    orc_order_no = None
    select_columns = "order_detail_id ,order_id ,order_no ,relation_id ,mobike_uid ,thirdparty_uid ,application_id ,start_line_id ,start_line_name ,start_station_id ,start_station_name ,end_line_id ,end_line_name ,end_station_id ,end_station_name ,price_snapshot_id ,price ,status ,ticket_total ,ticket_real ,amount ,real_amount ,ticket_code ,activity_id ,pay_channel ,order_type ,create_time ,update_time, orc_order_no"


class MBKOrderStatus:
    status_id = None
    order_id = None
    parent_order_id = None
    order_type = None
    status = None
    create_time = None
    update_time = None


class MBKOrderStatusSnapshot:
    order_status_snapshot_id = None
    order_id = None
    status = None
    each_ticket_real = None
    wx_transaction_id = None
    pay_transaction_id = None
    wx_pay_time = None
    wx_pay_real_fee = None
    wx_pay_fee = None
    wx_refund_id = None
    pay_refund_id = None
    wx_refund_time = None
    wx_refund_fee = None
    create_time = None
    application_id = None
    order_no = None


class MBKPlatformApplication:
    application_id = None
    city_code = None
    country_code = None
    application_type = None
    application_name = None
    status = None
    create_time = None
    update_time = None


class MBKPlatformConfig:
    config_id = None
    application_id = None
    key = None
    value = None
    status = None
    create_time = None
    update_time = None


class MBKPrice:
    price_id = None
    price = None
    start_station_id = None
    end_station_id = None
    application_id = None
    create_time = None
    update_time = None


class MBKPriceSnapshot:
    price_snapshot_id = None
    price_id = None
    price = None
    currency = None
    create_time = None
    update_time = None


class MBKStation:
    station_id = None
    station_code = None
    station_name = None
    station_name_en = None
    station_first_letter = None
    line_id = None
    city_code = None
    application_id = None
    visible = None
    machine_position = None
    is_transfer_station = None
    last_station_id = None
    next_station_id = None
    server_version = None
    status = None
    machine_status = None
    station_order = None
    loneitude = None
    latitude = None
    create_time = None
    update_time = None
    select_column = "station_id, station_code, station_name, station_name_en, line_id, application_id, station_first_letter, next_station_id, last_station_id"

class MBKStationV1:
    station_id = None
    station_code = None
    station_name = None
    station_name_en = None
    station_first_letter = None
    line_id = None
    city_code = None
    application_id = None
    visible = None
    machine_position = None
    is_transfer_station = None
    last_station_id = None
    next_station_id = None
    server_version = None
    status = None
    loneitude = None
    latitude = None
    create_time = None
    update_time = None


class MBKUserRelation:
    relation_id = None
    mobike_uid = None
    thirdparty_uid = None
    application_id = None
    create_time = None
    update_time = None

    select_column = "relation_id, mobike_uid, thirdparty_uid, application_id, create_time, update_time"