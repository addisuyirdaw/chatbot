import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="MyHealthID Assistant", page_icon="🏥", layout="centered")

# --- SIDEBAR SETTINGS (The Mute Button) ---
with st.sidebar:
    st.title("⚙️ Settings")
    is_muted = st.toggle("Mute AI Voice", value=False)
    st.info("Toggle this to turn the audio on or off for hospital environments.")
    st.divider()
    st.markdown("### Developers\n- Addisu Yirdaw\n- Belay Kassanew")

# 2. Logic & Safety Scripts
def get_ai_response(prompt):
    query = prompt.lower()
    
    # Emergency Keywords
    if any(word in query for word in ["emergency", "urgent", "help", "chest pain", "bleeding"]):
        return """🚨 **Urgent Notice:** If you have an immediate medical emergency, please call our lines right now:
📞 +251 980 353 791 or 0980 354 112"""

    # Mission/Vision
    elif any(word in query for word in ["mission", "vision", "goal", "why"]):
        return "🇪🇹 **Our Vision:** To digitize every medical record in Ethiopia. **No paper, no wasted time, and no long queues.**"

    # Process/Steps
    elif any(word in query for word in ["how", "register", "step", "use"]):
        return "👋 **Process:** 1. Verify ID at clinic -> 2. Digital Check-in -> 3. Fast Doctor Access -> 4. Records follow you everywhere."

    else:
        return "I am the MyHealthID expert. Ask about: **'Emergency'**, **'Mission'**, or **'How to use'**."

# 3. Audio Logic (Controlled by Sidebar Toggle)
def speak_text(text):
    if not is_muted:
        # Clean text for voice engine
        clean_text = text.replace('**', '').replace('🏥', '').replace('👋', '').replace('🇪🇹', '').replace('🚨', 'Alert').replace('📞', 'Call')
        components_code = f"""
            <script>
            var msg = new SpeechSynthesisUtterance("{clean_text}");
            window.speechSynthesis.speak(msg);
            </script>
        """
        st.components.v1.html(components_code, height=0)

# 4. User Interface
st.title("🏥 MyHealthID AI Assistant")
st.markdown("### *Digital Identity for a Healthier Ethiopia*")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Welcome. I am the voice of MyHealthID. How can I help you today?"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if user_input := st.chat_input("Ask MyHealthID..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    response = get_ai_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
    
    speak_text(response)
