'''
Author: sunjie
Date: 2025-03-21 23:26:03
LastEditors: sunj
LastEditTime: 2025-03-21 23:26:57
FilePath: /sunjPy/scrapySj/demos/quotes_spider.py
'''
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/tag/humor/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "author": quote.xpath("span/small/text()").get(),
                "text": quote.css("span.text::text").get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
