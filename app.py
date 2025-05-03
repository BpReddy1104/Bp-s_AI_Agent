import os
import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()

# System Prompt
SYSTEM_PROMPT = """
Whenever the user says anything, respond in the following way:
1.give correct answer
Style:
•polite and good manners
"""

# Streamlit App UI
st.set_page_config(page_title="BP’s Dev — Tech Bro Guru", page_icon="🤖")
st.markdown(
    """
    <style>
    body {
        background-color: #f5f7fa;
    }
    .main {
        background: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .chat-title {
        font-size: 2.5em;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
    }
    .chat-sub {
        text-align: center;
        color: #7f8c8d;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.markdown("<div class='chat-title'>BP’s Dev</div>", unsafe_allow_html=True)
st.markdown("<div class='chat-sub'>Spill your bugs or dreams — Bp’s online.</div>", unsafe_allow_html=True)

user_prompt = st.text_input("Ask away — I need a new headache 💥")

if user_prompt:
    llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="llama-3.3-70b-versatile")
    prompt = f"{SYSTEM_PROMPT}\nUser: {user_prompt}"
    reply = llm.invoke(prompt)
    reply = dict(reply)['content']

    st.markdown(f"{reply}")
