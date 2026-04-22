import streamlit as st
import time

# 1. Page Setup
st.set_page_config(page_title="MyHealthID Assistant", page_icon="🏥", layout="centered")

# 2. Expert Knowledge Logic (Specific to your Team)
def get_ai_response(prompt):
    query = prompt.lower()
    
    # Who are you?
    if "who are you" in query or "who are u" in query or "developed" in query:
        return "👋 I am the MyHealthID AI Assistant, the digital voice of the MyHealthID system. I was developed by the innovative team of **Addisu Yirdaw** and **Belay Kassanew** to modernize healthcare."

    # Purpose / Mission
    elif "purpose" in query or "goal" in query or "mission" in query or "why" in query:
        return "🇪🇹 **Our Purpose:** We serve the Ethiopian people in this new century. Our mission is: **No more paper, no more wasted time, no more long queues, and no more lost energy.** We bring efficiency to every clinic."

    # For Mothers
    elif "mother" in query or "pregnant" in query:
        return "🤰 **Maternal Health:** MyHealthID ensures a mother's prenatal records follow her everywhere. It saves lives by giving doctors instant access to her history in 30 seconds."

    # Security
    elif "safe" in query or "security" in query:
        return "🛡️ **Security:** We use bank-level AES-256 encryption. Your health data is a private treasure, protected by the best digital locks."

    # Location
    elif "where" in query or "apply" in query:
        return "📍 **Implementation:** We are launching our pilot in the North Shewa Zone to prove that digital health works in both cities and rural health posts."

    # Default Fallback
    else:
        return "I am the MyHealthID expert. Ask me: **Who are you?**, **What is your purpose?**, or **How do you help mothers?**"

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

# 4. UI Display
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
        time.sleep(0.6)
        response = get_ai_response(user_input)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)
        
        # Audio Trigger
        speak_text(response)
