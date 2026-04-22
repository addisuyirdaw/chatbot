import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="MyHealthID Assistant", page_icon="🏥", layout="centered")

# 2. Styling to make it look "AI-like"
st.markdown("""
    <style>
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    .stChatInput { border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏥 MyHealthID AI Assistant")
st.caption("Secure Virtual Health Concierge | Offline-Ready Mode")

# 3. Knowledge Base Logic (No API Required - Zero Errors)
def get_ai_response(prompt):
    query = prompt.lower()
    if "safe" in query or "security" in query or "private" in query:
        return "🛡️ **Security:** MyHealthID uses bank-level AES-256 encryption. Patient data is only decrypted when a verified health professional scans a unique MyHealthID."
    elif "fast" in query or "time" in query or "speed" in query:
        return "⚡ **Efficiency:** We reduce medical record retrieval time from 20 minutes (paper-based) to just 30 seconds (digital)."
    elif "internet" in query or "rural" in query or "village" in query:
        return "📶 **Accessibility:** The system is optimized for low-bandwidth. It is designed to work perfectly on 2G and 3G signals in remote Ethiopian clinics."
    elif "benefit" in query or "why" in query or "problem" in query:
        return "🌟 **Impact:** MyHealthID eliminates lost patient history, reduces diagnosis errors, and ensures doctors have the full medical picture instantly."
    elif "who" in query or "team" in query:
        return "👨‍💻 **Our Team:** We are a group of dedicated students building the digital infrastructure for Ethiopia's future healthcare system."
    else:
        return "I am the MyHealthID expert. You can ask me about our **Security**, **Speed**, or how we work in **Rural areas**."

# 4. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am the MyHealthID AI. How can I help you understand our system today?"}
    ]

# 5. Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 6. Chat Input & Logic
if user_input := st.chat_input("Ask a question about MyHealthID..."):
    # Add User Message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Generate & Display Response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing system data..."):
            time.sleep(0.8)  # Mimics AI processing time
            response = get_ai_response(user_input)
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
