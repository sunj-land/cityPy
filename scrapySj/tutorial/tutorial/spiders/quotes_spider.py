import scrapy


class AuthorSpider(scrapy.Spider):
    """作者信息爬虫：爬取作者的详细信息"""

    name = "author"  # 爬虫的唯一标识符

    # 定义起始URL
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        """处理主页面的解析方法
        1. 提取所有作者详情页链接
        2. 提取下一页链接
        """
        # 查找作者链接：选择 .author 类后面的 a 标签
        author_page_links = response.css(".author + a")
        # 跟随所有作者链接，使用 parse_author 方法处理
        yield from response.follow_all(author_page_links, self.parse_author)

        # 查找下一页链接并处理
        pagination_links = response.css("li.next a")
        # 跟随下一页链接，继续使用当前 parse 方法处理
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        """处理作者详情页面的解析方法"""

        def extract_with_css(query):
            """辅助函数：使用CSS选择器提取文本并去除空白
            Args:
                query: CSS选择器字符串
            Returns:
                提取的文本，去除首尾空白
            """
            return response.css(query).get(default="").strip()

        # 生成包含作者详细信息的字典
        yield {
            "name": extract_with_css("h3.author-title::text"),       # 提取作者名称
            "birthdate": extract_with_css(".author-born-date::text"),  # 提取出生日期
            "bio": extract_with_css(".author-description::text"),     # 提取作者简介
        }
