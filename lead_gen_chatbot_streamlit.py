import streamlit as st
from fuzzywuzzy import process
import pandas as pd
import os

# ---------------- UI Setup ----------------
st.set_page_config(page_title="AI Lead Gen Bot", page_icon="🤖")
st.title("🤖 AI Lead Generation Bot")

# ---------------- Sidebar for User Details ----------------
st.sidebar.header("📋 Enter Your Details")
name = st.sidebar.text_input("Your Name")
email = st.sidebar.text_input("Your Email")
phone = st.sidebar.text_input("Your Phone Number")
st.sidebar.caption("🔒 Your information is safe with us. We never spam or share your data.")

def save_user_details(name, email, phone):
    new_data = {"Name": name, "Email": email, "Phone": phone}
    file_path = "user_data.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    else:
        df = pd.DataFrame([new_data])
    df.to_csv(file_path, index=False)

if st.sidebar.button("Submit"):
    if name and email and phone:
        save_user_details(name, email, phone)
        st.sidebar.success(f"✅ Thank you, {name}! Your details have been saved.")
    else:
        st.sidebar.error("❌ Please fill in all fields before submitting.")

# ---------------- Chatbot Logic ----------------
qa_pairs = {
    ("hi", "hello", "hey", "heyy", "helloo", "helooo"): 
        "👋 Hello there! I'm here to help with our AI lead gen services. Ask away!",
        
    ("services", "what do you offer", "tell me your services", "what services do you have", "what can you do"): 
        "📌 We offer smart AI chatbots that engage website visitors, capture leads, and automate customer support 24/7.",
        
    ("pricing", "cost", "price", "how much", "charges", "fees"): 
        "💰 Our pricing is flexible! Plans start affordably, tailored to your business size. Let’s chat details!",
        
    ("24/7", "available anytime", "support hours", "service time", "do you work all time", "always available"): 
        "⏰ Yes! Our AI bots work round the clock, 24/7 — even when you sleep, we capture leads!",
        
    ("bye", "exit", "thank you", "thanks", "see you", "goodbye"): 
        "🙌 Thanks for chatting! Feel free to reach out if you have more questions. Have a great day! 😊"
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for questions, answer in qa_pairs.items():
        best_match, score = process.extractOne(user_input, questions)
        if score >= 70:
            return answer
    return "🤖 Hmm, I didn’t quite catch that. Could you please rephrase your question?"

# ---------------- Chat Interface ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

st.write("💬 **Chat with our AI Bot about our services**")
user_input = st.text_input("Ask me anything about our services:")

if user_input:
    response = chatbot_response(user_input)
    # Avoid duplicate user inputs or bot replies
    if not (st.session_state.messages and st.session_state.messages[-1] == ("You", user_input)):
        st.session_state.messages.append(("You", user_input))
        st.session_state.messages.append(("Bot", response))

# Display chat history
for sender, msg in st.session_state.messages:
    with st.chat_message(sender if sender == "Bot" else "user"):
        st.markdown(msg)


