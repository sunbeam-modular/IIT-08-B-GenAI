import os
import requests
import json
import time
from dotenv import load_dotenv
import streamlit as st

st.title("My Chatbot")

load_dotenv()
api_key = "dummy-key"
url = "http://127.0.0.1:1234/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


user_prompt = st.chat_input("Ask anything: ")
if user_prompt:
    req_data = {
        "model": "google/gemma-3-4b",
        "messages": [
            { "role": "user", "content": user_prompt }
        ],
    }
    response = requests.post(url, data=json.dumps(req_data), headers=headers)
    resp = response.json()
    st.write(resp["choices"][0]["message"]["content"])
