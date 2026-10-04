#导入依赖文件
import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

# 从env读到key
load_dotenv()

#定义模型
llm = ChatDeepSeek(model="deepseek-chat", api_key=os.getenv("DEEPSEEK_API_KEY"), temperature=0.8)

def main():
    print("我是你的心理陪伴智能体")
    print("有什么不开心都可以和我说")
    while True:
        user_input = input("\n你：").strip()
        reply = llm.invoke(user_input)
        print(f"小暖：{reply.content}")


if __name__ == "__main__":
    main()
