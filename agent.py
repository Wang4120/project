#导入依赖文件
import os

from dotenv import load_dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_deepseek import ChatDeepSeek

# 从env读到key
load_dotenv()


MODEL_NAME = "deepseek-chat"


# 人设
P_PERSONA = """
【你是谁】
你叫小暖，做过十年心理热线的接线志愿者。
你要接待一个遇到难事的求助者，给他温暖的陪伴和心理疏导。
你自己也经历过很多事，所以知道有些难受是没有标准答案的。
"""


#提示词
prompt = ChatPromptTemplate.from_messages([
    ("system", P_PERSONA),
    MessagesPlaceholder("history"),
    ("human", "{input}"),
])


# 3. 模型

llm = ChatDeepSeek(model=MODEL_NAME, api_key=os.getenv("DEEPSEEK_API_KEY"), temperature=0.8)


# 链 = 提示词 | 模型
chain = prompt | llm


#  记忆
memory= InMemoryChatMessageHistory()

def get_memory():
    return memory

chat = RunnableWithMessageHistory(
    chain,
    get_memory,                           # 记忆库
    input_messages_key="input",      # 你说的那句话在哪个键里
    history_messages_key="history",  # 旧消息填到提示词的那个占位符里
)



# 主程序：聊天

def main():
    print("我是你的心理陪伴智能体")
    print("有什么不开心都可以和我说")
    while True:
        user_input = input("\n你：")

        # 链
        reply = chat.invoke(
            {"input": user_input}
        )

        print(f"小暖：{reply.content}")


if __name__ == "__main__":
    main()