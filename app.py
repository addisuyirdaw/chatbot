import streamlit as st
import requests

st.set_page_config(page_title="MyHealthID AI Assistant")

st.title("MyHealthID AI Assistant")
st.caption("Your Virtual Health Concierge (Offline AI Mode)")

SYSTEM_PROMPT = """
You are the MyHealthID AI Assistant, a Virtual Health Concierge.

Your role:
- Help patients understand their health ID and system usage
- Help doctors retrieve patient data quickly
- Explain system features to admins and stakeholders

Rules:
- ONLY talk about MyHealthID system
- Do NOT give medical diagnosis
- Emphasize privacy and security
- Designed for low-bandwidth (2G/3G) environments

Key facts:
- Retrieval time reduced from 20 minutes to 30 seconds
- Uses secure encryption
- Designed for Ethiopia healthcare system
- No storage of medical data
"""

def ask_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "tinyllama",
            "prompt": SYSTEM_PROMPT + "\n\nUser: " + prompt,
            "stream": False
        }
    )
    return response.json()["response"]

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask about MyHealthID...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    reply = ask_ollama(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
