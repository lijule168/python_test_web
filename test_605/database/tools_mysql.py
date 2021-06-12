#encoding= utf-8
from test_605 import tools_ini_config
import pymysql
from pymysql import connect,cursors
import time

class DataBase:

    def __init__(self):
        dbdata=tools_ini_config.ConfigTools('.\config.ini')
        self.host=dbdata.get_config(['mysqlconf','host'])
        self.port=int(dbdata.get_config(['mysqlconf','port']))
        self.user=dbdata.get_config(['mysqlconf','user'])
        self.pwd=dbdata.get_config(['mysqlconf','password'])
        self.dbname=dbdata.get_config(['mysqlconf','db_name'])

        try:
            self.conn=connect(host=self.host,port=self.port,user=self.user,passwd=self.pwd,database=self.dbname)
            print('数据库连接成功')

        except pymysql.Error as e:
            print('表格创建失败'+ str(e))

        # print(self.host,self.port,self.user,self.pwd,self.dbname)

        # 关闭数据库

    # 清除表数据
    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.conn.cursor() as cursor:
            # 取消表的外键约束
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()

    # 插入表数据
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"

        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()

    # 关闭数据库
    def close(self):
        self.conn.close()

    # 初始化数据
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()


