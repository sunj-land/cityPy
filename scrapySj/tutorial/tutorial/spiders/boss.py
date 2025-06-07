'''
Author: sunjie
Date: 2025-03-22 21:53:19
LastEditors: sunj
LastEditTime: 2025-03-22 22:54:33
FilePath: /sunjPy/scrapySj/tutorial/tutorial/spiders/boss.py
'''
import scrapy
import json


class BossSpider(scrapy.Spider):
    name = "boss"

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Host': 'www.zhipin.com',
            'Referer': 'https://www.zhipin.com/web/geek/job',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="122", "Google Chrome";v="122", "Not(A:Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'cookie': 'lastCity=101200100; ab_guid=66b805d2-46db-448c-9647-0c003c40ab7a; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1742651677; HMACCOUNT=E2289034A94BCCB9; __zp_stoken__=7033fMzPDncK0wq%2FCtkAmCAMREgU9JzozJxU%2FMyc%2FOTszMzU3PTMzPRk3I8OlwrPDv8O2w5hhw4jCocK3NCg1OT8zMz85NkAYNT3CuDM0LMKLwrTDvcOzw5pbw4cGwoTCuFcXwrMGfMK5KcKmwrMEYsK2KSXCucK5NzpCOMKww4HDusK9wrPCvsO3wr3DvsOBaMOBOjo4MTE2VRINBTY6SUNUCEhdRF5iTApLUFEoOD01M8O9wr%2FDtCs1EQ8LEBERDwsQEQYECAQFDgwQCw4EBgoFBCs1wpzCt0PEs8SbxKrDqsSUwplNwqLCmMO2wqDCv8Kwwo3Ck8KrwqzCjkpNwq7CpFHCs1LCm8KmwrZgYFpfa8KtwrxwWUxrcU7Ct09vRMOADlF9EBENCg42Eh%2FCicOK; __l=l=%2Fwww.zhipin.com%2Frebots.txt&r=&g=&s=3&friend_source=0&s=3&friend_source=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1742653149; __c=1742651676; __a=92800854.1742651676..1742651676.10.1.10.10'  # 需要添加登录后的cookie
        },
        'ITEM_PIPELINES': {
            'tutorial.pipelines.boss_web.BossWebPipeline': 300,
        },
    }

    def start_requests(self):
        url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json"
        params = {
            'scene': '1',
            'query': 'web前端',
            'city': '101200100',
            'page': '1',
            'pageSize': '30'
        }
        yield scrapy.Request(
            url=f"{url}?{'&'.join(f'{k}={v}' for k, v in params.items())}",
            callback=self.parse,
            dont_filter=True,
            meta={'dont_merge_cookies': True}
        )

    def parse(self, response):
        # 将响应转换为 JSON 对象
        try:
            data = json.loads(response.text)
            # 保存格式化的 JSON
            with open('boss.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            # 处理数据
            if data['code'] == 0:  # 成功响应
                jobs = data.get('zpData', {}).get('jobList', [])
                print(f'成功获取{len(jobs)}条数据')
                for job in jobs:
                    yield {
                        'title': job.get('jobName'),
                        'salary': job.get('salaryDesc'),
                        'company': job.get('companyName'),
                        'location': job.get('cityName')
                    }
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON 解析错误: {e}")
