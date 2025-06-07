'''
Author: sunjie
Date: 2025-03-23 17:16:53
LastEditors: sunj
LastEditTime: 2025-03-23 17:17:05
FilePath: /sunjPy/wDemos/seleniumDemo.py
'''
import time
from selenium import webdriver
from sel2enium.webdriver.common.by import By

# 创建Chrome浏览器实例
driver = webdriver.Chrome()

# 打开百度首页
driver.get('https://www.baidu.com')

# 找到搜索框并输入关键词
input_box = driver.find_element(By.ID, 'kw')
input_box.send_keys('Python')

# 找到搜索按钮并点击
search_button = driver.find_element(By.ID, 'su')
search_button.click()

# 等待一段时间，以便查看结果
time.sleep(5)

# 关闭浏览器
# driver.quit()
