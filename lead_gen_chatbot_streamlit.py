import streamlit as st
from fuzzywuzzy import process
import pandas as pd
import os

# --------------- Page Setup ----------------
st.set_page_config(page_title="Smart Assistant", page_icon="🤖")
st.title("🤖 Welcome Assistant")

# --------------- Sidebar for User Info ----------------
st.sidebar.header("📋 Enter Your Details")
name = st.sidebar.text_input("Your Name")
email = st.sidebar.text_input("Your Email")
phone = st.sidebar.text_input("Your Phone Number")
st.sidebar.caption("🔒 Your data is safe. We don't spam or share information.")

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
        st.sidebar.error("❌ Please complete all fields.")

# --------------- Chatbot Logic ----------------
qa_pairs = {
    ("hi", "hello", "hey", "heyy", "helloo", "helooo"): 
        " Hey there! Great to have you here. How can I assist you today?",
    ("services", "what do you offer", "tell me your services", "what services do you have", "what can you do"): 
        " I can help answer questions, guide you through common queries, and assist you as needed.",
    ("pricing", "cost", "price", "how much", "charges", "fees"): 
        " We offer flexible options depending on your needs. Let me know what you're looking for, and I’ll guide you accordingly.",
    ("24/7", "available anytime", "support hours", "service time", "do you work all time", "always available"): 
        " Yes! I’m always here to chat — anytime you need help or answers.",
    ("bye", "exit", "thank you", "thanks", "see you", "goodbye"): 
        " Thanks for stopping by! Let me know if you need anything else. Have a wonderful day! 😊"
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for questions, answer in qa_pairs.items():
        best_match, score = process.extractOne(user_input, questions)
        if score >= 70:
            return answer
    return "🤖 Hmm, I didn’t quite catch that. Could you please rephrase your question?"

# --------------- Chat State & UI ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

st.write("💬 **Ask me anything. I'm here to help!**")

# Chat input form (to prevent duplicate messages)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", key="user_input")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    response = chatbot_response(user_input)
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", response))

# Show the conversation
for sender, msg in st.session_state.messages:
    with st.chat_message("assistant" if sender == "Bot" else "user"):
        st.markdown(msg)




