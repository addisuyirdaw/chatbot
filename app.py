import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="MyHealthID Assistant", page_icon="🏥", layout="centered")

# 2. Smart Keyword Logic (Designed for Offline Speed)
def get_ai_response(prompt):
    query = prompt.lower()
    
    # Identity & Team
    if any(word in query for word in ["who", "founder", "developed", "addisu", "belay", "team", "created"]):
        return "👋 I am the MyHealthID AI Assistant. I was developed by **Addisu Yirdaw** and **Belay Kassanew**. We are dedicated to building Ethiopia's digital health future."

    # Mission & Purpose
    elif any(word in query for word in ["mission", "purpose", "goal", "why", "vision", "info", "about"]):
        return "🇪🇹 **Our Vision:** We serve the Ethiopian people by ensuring: **No paper, no wasted time, and no long queues.** MyHealthID provides a single digital medical ID for every citizen."

    # Impact on Mothers
    elif any(word in query for word in ["mother", "pregnant", "woman", "child", "family", "help"]):
        return "🤰 **Maternal Health:** MyHealthID ensures prenatal records follow a mother everywhere. In rural clinics, doctors can access her history in 30 seconds to ensure a safe delivery."

    # Technical & Security
    elif any(word in query for word in ["safe", "security", "protect", "tech", "mern", "encrypt", "offline"]):
        return "🛡️ **Technical Specs:** Built with the **MERN stack**, we use **AES-256 encryption**. This system is optimized for **offline deployment** and low-bandwidth (2G/3G) environments."

    # Pilot Location
    elif any(word in query for word in ["where", "apply", "location", "start", "shewa"]):
        return "📍 **Launch:** Our pilot program is starting in the **North Shewa Zone**, specifically targeting health centers that currently rely on paper management."

    # Greetings & Politeness
    elif any(word in query for word in ["thank", "great", "cool", "hello", "hi", "good"]):
        return "It is my honor! MyHealthID is built for the century of digital health in Ethiopia. How else can I help your pitch?"

    else:
        return "I am the MyHealthID expert. You can ask me about our **Founders**, our **Mission**, how we help **Mothers**, or our **Security**."

# 3. Audio Function (Browser-Based TTS)
def speak_text(text):
    clean_text = text.replace('**', '').replace('🏥', '').replace('👋', '').replace('🇪🇹', '').replace('🛡️', '').replace('📍', '').replace('🤰', '')
    components_code = f"""
        <script>
        var msg = new SpeechSynthesisUtterance("{clean_text}");
        window.speechSynthesis.speak(msg);
        </script>
    """
    st.components.v1.html(components_code, height=0)

# 4. Professional UI Display
st.title("🏥 MyHealthID AI Assistant")
st.markdown("### *'No Paper. No Queues. Just Health.'*")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Welcome. I am the voice of MyHealthID. Ask me about our mission or our founders."}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 5. Chat Input Logic
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
        
        # This triggers the voice!
        speak_text(response)
