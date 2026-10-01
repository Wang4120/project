from langchain_deepseek import ChatDeepSeek
import os
from dotenv import load_dotenv
load_dotenv()
key=os.getenv("DEEPSEEK_API_KEY")
model =ChatDeepSeek(
    model="deepseek-chat",
    temperature=0.7,
    api_key=key
)
response = model.chat("你好呀")
print(response.content)
123