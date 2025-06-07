from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
driver = webdriver.Chrome(options=options)

page_url = 'https://quotes.toscrape.com/tag/humor/'
driver.get(page_url)

try:
    # 使用正确的选择器类型 By.CLASS_NAME
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'container'))
    )

    # 添加更多数据提取
    quotes = driver.find_elements(By.CLASS_NAME, 'quote')
    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, 'text').text
        author = quote.find_element(By.CLASS_NAME, 'author').text
        print(f"作者: {author}")
        print(f"名言: {text}")
        print("-" * 50)

except Exception as e:
    print(f"发生错误: {e}")
finally:
    driver.quit()
