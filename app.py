import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="MyHealthID Assistant", page_icon="🏥", layout="centered")

# 2. The Expert Knowledge Logic (Business & User Focused)
def get_ai_response(prompt):
    query = prompt.lower()
    
    # User Journey & How to Use (Step-by-Step)
    if any(word in query for word in ["how", "step", "use", "process", "register", "new", "start"]):
        return """👋 **Welcome to MyHealthID! Here is how you use the system:**
        
1️⃣ **One-Time Registration:** Visit any partner clinic with your National ID. The registrar scans your details to create your Digital Health Profile—no more paper forms.
        
2️⃣ **Digital Check-In:** At your next visit, simply provide your ID. You are added to a digital queue instantly. No more waiting for lost paper folders.
        
3️⃣ **Doctor's Access:** Your doctor opens your secure profile. In under 30 seconds, they see your full history and allergies, ensuring high-quality care.
        
4️⃣ **Seamless Continuity:** Your records follow you everywhere. If you are referred to a city hospital, your data is already there waiting for you."""

    # Identity & Founders
    elif any(word in query for word in ["who", "founder", "developed", "addisu", "belay", "team", "created"]):
        return "👨‍💻 **Our Team:** MyHealthID was developed by **Addisu Yirdaw** and **Belay Kassanew**. We are dual-degree students committed to solving Ethiopia's healthcare challenges through digital innovation."

    # Mission & The "No Paper" Vision
    elif any(word in query for word in ["mission", "purpose", "goal", "vision", "about", "why"]):
        return "🇪🇹 **Our Vision:** To eliminate the burden of paper in healthcare. We ensure: **No paper, no wasted time, no long queues, and no energy lost.** Every Ethiopian citizen deserves a digital health passport that saves lives."

    # Maternal Health
    elif any(word in query for word in ["mother", "pregnant", "woman", "child", "help"]):
        return "🤰 **Maternal Health:** We ensure prenatal records are never lost. Even if a mother visits a new clinic without her documents, the doctor can access her history in seconds, ensuring a safe delivery for both mother and baby."

    # Technical & Security (Business terms)
    elif any(word in query for word in ["safe", "security", "protect", "tech", "mern", "encrypt", "offline"]):
        return "🛡️ **Reliability & Security:** Built on the **MERN stack** with **AES-256 encryption**. MyHealthID is designed for **offline-first** capability, meaning it works in rural clinics even when the internet is down."

    # Greetings & Politeness
    elif any(word in query for word in ["thank", "great", "cool", "hello", "hi", "good"]):
        return "It is an honor to serve you! MyHealthID is the future of digital health in Ethiopia. How else can I assist your presentation?"

    else:
        return "I am the MyHealthID expert. You can ask me: **'How do I use this?'**, **'Who are the founders?'**, or **'What is your mission?'**"

# 3. Browser-Based Audio Function
def speak_text(text):
    # Cleaning text for smoother speech
    clean_text = text.replace('**', '').replace('🏥', '').replace('👋', '').replace('🇪🇹', '').replace('🛡️', '').replace('🤰', '').replace('1️⃣', 'Step 1').replace('2️⃣', 'Step 2').replace('3️⃣', 'Step 3').replace('4️⃣', 'Step 4')
    components_code = f"""
        <script>
        var msg = new SpeechSynthesisUtterance("{clean_text}");
        window.speechSynthesis.speak(msg);
        </script>
    """
    st.components.v1.html(components_code, height=0)

# 4. Professional Interface
st.title("🏥 MyHealthID AI Assistant")
st.markdown("### *Digital Identity for a Healthier Ethiopia*")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Welcome. I am the voice of MyHealthID. How can I help you understand our system?"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 5. Execution Logic
if user_input := st.chat_input("Ask MyHealthID..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("Processing..."):
        time.sleep(0.4)
        response = get_ai_response(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)
        
        # Trigger Voice
        speak_text(response)
