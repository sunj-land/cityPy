'''
Author: sunjie
Date: 2025-03-10 22:24:23
LastEditors: sunj
LastEditTime: 2025-03-10 22:45:41
FilePath: /sunjPy/douban.py
'''
import requests
from lxml import etree
from bs4 import BeautifulSoup

url = "https://read.douban.com/category/100"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


resp = requests.get(url, headers=headers)

resp.encoding = "utf-8"

e = BeautifulSoup(resp.text, "html.parser")
with open("douban.html", "w", encoding="utf-8") as f:
    f.write(resp.text)
titles = map(lambda x: x.text, e.select(".title"))

print(list(titles))
