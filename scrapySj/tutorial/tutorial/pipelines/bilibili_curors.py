'''
Author: sunjie
Date: 2025-03-21 23:53:50
LastEditors: sunj
LastEditTime: 2025-03-22 22:22:04
FilePath: /sunjPy/scrapySj/tutorial/tutorial/pipelines/bilibili_curors.py
'''
# 保存bilibili 搜索栏内的视频
from .utils.mysql_helper import MySQLHelper


class BiliBiliCurorsPipeline:
    """MySQL数据管道"""

    def __init__(self):
        self.conn = None
        self.cursor = None

    def open_spider(self, spider):
        """爬虫启动时创建数据库连接"""
        self.conn = MySQLHelper.get_conn()
        self.cursor = self.conn.cursor()
        # 创建视频结果表
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bilibili_cursor (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                birthdate VARCHAR(255),
                bio TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def process_item(self, item, spider):
        """处理每个爬取到的数据项"""
        try:

            print(f'bilibili ==== item====={item}')
            self.cursor.execute(
                """
                INSERT INTO authors (name, birthdate, bio)
                VALUES (%s, %s, %s)
                """,
                (item['name'], None, None)
            )
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            spider.logger.error(f"数据保存失败: {e}")
        return item

    def close_spider(self, spider):
        """爬虫结束时关闭数据库连接"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
