from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
import os

api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="openai/gpt-oss-120b", api_key=api_key)

# api_key = os.getenv("GEMINI_API_KEY")
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=api_key)

# llm_url = "http://127.0.0.1:1234/v1"
# llm = ChatOpenAI(
#     base_url=llm_url,
#     model="google/gemma-3-4b",
#     api_key="dummy-key"
# )

user_input = input("You: ")
# result = llm.invoke(user_input)
# print("AI: ", result.content)
result = llm.stream(user_input)
for chunk in result:
    print(chunk.content, end="")
