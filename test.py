import json  
from openai import OpenAI

client = OpenAI(
    api_key="sk-iZcnGEqWdIJDpHoNCaA4AdDd15C84d459072189e1bEe8eB4", # 从https://cloud.siliconflow.cn/account/ak获取
    base_url="http://localhost:4000/v1"
)

response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": "? 2020 年世界奥运会乒乓球男子和女子单打冠军分别是谁? "
             "Please respond in the format {\"男子冠军\": ..., \"女子冠军\": ...}"}
        ],
        response_format={"type": "json_object"}
    )

print(response.choices[0].message.content)