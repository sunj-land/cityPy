'''
Author: sunjie
Date: 2025-03-22 01:14:56
LastEditors: sunj
LastEditTime: 2025-03-22 01:23:03
FilePath: /sunjPy/scrapySj/tutorial/tutorial/spiders/baidu.py
'''
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fake_useragent import UserAgent


class BaiduSpider(CrawlSpider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://www.baidu.com"]

    # 随机生成 User-Agent
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
        },
        'DOWNLOAD_DELAY': 2,  # 延迟2秒
        'COOKIES_ENABLED': False,  # 禁用cookies
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                headers={
                    'User-Agent': UserAgent().random,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                }
            )

    rules = (Rule(LinkExtractor(allow=r"Items/"),
             callback="parse_item", follow=True),)

    def parse_item(self, response):
        item = {}
        # item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # item["name"] = response.xpath('//div[@id="name"]').get()
        # item["description"] = response.xpath('//div[@id="description"]').get()
        return item
