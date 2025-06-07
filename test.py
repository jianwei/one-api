import json  
from openai import OpenAI

client = OpenAI(
    api_key="sk-Nsxv8HhG0cCdoTub01A5A8FbD2314703Bc851e80376b87E4", # 从https://cloud.siliconflow.cn/account/ak获取
    base_url="http://localhost:3000/v1"
)

response = client.chat.completions.create(
    model='deepseek-ai/DeepSeek-R1',
    # model="Qwen/Qwen2.5-72B-Instruct",
    messages=[
        {'role': 'user', 
        'content': "推理模型会给市场带来哪些新的机会"}
    ],
    stream=True
)

for chunk in response:
    if not chunk.choices:
        continue
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
    if chunk.choices[0].delta.reasoning_content:
        print(chunk.choices[0].delta.reasoning_content, end="", flush=True)
