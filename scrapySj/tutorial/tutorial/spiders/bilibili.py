'''
Author: sunjie
Date: 2025-03-22 12:49:18
LastEditors: sunj
LastEditTime: 2025-03-22 22:32:18
FilePath: /sunjPy/scrapySj/tutorial/tutorial/spiders/bilibili.py
'''
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tutorial.items.TutorialItem import TutorialItem


class BilibiliSpider(scrapy.Spider):
    name = "bilibili"
    start_urls = ["http://www.bilibili.com"]  # 修改为 https

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        },
        'FEED_EXPORT_ENCODING': 'utf-8',  # 设置导出编码
        'FEEDS': {
            'bilibili.json': {
                'format': 'json',
                'encoding': 'utf-8',
                'indent': 4,
            }
        },
        "ITEM_PIPELINES": {
            'tutorial.pipelines.bilibili_cursors.BiliBiliCurorsPipeline': 300,
        }
    }

    def parse(self, response):
        # 打印响应状态和内容，便于调试
        self.logger.info(f"状态码: {response.status}")
        # self.logger.info(f"响应头: {response.headers}")

        # 保存响应内容到文件
        with open('bilibili.html', 'w', encoding='utf-8') as f:
            f.write(response.text)

        # 提取链接并返回
        for linkTag in response.css("a.channel-link::text").getall():
            item = TutorialItem()
            item["name"] = linkTag
            yield item
