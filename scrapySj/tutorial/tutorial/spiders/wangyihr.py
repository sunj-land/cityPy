'''
Author: sunjie
Date: 2025-03-22 21:53:19
LastEditors: sunj
LastEditTime: 2025-03-23 17:31:21
FilePath: /sunjPy/scrapySj/tutorial/tutorial/spiders/wangyihr.py
'''
import scrapy
import json
from scrapy_splash import SplashRequest


class WangYiHrSpider(scrapy.Spider):
    name = "wangyihr"

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Host': 'hr.163.com',
            'Referer': 'https://hr.163.com/',
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Chromium";v="122", "Google Chrome";v="122", "Not(A:Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
        },
        'DOWNLOAD_DELAY': 2,  # 添加延迟
        'RANDOMIZE_DOWNLOAD_DELAY': True,
        'COOKIES_ENABLED': True,  # 禁用默认cookie
        'DOWNLOADER_MIDDLEWARES': {
            'tutorial.middlewares.selenium_middleware.SeleniumMiddleware': 543,
            # 注释掉或移除 Splash 相关的中间件
            # 'scrapy_splash.SplashCookiesMiddleware': 723,
            # 'scrapy_splash.SplashMiddleware': 725,
            # 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
        },
        # 移除 Splash 相关配置
        # 'SPLASH_URL': 'http://localhost:8050',
        # 'SPIDER_MIDDLEWARES': {
        #     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
        # },
        # 'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
    }

    def start_requests(self):
        url = "https://hr.163.com/job-list.html"
        # 使用普通的 Request 替代 SplashRequest
        yield scrapy.Request(
            url=url,
            callback=self.parse,
            dont_filter=True
        )

    def parse(self, response):
        print("==========")
        # 保存格式化的 JSON
        with open('wangyihr.html', 'w', encoding='utf-8') as f:
            f.write(response.text)

        yield scrapy.Request(
            url="https://hr.163.com/job-detail.html?id=64259&lang=zh",
            callback=self.parseDetail,
            dont_filter=True,
            meta={
                'dont_redirect': True,
                'handle_httpstatus_list': [403],  # 处理403状态,
                'sunjie': "sunjie",
            }
        )

    def parseDetail(self, response):
        print(f"=========={response.meta}")
        # 保存格式化的 JSON
        with open('wangyihrDetail.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
