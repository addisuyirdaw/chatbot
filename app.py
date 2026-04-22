import streamlit as st
import time

st.set_page_config(page_title="MyHealthID Assistant", page_icon="🏥", layout="centered")

def get_ai_response(prompt):
    query = prompt.lower()
    
    # 1. Greetings & Politeness
    if "thank" in query or "great" in query or "cool" in query:
        return "You're very welcome! It is an honor to serve the Ethiopian healthcare system. Do you have more questions about our mission?"
    elif "hello" in query or "hi" in query:
        return "Hello! I am the MyHealthID Assistant. I am here to show you how we are ending the era of paper records. How can I help you?"

    # 2. Identity & Founders
    elif "who are you" in query or "who are u" in query or "developed" in query:
        return "👋 I am the MyHealthID AI Assistant. I was developed by the innovative team of **Addisu Yirdaw** and **Belay Kassanew** to digitize medical identities."

    # 3. Mission & Purpose (The "Full Info")
    elif "purpose" in query or "goal" in query or "mission" in query or "info" in query:
        return "🇪🇹 **Our Vision:** We serve the Ethiopian people by ensuring: **No paper, no wasted time, and no long queues.** MyHealthID provides a single digital medical ID that stores a patient's entire history securely."

    # 4. Impact on Mothers & Families
    elif "mother" in query or "pregnant" in query or "family" in query:
        return "🤰 **Maternal Health:** MyHealthID ensures prenatal records follow a mother everywhere. Even in rural health posts, doctors can access her history in 30 seconds to ensure a safe delivery."

    # 5. Technical & Security (For the Jury)
    elif "safe" in query or "security" in query or "how" in query:
        return "🛡️ **Technical Specs:** The system uses **AES-256 encryption** and is built with a **MERN stack** (MongoDB, Express, React, Node). It is optimized for **2G/3G networks** to work in remote clinics."

    # 6. Pilot Location
    elif "where" in query or "apply" in query or "location" in query:
        return "📍 **Launch:** We are starting our pilot in the **North Shewa Zone**, specifically targeting regional health centers that currently struggle with paper management."

    else:
        return "I am the MyHealthID expert. You can ask me about our **Founders**, our **Mission**, how we help **Mothers**, or our **Security**."

def speak_text(text):
    clean_text = text.replace('**', '').replace('🏥', '').replace('👋', '').replace('🇪🇹', '').replace('🛡️', '').replace('📍', '').replace('🤰', '')
    components_code = f"""<script>var msg = new SpeechSynthesisUtterance("{clean_text}"); window.speechSynthesis.speak(msg);</script>"""
    st.components.v1.html(components_code, height=0)

st.title("🏥 MyHealthID AI Assistant")
st.markdown("### *'Digital Identity for a Healthier Ethiopia'*")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Welcome. I am the voice of MyHealthID. Ask me anything about our project."}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if user_input := st.chat_input("Ask MyHealthID..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    with st.spinner("Processing..."):
        time.sleep(0.5)
        response = get_ai_response(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)
        speak_text(response)
