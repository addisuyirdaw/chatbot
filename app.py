import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="MyHealthID Assistant", page_icon="🏥", layout="centered")

# 2. Comprehensive Business & Safety Logic
def get_ai_response(prompt):
    query = prompt.lower()
    
    # 🚨 THE "URGENT NEED" & SAFETY BYPASS
    # This ensures real emergencies get immediate phone access
    if any(word in query for word in ["emergency", "urgent", "help", "chest pain", "bleeding", "accident", "dying"]):
        return """🚨 **Urgent Notice:** If you have an immediate medical emergency or urgent need, please do not wait for a chat response.
        
**Please call our emergency lines directly right now:**
📞 +251 980 353 791 or 0980 354 112
        
I am an AI assistant here for digital health information. For life-threatening situations, contact emergency services or visit the nearest facility immediately."""

    # 📅 APPOINTMENTS & QUEUE MANAGEMENT
    elif any(word in query for word in ["book", "appointment", "queue", "visit", "time", "wait"]):
        return """📅 **Appointments & Queue:** To ensure everyone receives care as quickly as possible, we follow a **'First-Come, First-Served'** policy.
        
For the **Urgent Queue**, please book your appointment through this system immediately. This helps our medical team at the campus prepare for your arrival and reduces your waiting time."""

    # 👋 USER JOURNEY & REGISTRATION (Business Process)
    elif any(word in query for word in ["how", "step", "use", "process", "register", "new", "start"]):
        return """👋 **Welcome to MyHealthID! Here is our 4-step process:**
        
1️⃣ **Verified Registration:** Visit a partner clinic with your National ID. A registrar verifies your identity to create your Digital Health Profile (prevents fake accounts).
        
2️⃣ **Digital Check-In:** Provide your ID at any facility to enter the digital queue instantly. No paper folders required.
        
3️⃣ **Doctor's Access:** Your doctor opens your secure profile. In under 30 seconds, they see your full history and allergies, ensuring high-quality care.
        
4️⃣ **Seamless Continuity:** Your records follow you everywhere. If you move from rural areas to a city hospital, your data is already there."""

    # 👨‍💻 TEAM & FOUNDERS
    elif any(word in query for word in ["who", "founder", "developed", "addisu", "belay", "team", "created"]):
        return "👨‍💻 **Our Team:** MyHealthID was developed by **Addisu Yirdaw** and **Belay Kassanew**. We are dedicated dual-degree students building the future of Ethiopian healthcare."

    # 🇪🇹 MISSION & VISION
    elif any(word in query for word in ["mission", "purpose", "goal", "vision", "about", "why"]):
        return "🇪🇹 **Our Vision:** To digitize every medical record in Ethiopia. Our mission is: **No paper, no wasted time, no long queues, and no energy lost.**"

    # 🤰 MATERNAL HEALTH
    elif any(word in query for word in ["mother", "pregnant", "woman", "child"]):
        return "🤰 **Maternal Health:** We ensure prenatal records are never lost. Doctors can access history in seconds, ensuring a safe delivery even if you travel far from home."

    # 🛡️ SECURITY & OFFLINE-FIRST
    elif any(word in query for word in ["safe", "security", "protect", "tech", "mern", "encrypt", "offline"]):
        return "🛡️ **Reliability:** Built on the **MERN stack** with **AES-256 encryption**. Designed for **offline-first** capability to work in rural clinics even without internet."

    # 🙏 GREETINGS
    elif any(word in query for word in ["thank", "great", "hello", "hi", "good"]):
        return "It is an honor! MyHealthID is built for the century of digital health in Ethiopia. How else can I assist your presentation?"

    else:
        return "I am the MyHealthID expert. You can ask me about: **'Emergency'**, **'Book Appointment'**, **'Founders'**, or **'How to use'**."

# 3. Audio Accessibility Function
def speak_text(text):
    clean_text = text.replace('**', '').replace('🏥', '').replace('👋', '').replace('🇪🇹', '').replace('🛡️', '').replace('🤰', '').replace('1️⃣', 'Step 1').replace('2️⃣', 'Step 2').replace('3️⃣', 'Step 3').replace('4️⃣', 'Step 4').replace('🚨', 'Alert').replace('📞', 'Call').replace('📅', 'Date')
    components_code = f"""
        <script>
        var msg = new SpeechSynthesisUtterance("{clean_text}");
        window.speechSynthesis.speak(msg);
        </script>
    """
    st.components.v1.html(components_code, height=0)

# 4. Professional User Interface
st.title("🏥 MyHealthID AI Assistant")
st.markdown("### *'Digital Identity for a Healthier Ethiopia'*")

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
        
        speak_text(response)
