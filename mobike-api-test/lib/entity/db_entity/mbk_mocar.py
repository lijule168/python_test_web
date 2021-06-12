#!/usr/bin/python
# -*- coding:utf-8 -*-

class MBKCarUser:
    id = None
    user_id = None
    iden_front_img = None
    iden_back_img = None
    iden_body_img = None
    driving_license_front_img = None
    driving_license_back_img = None
    deposit_status = None
    is_valid = None
    create_time = None
    update_time = None
    user_name = None
    iden_code = None
    driving_code = None
    iden_status = None
    driving_status = None
    iden_msg = None
    driving_msg = None
    currency = None
    amount = None

class MBKCarBooking:
    id = None
    car_id = None
    user_id = None
    order_id = None
    source_parking_id = None
    destination_parking_id = None
    lon = None
    lat = None
    status = None
    cancel_reason = None
    create_time = None
    end_time = None

class MBKCarOrder:
    id = None
    order_id = None
    user_id = None
    car_id = None
    start_trip_distance = None
    start_lon = None
    start_lat = None
    start_time = None
    total_distance = None
    total_duration = None
    end_time = None
    end_lon = None
    end_lat = None
    source_parking_id = None
    destination_parking_id = None
    total_fee = None
    pay_fee = None
    insurance_fee = None
    deduction_fee = None
    charging_rule_id = None
    status = None
    ts = None
    is_delete = None
    os_platform = None
    os_version = None
    city_code = None
    country_code = None
    app_version = None
    pay_id = None

class MBKCarPeccancyRecord:
    id = None
    order_id = None
    user_id = None
    city_code = None
    status = None
    description = None
    sms_content = None
    deal_type = None
    deal_result = None
    operator_id = None
    operator_name = None
    create_time = None
    update_time = None

class MBKCarDepositRecord:
    id = None
    order_id = None
    user_id = None
    total_fee = None
    currency = None
    status = None
    create_time = None
    update_time = None
    pay_id = None
    source = None

class MBKCarTypeInfo:
    id = None
    name = None
    car_brand = None
    vehicle_type = None
    color = None
    endurance_mileage = None
    energy_consumption = None
    fuel_type = None
    energy_capacity = None
    seating = None
    description = None
    map_icon = None
    img_default = None
    img_hd = None
    img_min = None
    img_1 = None
    img_2 = None
    img_3 = None
    ext_info = None
    create_time = None
    update_time = None
    has_del = None

class MBKCarUserDepositCoupon:
    id = None
    phone_number = None
    user_id = None
    coupon_code = None
    start_time = None
    end_time = None
    coupon_status = None
    job_status = None
    create_time = None
    update_time = None
    is_del = None
