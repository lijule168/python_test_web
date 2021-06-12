from lib.mbmanage.dbmanage.mbk_orders_admin import MBKOrdersAdmin


class MBKOrderBusiness:
    def __init__(self, city_code, user_id):
        self.__order_admin = MBKOrdersAdmin(citycode=city_code, user_id=user_id)

    def get_order_detail(self, order_id):
        '''
        获取订单信息
        :param order_id:订单ID
        :return:
        '''
        return self.__order_admin.get_orderinfo_by_orderid(order_id)




