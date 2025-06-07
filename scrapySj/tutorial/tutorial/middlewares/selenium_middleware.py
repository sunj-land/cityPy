'''
Author: sunjie
Date: 2025-03-23 17:29:22
LastEditors: sunj
LastEditTime: 2025-03-23 17:32:21
FilePath: /sunjPy/scrapySj/tutorial/tutorial/middlewares/selenium_middleware.py
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.http import HtmlResponse
import time


class SeleniumMiddleware:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 无头模式
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)

    def process_request(self, request, spider):
        print("process_request====", request.url)
        try:
            self.driver.get(request.url)
            time.sleep(5)  # 等待页面加载
            body = self.driver.page_source
            return HtmlResponse(
                url=request.url,
                body=body,
                encoding='utf-8',
                request=request
            )
        except Exception as e:
            spider.logger.error(f'Selenium 请求失败: {e}')
            return None

    def __del__(self):
        self.driver.quit()
