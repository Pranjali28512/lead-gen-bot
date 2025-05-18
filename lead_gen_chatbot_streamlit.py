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

# Save user details to CSV
def save_user_details(name, email, phone):
    new_data = {"Name": name, "Email": email, "Phone": phone}
    file_path = "C:\Users\Parshuram  Dalwai\OneDrive\Desktop\lea\user_data.csv"
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
        st.sidebar.error("❌ Please fill all fields.")

# ---------------- Chatbot Logic ----------------
qa_pairs = {
    ("hi", "hello", "hey", "heyy", "helloo"): "Hi there! How can I help you today?",
    ("services", "what do you offer", "tell me your services", "what services do you have", "what can you do"): 
        "We offer AI-powered lead generation chatbots to help businesses automate customer interactions.",
    ("pricing", "cost", "price", "how much", "charges", "fees"): 
        "Our chatbot services start at an affordable price. Let's discuss your needs!",
    ("bye", "exit", "thank you", "thanks", "see you"): 
        "Thank you! Have a great day! 😊"
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for questions, answer in qa_pairs.items():
        best_match, score = process.extractOne(user_input, questions)
        if score > 70:
            return answer
    return "🤔 I'm not sure I understand. Could you rephrase that?"

# ---------------- Chat Interface ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

st.write("💬 **Chat with our AI Bot about our services**")
user_input = st.text_input("Ask me anything:")

if user_input:
    response = chatbot_response(user_input)
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", response))

for sender, msg in st.session_state.messages:
    st.write(f"**{sender}:** {msg}")
