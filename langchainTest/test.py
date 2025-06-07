'''
Author: sunjie
Date: 2025-05-08 21:59:43
LastEditors: sunj
LastEditTime: 2025-05-08 21:59:45
FilePath: /sunjPy/langchainTest/test.py
'''
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# 设置 OpenAI API 密钥
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

# 初始化 OpenAI 模型
llm = OpenAI(temperature=0.7)

# 创建提示模板
prompt = PromptTemplate(
    input_variables=["genre"],
    template="请推荐一部{genre}类型的电影。",
)

# 结合模型和提示模板
chain = LLMChain(llm=llm, prompt=prompt)

# 运行链并获取结果
genre = "科幻"
result = chain.run(genre)
print(result)
