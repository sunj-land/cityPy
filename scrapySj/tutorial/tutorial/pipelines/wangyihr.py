'''
Author: sunjie
Date: 2025-03-21 23:53:50
LastEditors: sunj
LastEditTime: 2025-03-22 23:18:31
FilePath: /sunjPy/scrapySj/tutorial/tutorial/pipelines/wangyihr.py
'''
# 保存bilibili 搜索栏内的视频
from tutorial.utils.mysql_helper import MySQLHelper


class WangYiHrPipeline:
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
                title VARCHAR(255),
                salary VARCHAR(255),
                company VARCHAR(255),
                location VARCHAR(255),
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
                INSERT INTO bilibili_cursor (title, salary, company,location)
                VALUES (%s, %s, %s,%s)
                """,
                (item['title'], str(item['salary']),
                 item['company'], item['location'])
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
