import pymysql
from dbutils.pooled_db import PooledDB

class MySQLHelper:
    """MySQL连接池工具类"""
    
    _pool = None
    
    @staticmethod
    def get_pool():
        if MySQLHelper._pool is None:
            MySQLHelper._pool = PooledDB(
                creator=pymysql,
                maxconnections=10,  # 连接池最大连接数
                mincached=2,        # 初始化时，连接池中至少创建的空闲的链接
                host='localhost',
                port=3306,
                user='root',
                password='123456789',
                database='scrapy_data',
                charset='utf8mb4'
            )
        return MySQLHelper._pool

    @staticmethod
    def get_conn():
        return MySQLHelper.get_pool().connection()