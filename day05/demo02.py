import streamlit as st
from langchain.chat_models import init_chat_model
import os

st.title("Langchain Chatbot")

llm = init_chat_model(
    model = "llama-3.3-70b-versatile",
    model_provider = "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("GROQ_API_KEY")
)

user_input = st.chat_input("Say something...")
if user_input:
    result = llm.stream(user_input)
    # msg_box = st.empty()
    # output = ""
    # for chunk in result:
    #     output += chunk.content
    #     msg_box.markdown(output)
    st.write_stream([chunk.content for chunk in result])
