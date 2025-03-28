import streamlit as st

# Initialize the chatbot UI
st.title("🤖 AI Lead Generation Bot")

# Collect user details
st.sidebar.header("📋 Enter Your Details")
name = st.sidebar.text_input("Your Name")
email = st.sidebar.text_input("Your Email")
phone = st.sidebar.text_input("Your Phone Number")

if st.sidebar.button("Submit"):
    if name and email and phone:
        st.sidebar.success(f"✅ Thank you, {name}! Your details have been saved.")
    else:
        st.sidebar.error("❌ Please fill all fields.")

# Chatbot response logic
def chatbot_response(user_input):
    responses = {
        "hi": "Hi there! How can I help you today?",
        "services": "We offer AI-powered lead generation chatbots to help businesses automate customer interactions.",
        "pricing": "Our chatbot services start at an affordable price. Let's discuss your needs!",
        "exit": "Thank you! Have a great day! 😊"
    }
    return responses.get(user_input.lower(), "I'm sorry, I didn't understand that. Can you rephrase?")

# Chat Interface
st.write("💬 **Chat with our AI Lead Gen Bot**")
user_input = st.text_input("Ask me anything about our services:")
if user_input:
    bot_reply = chatbot_response(user_input)
    st.write(f"🤖 Bot: {bot_reply}")
